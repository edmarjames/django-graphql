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