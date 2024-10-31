import graphene
from graphene_django import DjangoObjectType

from .models import User
from apps.decks.models import Deck
from apps.cards.models import Card


class UserModel(DjangoObjectType):
    class Meta:
        model = User

class DeckModel(DjangoObjectType):
    class Meta:
        model = Deck

class CardModel(DjangoObjectType):
    class Meta:
        model = Card


class CreateCard(graphene.Mutation):
    class Arguments:
        deck_id = graphene.ID(required=True)
        question = graphene.String(required=True)
        answer = graphene.String(required=True)
        bucket = graphene.Int(required=True)

    card = graphene.Field(CardModel)

    @classmethod
    def mutate(cls, root, info, deck_id, question, answer, bucket):
        deck = Deck.objects.get(pk=deck_id)
        card = Card(deck=deck, question=question, answer=answer, bucket=bucket)
        card.save()
        return CreateCard(card=card)


class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserModel)
    decks = graphene.List(DeckModel)
    cards = graphene.List(CardModel)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_decks(self, info, **kwargs):
        return Deck.objects.all()

    def resolve_cards(self, info, **kwargs):
        return Card.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)