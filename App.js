import { Amplify } from "aws-amplify";
import { API } from "aws-amplify";
import { withAuthenticator } from "@aws-amplify/ui-react";
import "@aws-amplify/ui-react/styles.css";
import awsExports from "./src/aws-exports";
import { Button } from "react-native";
import StockInfo from "./src/panels/StockInfo";
import Backtest from "./src/panels/Backtest";
import { Portfolio } from "./src/panels/Portfolio";
import { View } from "react-native-web";

Amplify.configure(awsExports);

function App({ signOut, user }) {
  //
  return (
    <>
      <h1>
        Hello, UserID: {user.username}! <button>Sign Out</button>
      </h1>

      <h3>NOTE: Check the console Network log for analyst Info.</h3>

      <StockInfo data="GOOG"></StockInfo>
      <Backtest data="GOOG"></Backtest>
      <Button
        onPress={Portfolio}
        title="Insert Sample Portfolio Entry into Database and return to console"
        color="#841584"
        accessibilityLabel="Learn more about this purple button"
      />
    </>
  );
}

export default withAuthenticator(App);
