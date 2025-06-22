import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';  

export default function GreetMeApp() {
   const [name, setName] = useState('');

   return(
    <View style={styles.container}>
      <Text style={styles.title}>Hello! What's your name?</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your name"
        value={name}
        onChangeText={setName}
      />
      <Text style={styles.greeting}>Hi, {name ? name:'there'}!</Text>
       </View>);
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    color: '#333',
  },
  input: {
    borderWidth: 1,
    borderColor: '#555',
    backgroundColor: '#fff',
    padding: 10,
    width: '80%',
    marginBottom: 20,
    borderRadius: 5,
  },
  greeting: {
    fontSize: 20,
    fontWeight: 'bold'
  },
});