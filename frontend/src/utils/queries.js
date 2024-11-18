// external imports
import { gql }               from '@apollo/client';

export const getCards = gql`{
  cards {
    id
    question
    answer
  }
}`;

export const getDecks = gql`{
  decks {
    id
    title
    description
  }
}`;

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