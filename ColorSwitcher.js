import React, { useState } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

export default function App() {
  const [bgColor, setBgColor] = useState('white');
  const colors = ['red','green','blue','yellow','purple','orange','pink'];
  
  const changeColor = ()=>{
    const randomColor = colors[Math.floor(Math.random()*colors.length)];
    setBgColor(randomColor);
  };
  
  return (
    <View style={[styles.container, { backgroundColor: bgColor }]}>
      <Text style={styles.text}> Tap the button below to change the background color! </Text>
      <Button title = "Change Color" onPress={changeColor}/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
