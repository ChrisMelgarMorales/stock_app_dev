import DropDownPicker from 'react-native-dropdown-picker';
import React, {  useState, useEffect } from 'react';

const Dropdown = () => {
  const [open, setOpen] = useState(false);
  const [value, setValue] = useState(null);
  const [items, setItems] = useState([
    {label: 'Chevron Corp.', value: 'cvx'},
    {label: 'Caterpillar Inc.', value: 'cat'},
    {label: 'Apple Inc', value: 'aapl'},
    {label: 'Nike Inc', value: 'nke'},
    {label: '3M Co.', value: 'mmm'},
    {label: 'Travelers Cos.', value: 'trv'},
    {label: 'Walmart Inc.', value: 'wmt'},
    {label: 'Dow Inc.', value: 'dow'},
    {label: 'Microsoft Corp.', value: 'msft'},
    {label: 'Salesforce Inc.', value: 'crm'},
    {label: 'Verizon Communications Inc.', value: 'vz'},
    {label: 'Goldman Sachs Group Inc.', value: 'gs'},
    {label: 'American Express Co.', value: 'axp'},
    {label: 'International Business Machines Corp.', value: 'ibm'},
    {label: 'Walt Disney Co.', value: 'dis'},
    {label: 'Honeywell International Inc.', value: 'hon'},
    {label: 'JPMorgan Chase & Co.', value: 'jpm'},
    {label: 'Walgreens Boots Alliance Inc', value: 'wba'},
    {label: 'Home Depot Inc.', value: 'hd'},
    {label: 'Visa Inc. Cl A', value: 'v'},
    {label: 'Johnson & Johnson.', value: 'jnj'},
    {label: 'Coca-Cola Co.', value: 'ko'},
    {label: 'UnitedHealth Group Inc.', value: 'unh'},
    {label: 'Boeing Co.', value: 'ba'},
    {label: "McDonald's Corp.", value: 'mcd'},
    {label: 'Cisco Systems Inc.', value: 'csco'},
    {label: 'Merck & Co. Inc.', value: 'mrk'},
    {label: 'Amgen Inc.', value: 'amgn'},
    {label: 'Procter & Gamble Co.', value: 'pg'},
    {label: 'Intel Corp.', value: 'intc'},
  ]);

  return (
    <DropDownPicker
      open={open}
      value={value}
      items={items}
      setOpen={setOpen}
      setValue={setValue}
      setItems={setItems}
      onChangeValue={(value)=>(console.log(value))}
    />
  );
};
export default Dropdown;
