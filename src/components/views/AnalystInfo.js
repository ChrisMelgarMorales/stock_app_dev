import React, {  useState, useEffect } from 'react';
import { ActivityIndicator,View, Text,SafeAreaView,StyleSheet, FlatList,Item } from 'react-native';
import { Avatar, Button, Card, Title, Paragraph } from 'react-native-paper';
// client request: fetching todos
import { API } from 'aws-amplify';

const AnalystInfo = (props) => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  
  const getMovies = async () => {
     
     try {
        const apiName = 'pythonapi';
        const path = '/analyst';
      const json = await API.get(apiName, path, {
        'queryStringParameters': {
          'stock': props.value,
          'lower': props.lower,
          'upper': props.upper
        }
      });
      setData(json.data);
      console.log(data);
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
                <Text>Check the console Network log for analyst Info</Text>
                <Text>Firm: {item.Date}</Text>
                <Text>Firm: {item.Firm}</Text>
                <Text>Firm: {item.Action}</Text>
            </View>

        )} />
      )}
    </View>
  );
}
export default AnalystInfo;