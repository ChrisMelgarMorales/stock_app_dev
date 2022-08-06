// @ts-check
import { initSchema } from '@aws-amplify/datastore';
import { schema } from './schema';



const { Portfolio } = initSchema(schema);

export {
  Portfolio
};