import React,{useState} from 'react'; //useState is a React hook which Keeps track of a value over time inside your component
// And notifies React when that value changes
import {View, TextInput,Text,StyleSheet,Button,Alert } from 'react-native'; //View is a container that supports layout with flexbox, style, some touch handling, and accessibility controls. TextInput is a basic component that allows the user to enter text

//step 2
export default function App() {
const [exercise,setExercise] = useState('');
const [weight,setWeight] = useState('');
const [reps,setReps] = useState(''); 
const [workouts, setWorkouts] = useState([]);

function handleSave() {
    // Validate inputs
if(!exercise || !weight || !reps){
    Alert.alert("Please fill in all fields");
    return;
}

let currentWorkout = {
    id: Date.now(),
    exercise: exercise,
    weight: parseFloat(weight), // Convert weight to a float
    reps: parseInt(reps)
};

setWorkouts([...workouts,currentWorkout]); 

  setExercise('');
  setWeight('');
  setReps('');
}

const styles= StyleSheet.create({
  container:{
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'gray'
    },
  
  input:{
    borderWidth: 1,
    borderColor: '#000',
    padding: 10,
    margin: 10,
    width: '80%'
  },
});

//step 3

return (
  <View style={styles.container}>
    <Text style ={styles.title}>My Fitness App</Text>
<TextInput 
  style={styles.input}
  placeholder="Exercise"
  value={exercise}
  onChangeText={setExercise}
/>
<TextInput 
  style={styles.input}
  placeholder="Weight"
  value={weight}
  onChangeText={setWeight}
  keyboardType="numeric"
/>
<TextInput 
  style={styles.input}
  placeholder="Reps"
  value={reps}
  onChangeText={setReps}
/> 
<Button title="Save Workout" onPress={handleSave}/>

{workouts.map((workout) => (
  <View key={workout.id}>
    <Text>Exercise: {workout.exercise}</Text>
    <Text>Weight: {workout.weight}</Text>
    <Text>Reps: {workout.reps}</Text>
  </View>
))}
</View>);
//step 4 

}