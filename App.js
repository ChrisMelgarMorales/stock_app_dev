import { Amplify } from 'aws-amplify';
import { API } from 'aws-amplify';
import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import awsExports from './src/aws-exports';
import {  Button } from 'react-native';
import StockInfo from './src/panels/StockInfo';
import Backtest from './src/panels/Backtest';
import Portfolio from './src/panels/Portfolio';
Amplify.configure(awsExports);





function App({ signOut, user }) {
  //
  return (
    <>
      <h1>Hello {user.username}</h1>
      
      <StockInfo data = "GOOG"></StockInfo>
      <Backtest data = "GOOG"></Backtest>
      <Portfolio></Portfolio>
      <button onClick={signOut}>Sign out</button>
    </>
  );
}

export default withAuthenticator(App);