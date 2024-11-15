// react imports
import React                 from 'react';

// external imports
import {
    gql,
    useQuery,
}                            from '@apollo/client';

const getCards = gql`{
  cards {
    id
    question
    answer
  }
}`;

export default function Cards() {

  const { loading, error, data } = useQuery(getCards);

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
