import graphene
from graphene_django import DjangoObjectType

from .models import User
from apps.decks.models import Deck
from apps.cards.models import Card


class UserType(DjangoObjectType):
    class Meta:
        model = User

class DeckType(DjangoObjectType):
    class Meta:
        model = Deck

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
            raise Exception("Deck does not exist")

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
            raise Exception("Card not found")

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
            raise Exception("Card not found")

        if card is not None:
            card.delete()

        return DeleteCard(success=True)

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
            raise Exception("Deck not found")

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
            raise Exception("Deck not found")

        if deck is not None:
            deck.delete()

        return DeleteDeck(success=True)

class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
    update_card = UpdateCard.Field()
    delete_card = DeleteCard.Field()
    create_deck = CreateDeck.Field()
    update_deck = UpdateDeck.Field()
    delete_deck = DeleteDeck.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    decks = graphene.List(DeckType)
    decks_by_id = graphene.Field(DeckType, id=graphene.Int())
    cards = graphene.List(CardType)
    cards_by_id = graphene.Field(CardType, id=graphene.Int())
    deck_cards = graphene.List(CardType, deck=graphene.Int())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_decks(self, info, **kwargs):
        return Deck.objects.all()

    def resolve_decks_by_id(self, info, id, **kwargs):
        return Deck.objects.get(pk=id)

    def resolve_cards(self, info, **kwargs):
        return Card.objects.all()

    def resolve_cards_by_id(self, info, id, **kwargs):
        return Card.objects.get(pk=id)

    def resolve_deck_cards(self, info, deck, **kwargs):
        return Card.objects.filter(deck=deck)


schema = graphene.Schema(query=Query, mutation=Mutation)