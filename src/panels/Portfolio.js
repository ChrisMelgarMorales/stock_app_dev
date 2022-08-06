import * as queries from '../graphql/queries';
import * as mutations from '../graphql/mutations';
import * as subscriptions from '../graphql/subscriptions';
import { API } from 'aws-amplify';

export function Portfolio () {

const PortfolioDetails = {
        ShorthandStockName: 'AAPL',
        Date: '2020-01-01',
        Strategy: 'Simple'
      };
async function asyncCall() {
    const newPortfolio = await API.graphql({ query: mutations.createPortfolio, variables: {input: PortfolioDetails}});
    const allPortfolio = await API.graphql({ query: queries.listPortfolios });
    console.log(allPortfolio); // result: { "data": { "listTodos": { "items": [/* ..... */] } } }
}
asyncCall();
}
