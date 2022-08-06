import { Amplify } from 'aws-amplify';
import { API } from 'aws-amplify';
import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import awsExports from './src/aws-exports';
import {  Button } from 'react-native';
import StockInfo from './src/panels/StockInfo';
Amplify.configure(awsExports);





function App({ signOut, user }) {
  //
  return (
    <>
      <h1>Hello {user.username}</h1>
      
      <StockInfo></StockInfo>
      

      <button onClick={signOut}>Sign out</button>
    </>
  );
}

export default withAuthenticator(App);