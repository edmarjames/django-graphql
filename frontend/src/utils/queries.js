// external imports
import { gql }               from '@apollo/client';

export const getCards = gql`{
  cards {
    id
    question
    answer
  }
}`;

export const getCardsByDeck = gql`
  query($deck: Int) {
    deckCards(deck: $deck) {
      id
      question
      answer
    }
  }
`;

export const getDecks = gql`{
  decks {
    id
    title
    description
  }
}`;

export const getDeck = gql`
  query($id: Int) {
    decksById(id: $id) {
      id
      title
      description
    }
  }
`;

export const addDeck = gql`
  mutation ($title: String!, $description: String!) {
    createDeck(title: $title, description: $description) {
      deck {
        id
        title
        description
      }
    }
  }
`;