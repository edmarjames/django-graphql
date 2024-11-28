// react imports
import React, {
  lazy,
  Suspense,
  useState,
}                            from 'react';

// external imports
import { useQuery }          from '@apollo/client';

// internal imports
import { getDecks }          from '../utils/queries';
import ErrorBoundary         from '../utils/ErrorBoundary';
const DeckDetails =          lazy(() => import('./DeckDetails'));


export default function Decks() {

  const [selectedDeck, setSelectedDeck] = useState(null);
  const { loading, error, data } = useQuery(getDecks);

  function handleSelect (deckId) {
    setSelectedDeck(parseInt(deckId));
  };

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error.message}</p>

  return (
    <>
      <h2>Decks</h2>
      {data?.decks?.map(data => (
        <ul key={data?.id}>
          <li onClick={() => handleSelect(data?.id)}>{data?.title}</li>
        </ul>
      ))}
      <h2>Deck Details here</h2>
      <ErrorBoundary fallback={<h3>No selected deck yet</h3>}>
        <Suspense fallback={<h2>Loading...</h2>}>
          {selectedDeck && <DeckDetails deckId={selectedDeck}/>}
        </Suspense>
      </ErrorBoundary>
    </>
  )
};

