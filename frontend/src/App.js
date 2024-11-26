// external imports
import {
  ApolloClient,
  ApolloProvider,
  InMemoryCache,
}                            from '@apollo/client';

// internal imports
import                       './App.css';
import Cards                 from './components/Cards';
import Decks                 from './components/Decks';
import CreateDecks           from './components/CreateDecks';


const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphql/',
  cache: new InMemoryCache(),
});

function App() {
  return (
    <ApolloProvider client={client}>
      <div>
        <Cards/>
        <hr/>
        <Decks/>
        <CreateDecks/>
      </div>
    </ApolloProvider>
  );
}

export default App;
