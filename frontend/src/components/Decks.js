// react imports
import React                 from 'react';

// external imports
import { useQuery }          from '@apollo/client';

// internal imports
import { getDecks }          from '../utils/queries';


export default function Decks() {

  const { loading, error, data } = useQuery(getDecks);

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error.message}</p>

  return (
    <>
      <h2>Decks</h2>
      {data?.decks?.map(data => (
        <ul key={data?.id}>
          <li>id: {data?.id}</li>
          <li>title: {data?.title}</li>
          <li>description: {data?.description}</li>
        </ul>
      ))}
    </>
  )
};

