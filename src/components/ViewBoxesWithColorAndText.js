import React, {  useState, useEffect } from 'react';
import { ActivityIndicator,View, Text,SafeAreaView,StyleSheet, FlatList,Item } from 'react-native';
import { Avatar, Button, Card, Title, Paragraph } from 'react-native-paper';
// client request: fetching todos
import { API } from 'aws-amplify';

const ViewBoxesWithColorAndText = () => {
    const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getMovies = async () => {
     try {
        const apiName = 'pythonapi';
        const path = '/hello';
      const json = await API.get(apiName, path).data;
      setData(json);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    getMovies();
  }, []);

  return (
    <View style={{ flex: 1, padding: 24 }}>
      {isLoading ? <ActivityIndicator/> : (
        <FlatList
        data={data}
        keyExtractor={({ id }, index) => id}
        renderItem={({ item }) => (
          <Text>{item.message}, {item.open}</Text>
        )}
      />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        textAlign: 'center',
        justifyContent: 'center',
        marginHorizontal: 10,
        marginVertical: 15,
    },
    cardbox:{
        marginVertical:8,
        marginHorizontal:5,
        padding: 10,
    },
    title:{
        backgroundColor: '#e2e2e2',
        fontWeight: 'bold', 
        textAlign:  'center',
        borderRadius: 10,
        paddingVertical: 5 ,
    }
});

export default ViewBoxesWithColorAndText;