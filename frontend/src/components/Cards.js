// react imports
import React, { useEffect }  from 'react';

// external imports
import { useQuery }          from '@apollo/client';

// internal imports
import { getCards }          from '../utils/queries';


export default function Cards() {

  const { loading, error, data } = useQuery(getCards);

  useEffect(() => {
    console.log(error);
  }, [error]);

  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error.message}</p>

  return (
    <>
      <h2>Cards</h2>
      {data?.cards?.map(data => (
        <ul key={data?.id}>
          <li>id: {data?.id}</li>
          <li>question: {data?.question}</li>
          <li>answer: {data?.answer}</li>
        </ul>
      ))}
    </>
  )
};
