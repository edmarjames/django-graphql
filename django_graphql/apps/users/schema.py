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
    class Arguments:
        deck_id = graphene.ID(required=True)
        question = graphene.String(required=True)
        answer = graphene.String(required=True)
        bucket = graphene.Int(required=True)

    card = graphene.Field(CardType)

    def mutate(self, info, deck_id, question, answer, bucket):
        deck = Deck.objects.get(pk=deck_id)
        card = Card(deck=deck, question=question, answer=answer, bucket=bucket)
        card.save()
        return CreateCard(card=card)

class CreateDeck(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    deck = graphene.Field(DeckType)

    def mutate(self, info, title, description):
        deck = Deck(title=title, description=description)
        deck.save()
        return CreateDeck(deck=deck)

class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
    create_deck = CreateDeck.Field()


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