import * as queries from './graphql/queries';
import * as mutations from './graphql/mutations';
import * as subscriptions from './graphql/subscriptions';
import { API } from 'aws-amplify';

const Portfolio = (props) => {

const PortfolioDetails = {
        ShorthandStockName: 'AAPL',
        Date: '2020-01-01',
        Strategy: 'Simple'
      };
      
const newPortfolio = await API.graphql({ query: mutations.createPortfolio, variables: {input: PortfolioDetails}});
// Simple query
const allPortfolio = await API.graphql({ query: queries.listPortfolio });
console.log(allPortfolio); // result: { "data": { "listTodos": { "items": [/* ..... */] } } }
}
export default Portfolio;