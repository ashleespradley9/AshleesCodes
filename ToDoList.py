#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 19:42:45 2025

@author: ashcash

Creating a To-do list application

https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814
"""
def To_Do_List():
    import time
    tasks=[]
        
    while True:
        print("\n=== To-Do List === \n1. Add Task\n2. Show Tasks\n3. Mark Complete\n4. Set Reminder \n5. Exit") 
        user=int(input("Enter your choice: "))

        if user == 1:
            num_tasks=int(input("How many tasks do you want to add? "))
            for i in range(num_tasks): 
                enter_task= input("enter your task ")
                tasks.append({"task": enter_task, "Complete": False})#dictionary in a list
                print("Task added!")
        if user == 2:
            print("Tasks:")
            for i, task in enumerate(tasks,start=1):
                status= "Complete" if task["Complete"] else "Incomplete"
                print(f"{i}.{task['task']}-{status}")
        if user == 3:
            done_task=int(input("Enter the number of the finished task: "))-1
            if done_task < len(tasks):
                tasks[done_task]["Complete"]=True#nested lists
                print("Task Completed")
                #print(tasks)
            else:
                print("Invalid Option")
        if user == 4:#decided to add a reminder to finish tasks because I'm ditzy
            reminder = input("Do you want a reminder to complete tasks? ")
            if reminder == "yes":
                mins = int(input("In how many minutes? ")) 
                secs = mins * 60 
                time.sleep(secs)
                print("Reminder to finish tasks. You're doing great!")
            else:
                continue
        if user == 5:
            print("Existing To Do List")
            break
    else:
        return "Invalid"
if __name__=="__main__":
    To_Do_List()