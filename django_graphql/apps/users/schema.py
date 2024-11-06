import graphene
from graphene_django import DjangoObjectType

from apps.decks.models import Deck
from apps.cards.models import Card
from apps.cards.schema import (
    CardType,
    CreateCard,
    UpdateCard,
    DeleteCard
)
from apps.decks.schema import (
    DeckType,
    CreateDeck,
    UpdateDeck,
    DeleteDeck
)
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

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