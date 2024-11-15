// react imports
import React, { useEffect }                 from 'react';

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
    data?.cards?.map(data => (
      <div key={data?.id}>
        <p>id: {data?.id}</p>
        <p>question: {data?.question}</p>
        <p>answer: {data?.answer}</p>
      </div>
    ))
  )
};
