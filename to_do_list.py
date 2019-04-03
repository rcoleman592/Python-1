#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan Coleman
3-27-19
Python 1 Spring 2019
To-Do List
"""
main_menu = ["View items in your todo list",\
             "View items you have completed",\
             "Add an item to your todo list",\
             "Mark an item as complete",\
             "Exit the Application. (The list will not be saved!)"]


    
    
def choose_menu_option(the_list):
    display_list(the_list)
    user_input = int(input("Please choose a number from the menu options above: "))
    index = user_input - 1
    return index



def add_item(the_list):
    user_string= input("What would you like to add?: ")
    the_list.append(user_string)
    #return None

def finished_item(finished_list, list_todo):
    
    if len(list_todo) == 0:
        print("There is nothing on the list!")
    else:
       index= choose_menu_option(list_todo)
       finished_list.append(list_todo[index])
       list_todo.remove(list_todo[index])
           
    #return None

def display_list(the_list):
    
    number= 1
    
    if len(the_list) == 0:
        print("There is nothing on the list!")
    else:
       for item in the_list:
           print (number,'.', item.capitalize())
           number= number + 1

        


def main():
    todo_list = [ ]
    done_list = [ ]
    program_run = True
    while program_run < 4 or program_run > 1:
        user_choice = choose_menu_option(main_menu)
        
        print("")
        if user_choice == 0:
           display_list(todo_list)
           print("")
            
        elif user_choice == 1:
            display_list(done_list)
            print("")
            
        elif user_choice == 2:
            add_item(todo_list)
            print("")
            
        elif user_choice == 3:
            finished_item(done_list,todo_list)
            print("")
            
        elif user_choice == 4:
            program_run = False
            print("")
            
        else: 
            print("That was not a valid input!")
            
main()

    
