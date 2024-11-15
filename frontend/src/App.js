// external imports
import {
  ApolloClient,
  ApolloProvider,
  InMemoryCache,
}                             from '@apollo/client';

// internal imports
import                       './App.css';
import Cards                  from './components/Cards';


const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphql/',
  cache: new InMemoryCache(),
});

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <Cards/>
      </div>
    </ApolloProvider>
  );
}

export default App;