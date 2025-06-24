import React, {useState} from 'react';
import {Text,View, StyleSheet, Button} from 'react-native';

const quotes = [
  "Believe you can and you're halfway there.",
  "Push yourself, because no one else is going to do it for you.",
  "The pain you feel today will be the strength you feel tomorrow.",
  "Don't watch the clock; do what it does. Keep going.",
  "Success doesn’t just find you. You have to go out and get it."
]
export default function App(){
    const [currentQuote, setCurrentQuote]= useState(quotes[0]);
    return(
        <View style={styles.container}>
          <Text style={styles.title}>Welcome to Motivational Quotes!</Text>
            <Text style={styles.quoteText}>{currentQuote}</Text>
            <Button
                title="Get Motivated!"
                onPress={()=>{
                  let randomIndex;
                  do {
                    randomIndex = Math.floor(Math.random() * quotes.length);
                  } while (quotes[randomIndex] === currentQuote);
                  setCurrentQuote(quotes[randomIndex]);
                }}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container:{
        flex:1,
        justifyContent:'center',
        alignItems:'center',
        padding:20,
        backgroundColor:'#eee',
    },
    quoteText:{
        fontSize:22,
        fontStyle:'italic',
        textAlign:'center',
    }
});
