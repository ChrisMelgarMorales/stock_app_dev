import React, {  useState, useEffect } from 'react';
import { ActivityIndicator,View, Text,SafeAreaView,StyleSheet, FlatList,Item } from 'react-native';
import { Avatar, Button, Card, Title, Paragraph } from 'react-native-paper';
// client request: fetching todos
import { API } from 'aws-amplify';

const Metrics = (props) => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getMovies = async () => {
     
     try {
        const apiName = 'pythonapi';
        const path = '/func2';
      const json = await API.get(apiName, path, {
        'queryStringParameters': {
          'stock': props.value,
          'day': props.day,
          'month': props.month,
          'year': props.year
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
                <Text>{props.stock}</Text>
            </View>

        )} />
      )}
    </View>
  );
}
export default Metrics;