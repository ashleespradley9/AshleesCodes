#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 19:42:45 2025

@author: ashcash

Creating a To-do list application

https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814
"""
def To_Do_List(user):
    print("=== To-Do List === \n1. Add Task\n2. Show Tasks\n3. Mark Task as Done\n4. Exit")
    user=int(input("Enter your choice"))
    
    if user == 1:
        task1= input("enter your task")
        print("Task added!")
    elif user ==2:
        print("Tasks")
    elif user ==3:
        #mark as done
    elif user == 4:
        #exit
    else:
        return "Invalid"