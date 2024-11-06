import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Deck


class DeckType(DjangoObjectType):
    class Meta:
        model = Deck

class CreateDeck(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    deck = graphene.Field(DeckType)

    def mutate(self, info, title, description):
        deck = Deck(title=title, description=description)
        deck.save()
        return CreateDeck(deck=deck)

class UpdateDeck(graphene.Mutation):
    deck = graphene.Field(DeckType)

    class Arguments:
        deck_id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, deck_id, title=None, description=None):
        try:
            deck = Deck.objects.get(pk=deck_id)
        except Deck.DoesNotExist:
            raise GraphQLError("Deck not found")

        if deck is not None:
            if title is not None:
                deck.title = title
            if description is not None:
                deck.description = description
            deck.save()

        return UpdateDeck(deck=deck)

class DeleteDeck(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        deck_id = graphene.ID(required=True)

    def mutate(self, info, deck_id):
        try:
            deck = Deck.objects.get(pk=deck_id)
        except Deck.DoesNotExist:
            raise GraphQLError("Deck not found")

        if deck is not None:
            deck.delete()

        return DeleteDeck(success=True)