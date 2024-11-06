import graphene
from apps.decks.models import Deck
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Card


class CardType(DjangoObjectType):
    class Meta:
        model = Card

class CreateCard(graphene.Mutation):
    card = graphene.Field(CardType)

    class Arguments:
        deck_id = graphene.ID(required=True)
        question = graphene.String(required=True)
        answer = graphene.String(required=True)
        bucket = graphene.Int(required=True)

    def mutate(self, info, deck_id, question, answer, bucket):
        try:
            deck = Deck.objects.get(pk=deck_id)
            card = Card(deck=deck, question=question, answer=answer, bucket=bucket)
            card.save()
        except Deck.DoesNotExist:
            raise GraphQLError("Deck does not exist")

        return CreateCard(card=card)

class UpdateCard(graphene.Mutation):
    card = graphene.Field(CardType)

    class Arguments:
        card_id = graphene.ID(required=True)
        question = graphene.String()
        answer = graphene.String()
        bucket = graphene.Int()

    def mutate(self, info, card_id, question=None, answer=None, bucket=None):
        try:
            card = Card.objects.get(pk=card_id)
        except Card.DoesNotExist:
            raise GraphQLError("Card not found")

        if card is not None:
            if question is not None:
                card.question = question
            if answer is not None:
                card.answer = answer
            if bucket is not None:
                card.bucket = bucket
            card.save()

        return UpdateCard(card=card)

class DeleteCard(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        card_id = graphene.ID(required=True)

    def mutate(self, info, card_id):
        try:
            card = Card.objects.get(pk=card_id)
        except Card.DoesNotExist:
            raise GraphQLError("Card not found")

        if card is not None:
            card.delete()

        return DeleteCard(success=True)