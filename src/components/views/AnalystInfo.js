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
          'stock': props.value
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
    <Text>Check the console Network log for analyst Info</Text>
  );
}
export default AnalystInfo;