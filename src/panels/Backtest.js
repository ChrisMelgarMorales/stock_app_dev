import React, { useState } from "react";
import { Text, TextInput, View, Button } from "react-native";
import DropDownPicker from "react-native-dropdown-picker";
import Metrics from "../components/views/Metrics";

const Backtest = (props) => {
  const [value, setValue] = useState(null);
  const [stock, setStock] = useState("");
  const [open, setOpen] = useState(false);
  const [items, setItems] = useState([
    { label: "Chevron Corp.", value: "cvx" },
    { label: "Caterpillar Inc.", value: "cat" },
    { label: "Tesla Inc.", value: "tsla" },
    { label: "Apple Inc.", value: "aapl" },
    { label: "Nike Inc.", value: "nke" },
    { label: "Cloudflare Inc.", value: "net" },
    { label: "3M Co.", value: "mmm" },
    { label: "Travelers Cos.", value: "trv" },
    { label: "Walmart Inc.", value: "wmt" },
    { label: "Dow Inc.", value: "dow" },
    { label: "Microsoft Corp.", value: "msft" },
    { label: "Salesforce Inc.", value: "crm" },
    { label: "Verizon Communications Inc.", value: "vz" },
    { label: "Goldman Sachs Group Inc.", value: "gs" },
    { label: "American Express Co.", value: "axp" },
    { label: "International Business Machines Corp.", value: "ibm" },
    { label: "Walt Disney Co.", value: "dis" },
    { label: "Honeywell International Inc.", value: "hon" },
    { label: "JPMorgan Chase & Co.", value: "jpm" },
    { label: "Walgreens Boots Alliance Inc", value: "wba" },
    { label: "Home Depot Inc.", value: "hd" },
    { label: "Visa Inc. Cl A", value: "v" },
    { label: "Johnson & Johnson.", value: "jnj" },
    { label: "Coca-Cola Co.", value: "ko" },
    { label: "UnitedHealth Group Inc.", value: "unh" },
    { label: "Boeing Co.", value: "ba" },
    { label: "McDonald's Corp.", value: "mcd" },
    { label: "Cisco Systems Inc.", value: "csco" },
    { label: "Merck & Co. Inc.", value: "mrk" },
    { label: "Amgen Inc.", value: "amgn" },
    { label: "Procter & Gamble Co.", value: "pg" },
    { label: "Intel Corp.", value: "intc" },
  ]);
  const changeState = () => {
    setStock(stock);
  };
  return (
    <View style={{ padding: 10, marginBottom: 50 }}>
      <DropDownPicker
        open={open}
        value={value}
        items={items}
        setOpen={setOpen}
        setValue={setValue}
        setItems={setItems}
        onChangeValue={(newStock) => setStock(newStock)}
      />
      <Button
        onPress={changeState}
        title="Submit Backtesting Parameters"
        color="#841584"
        accessibilityLabel="Learn more about this purple button"
      />
      <Metrics
        value={props.data}
        day="01"
        year="2020"
        month="01"
        funds="100000"
        strat="smacross"
      ></Metrics>
      <Text>
        [01-01-2020] test at starting with $100000 using smascross strategy
        requested
      </Text>
      <Metrics
        value={props.data}
        day="01"
        year="2020"
        month="01"
        funds="100000"
        strat="smatrailcross"
      ></Metrics>
      <Text>
        [01-01-2020] test at starting with $100000 using smastrailcross strategy
        requested
      </Text>
    </View>
  );
};

export default Backtest;
