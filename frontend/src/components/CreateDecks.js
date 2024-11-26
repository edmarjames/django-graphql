// react imports
import React, {
  useRef
}                            from 'react';

// external imports
import { useMutation }       from '@apollo/client';

// internal imports
import { addDeck, getDecks } from '../utils/queries';


export default function CreateDecks(props) {

  const titleRef = useRef(null);
  const descriptionRef = useRef(null);
  const [createDeck, { data, loading, error }] = useMutation(addDeck, {
    refetchQueries: [
      getDecks
    ],
  });

  function handleChangeTitle(e) {
    titleRef.current = e.target.value;
  };
  function handleChangeDescription(e) {
    descriptionRef.current = e.target.value;
  };
  function handleSubmit(e) {
    e.preventDefault();
    createDeck({
      variables: {
        title: titleRef?.current,
        description: descriptionRef?.current
      }
    });
  };

  if (loading) return <div>loading...</div>
  if (error) return <p>Error: {error.message}</p>

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <div>
        <label htmlFor="title">Title: </label>
        <input
          ref={titleRef}
          type="text"
          name="title"
          onChange={(e) => handleChangeTitle(e)}
        />
      </div>
      <div>
        <label htmlFor="description">Description: </label>
        <textarea
          ref={descriptionRef}
          name="description"
          onChange={(e) => handleChangeDescription(e)}
        />
      </div>
      <button>Save</button>
    </form>
  )
};

