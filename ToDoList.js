import React, {useState} from 'react';
import { StyleSheet, Text, View, Button, TextInput, TouchableOpacity } from 'react-native';

export default function App() {
  const [task,addTask] = useState('');
  const [tasks, setTasks] = useState([]);

  function toggleDone(index){
    const updatedTasks = [...tasks];
    updatedTasks[index].done = !updatedTasks[index].done;
    setTasks(updatedTasks);
  }

  return (
    <View style={styles.container}>
      <Text style={styles.titel}>
      Welcome!
      </Text>
      <TextInput
        style = {styles.input}
        placeholder = "Enter a task"
        value = {task}
        onChangeText={addTask}
      />
      <Button title = "Add Task" 
      onPress={() => {
        setTasks([...tasks,{text: task,done:false}])
        addTask('')
      }} />
      {tasks.map((item,index)=>(
        <TouchableOpacity key={index} onPress={()=> toggleDone(index)}>
        <Text style={item.done ? styles.doneTask : styles.task}>
          {item.text}
        </Text>
        </TouchableOpacity>
      ))}
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
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    height: 40,
    width: '80%',
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 10,
    marginBottom: 10,
  },
task: {
  fontSize: 18,
  marginVertical: 5,
},
doneTask: {
  fontSize: 18,
  marginVertical: 5,
  textDecorationLine: 'line-through',
  color: 'gray',
},

});
