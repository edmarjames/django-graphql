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
    data?.decks?.map(data => (
      <div key={data?.id}>
        <p>id: {data?.id}</p>
        <p>title: {data?.title}</p>
        <p>description: {data?.description}</p>
      </div>
    ))
  )
};

