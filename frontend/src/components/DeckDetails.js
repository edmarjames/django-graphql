import React from 'react';

import { useQuery }          from '@apollo/client';

import { getDeck }           from '../utils/queries';


export default function DeckDetails({ deckId }) {

  const { loading, error, data } = useQuery(getDeck, {
    variables: { id: deckId }
  });

  if (!data) return <p>No selected deck yet.</p>
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error.message}</p>

  return (
    <div>
      <p>id: {data?.decksById?.id}</p>
      <p>title: {data?.decksById?.title}</p>
      <p>description: {data?.decksById?.description}</p>
    </div>
  )
};
