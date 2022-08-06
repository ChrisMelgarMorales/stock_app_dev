import { ModelInit, MutableModel, PersistentModelConstructor } from "@aws-amplify/datastore";





type PortfolioMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

export declare class Portfolio {
  readonly id: string;
  readonly Date?: string | null;
  readonly ShorthandStockName?: string | null;
  readonly Strategy?: string | null;
  readonly createdAt?: string | null;
  readonly updatedAt?: string | null;
  constructor(init: ModelInit<Portfolio, PortfolioMetaData>);
  static copyOf(source: Portfolio, mutator: (draft: MutableModel<Portfolio, PortfolioMetaData>) => MutableModel<Portfolio, PortfolioMetaData> | void): Portfolio;
}