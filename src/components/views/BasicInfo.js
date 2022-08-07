import React, {  useState, useEffect } from 'react';
import { ActivityIndicator,View, Text,SafeAreaView,StyleSheet, FlatList,Item } from 'react-native';
import { Avatar, Button, Card, Title, Paragraph } from 'react-native-paper';
// client request: fetching todos
import { API } from 'aws-amplify';

const BasicInfo = (props) => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  
  const getMovies = async () => {
     
     try {
        const apiName = 'pythonapi';
        const path = '/hello';
      const json = await API.get(apiName, path, {
        'queryStringParameters': {
          'stock': props.value
        }
      });
      setData(json.data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    if(props.value !== '' ){
      getMovies();
    }
    else{
      setLoading(false);
    }
  }, []);

  return (
    <View style={{ flex: 1, padding: 24 }}>
      {isLoading ? <ActivityIndicator/> : (
        <FlatList
        data={data}
        renderItem={({ item }) => (
            <View>
                <Text>Information for stock {props.value}</Text>
                <Text>Open: {item.open}</Text>
                <Text>Close: {item.close}</Text>
                <Text>Bid: {item.bid}</Text>
                <Text>Ask: {item.ask}</Text>
                <Text>Volume: {item.volume}</Text>
                <Text>PEG Ratio: {item.pegRatio}</Text>
                <Text>Trailing EPS: {item.trailingEps}</Text>
                <Text>Forward EPS: {item.forwardEps}</Text>
            </View>

        )} />
      )}
    </View>
  );
}
export default BasicInfo;