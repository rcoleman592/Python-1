#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan Coleman
Python 1 Spring 2019
5-1-2019
Final Project: Data Analysis
"""

#function that calculates the average point per game
def average_calculator(points_total_list):
    season_total_points = sum(points_total_list)
    season_total_games = len(points_total_list)
    total_season_average = season_total_points / season_total_games
    
    return total_season_average

    
def main():
    
    #opening and writing to a new file
    raw_data_file = open("harden_stats.csv", "r")
    neat_data_file = open("neat_stats_harden.txt", "w")
    
    #reading in the lines from the original file
    lines_of_data = raw_data_file.readlines()
    
    #empty list for # of games played
    games_played = []
    
    #empty list for dates of the games played
    date_played = []
    
    #empty list for number of points scored in each games this season
    points_scored = []
    
    # lists for separating each game into what month it was played
    october_games = []
    november_games = []
    december_games = []
    jan_games = []
    feb_games = []
    march_games = []
    april_games = []
    
    #cleaning up the file and splitting each part of the text document into a string
    for data in lines_of_data: 
        data = data.rstrip("\n")
        data = data.split(",")
        #print(data)
        if data[0].isdigit():
            #adding each game played into games_played as integer
            games_played.append(int(data[0]))
            #adding the dates of each game played into dates_played as string
            date_played.append(data[1])
            #adding the points scored in each game to points_scored as integer
            points_scored.append(int(data[2]))
    #calling the average function to calculate the PPG for all games
    season_total_average = average_calculator(points_scored)
    
    #printing his season average
    print("James Harden's PPG for 2018-2019 Season: ", format(season_total_average,
          ",.2f"))
    print("\n")
    
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("James Harden's PPG for 2018-2019 Season: ")
    neat_data_file.write(format(season_total_average, ",.2f"))
    neat_data_file.write("\n")
    
    #Taking each game played per month and putting it  into each monthly list
    for month in date_played:
        month = month.rstrip("\n")
        month = month.split("-")
        if month[1] == "10":
           october_games.append(int(month[2]))
        if month[1] == "11":
            november_games.append(int(month[2]))
        if month[1] == "12":
            december_games.append(int(month[2]))
        if month[1] == "01":
            jan_games.append(int(month[2]))
        if month[1] == "02":
            feb_games.append(int(month[2]))
        if month[1] == "03":
            march_games.append(int(month[2]))
        if month[1] == "04":
            april_games.append(int(month[2]))
    
    print("Monthly Breakdown:")
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("Monthly Breakdown: ")
    neat_data_file.write("\n")

    
    #calling average function and calculating october average   
    october_average = average_calculator(october_games)
    print("October Average: ")
    print(format(october_average, ",.2f"))
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("October Average: ")
    neat_data_file.write(format(october_average, ",.2f"))
    neat_data_file.write("\n")
    
    #calling average function and calculating november games
    nov_average = average_calculator(november_games)
    print("November Average: ") 
    print(format(nov_average, ",.2f"))   
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("November Average: ")
    neat_data_file.write(format(nov_average, ",.2f"))
    neat_data_file.write("\n")

    
    #calling average function and calculating december games
    dec_average = average_calculator(december_games)
    print("December Average: ")
    print(format(dec_average, ",.2f"))
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("December Average: ")
    neat_data_file.write(format(dec_average, ",.2f"))
    neat_data_file.write("\n")
    
    #calling average function and calculating january games
    jan_average = average_calculator(jan_games)
    print("January Average: ") 
    print(format(jan_average, ",.2f"))
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("January Average: ")
    neat_data_file.write(format(jan_average, ",.2f"))
    neat_data_file.write("\n")
    
    #calling average function and calculating feb games
    feb_average = average_calculator(feb_games)
    print("February Average: ")
    print(format(feb_average, ",.2f"))
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("February Average: ")
    neat_data_file.write(format(feb_average, ",.2f"))
    neat_data_file.write("\n")
    
    #calling average function and calculating march games
    march_average = average_calculator(march_games)
    print("March Average: ")
    print(format(march_average, ",.2f"))
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("March Average: ")
    neat_data_file.write(format(march_average, ",.2f"))
    neat_data_file.write("\n")
    
    #calling average function and calculating april games
    april_average = average_calculator(april_games)
    print("April Average: ") 
    print(format(april_average, ",.2f"))
    #writing to new doc neat_stats_harden.txt
    neat_data_file.write("April Average: ")
    neat_data_file.write(format(april_average, ",.2f"))
    neat_data_file.write("\n")
    

    raw_data_file.close()
    neat_data_file.close()
main() 