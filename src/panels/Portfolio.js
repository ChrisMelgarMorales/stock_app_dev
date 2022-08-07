import * as queries from '../graphql/queries';
import * as mutations from '../graphql/mutations';
import * as subscriptions from '../graphql/subscriptions';
import { API } from 'aws-amplify';

export function Portfolio () {

const PortfolioDetails = {
        ShorthandStockName: 'AAPL',
        Date: '2020-01-01',
        Strategy: 'smacross'
      };
async function asyncCall() {
    const newPortfolio = await API.graphql({ query: mutations.createPortfolio,authMode:'AMAZON_COGNITO_USER_POOLS', variables: {input: PortfolioDetails}});
    const allPortfolio = await API.graphql({ query: queries.listPortfolios ,authMode:'AMAZON_COGNITO_USER_POOLS'});
    console.log(allPortfolio); // result: { "data": { "listTodos": { "items": [/* ..... */] } } }
}
asyncCall();
}
