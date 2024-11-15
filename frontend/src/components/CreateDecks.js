import React, {
  useRef
} from 'react';

export default function CreateDecks(props) {

  const titleRef = useRef(null);
  const descriptionRef = useRef(null);

  function handleChangeTitle(e) {
    titleRef.current = e.target.value;
  };
  function handleChangeDescription(e) {
    descriptionRef.current = e.target.value;
  };
  function handleSubmit(e) {
    e.preventDefault();
    console.log(titleRef);
    console.log(descriptionRef);
  };

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <div>
        <label htmlFor="title">Title: </label>
        <input type="text" name="title" ref={titleRef} onChange={(e) => handleChangeTitle(e)}/>
      </div>
      <div>
        <label htmlFor="description">Description: </label>
        <textarea name="description" ref={descriptionRef} onChange={(e) => handleChangeDescription(e)}/>
      </div>
      <button>Save</button>
    </form>
  )
};

