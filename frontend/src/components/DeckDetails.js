import React, {
  useEffect,
  useState
}                            from 'react';

import {
  NetworkStatus,
  useLazyQuery,
  useQuery,
}                            from '@apollo/client';

import {
  getCardsByDeck,
  getDeck,
}                            from '../utils/queries';


export default function DeckDetails({ deckId }) {

  const [relatedCards, setRelatedCards] = useState([]);

  const { loading, error, data, previousData, refetch, networkStatus } = useQuery(getDeck, {
    variables: { id: deckId },
    notifyOnNetworkStatusChange: true,
  });

  const [deckCards, { data: cardData }] = useLazyQuery(getCardsByDeck);

  useEffect(() => {
    if (data?.decksById?.id !== previousData?.decksById?.id) {
      setRelatedCards([]);
    }
  }, [data, previousData]);
  useEffect(() => {
    if (cardData?.deckCards?.length > 0) {
      setRelatedCards(cardData?.deckCards);
    };
  }, [cardData]);

  if (!deckId) return <p>No selected deck yet.</p>
  if (networkStatus === NetworkStatus.refetch) return <p>Refetching...</p>
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error.message}</p>

  return (
    <>
      <div>
        <button onClick={() => refetch()}>Refetch data</button>
        <button onClick={() => deckCards({ variables: {deck: parseInt(data?.decksById?.id)}})}>Get related cards</button>
        <p>id: {data?.decksById?.id}</p>
        <p>title: {data?.decksById?.title}</p>
        <p>description: {data?.decksById?.description}</p>
      </div>
      {relatedCards?.length > 0 && (
        <div>
          <h4>Related cards</h4>
          {relatedCards?.map(data => (
            <div key={data?.id}>
              <p>Id: {data?.id}</p>
              <p>Question: {data?.question}</p>
              <p>Answer: {data?.answer}</p>
              <hr/>
            </div>
          ))}
        </div>
      )}
      {relatedCards?.length === 0 && (
        <h4>No related cards</h4>
      )}
    </>
  )
};
