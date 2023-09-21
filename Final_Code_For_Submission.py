# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:53:25 2023

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:59:58 2023

@author: hp
"""

import time
import pandas as pd
import numpy as np

# the definition of filtering function based on user search

def get_filters():
    print("Hello! Let's explore some US bikeshare data!")

    city=' '
    while city not in ['chicago','new york','washington']:
         user_city=str(input(' Would you like to see data for Chicago, New York, or Washington?\n')).strip().lower()
         if user_city in ['chicago','new york','washington']:
            city=user_city
         else:
            user_city=str(input(' Invalid city, try again and tell me: Would you like to see data for Chicago, New York, or Washington?\n'))
          


    filter_choice=str(input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter?\n'))
    
    
    month = 'all'  
    day = 'all'
    
    if filter_choice == 'month':
    
       month=' '
       #while month not in ['january','february','march','april','may','june']:
       month=str(input('which month: January, February, March, April, May, June?\n')).lower()
       print(month)
       month_mapping = { 'january': '1',
                          'february': '2',
                          'march': '3',
                          'april': '4',
                          'may': '5',
                          'june': '6'
                            }
       month = int(month_mapping[month])
       print(month)
    
    elif filter_choice == 'day':
       day=' '
       day=int(input('which day: please give it as integer\n'))
    

    elif filter_choice == 'both':
       month=' '
       #while month not in ['january','february','march','april','may','june']:
       month=str(input('which month: January, February, March, April, May, June?\n')).lower()
       print(month)
       month_mapping = { 'january': '1',
                          'february': '2',
                          'march': '3',
                          'april': '4',
                          'may': '5',
                          'june': '6'
                            }
       month = int(month_mapping[month])
       print(month)
       
       day=' '
       day=int(input('which day: please give it as integer\n'))
   
    else:
            month = 'all'
            day='all'
          

    return city, month, day

# save filtering data into a list

#print(city, month, day)

# loading part of the data frame based on the previous filteration process by user

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}


def load_data(city, month, day):
    filename = None  # Initialize filename with a default value
    if city in CITY_DATA:
        filename = CITY_DATA[city]
    else:
        print("City not found in CITY_DATA.")

    if filename is not None:  # Check if filename is defined before proceeding
        df = pd.read_csv(filename)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        print('The month is: ', df['month'])
        df['month'] = df['month'].astype(int)
        df['day'] = df['Start Time'].dt.day
        df['day'] = df['day'].astype(int)

        print(city, month, day)
        print(df.shape)

        if month == 'all' and day == 'all':
            df = df
        elif month != 'all' and day != 'all':
            df = df[df['month'] == month]
            df = df[df['day'] == day]
        elif month != 'all' and day == 'all':
            df = df[df['month'] == month]
        else:
            df = df[df['day'] == day]

        print(df.shape)
        return df
    else:
        return None 


######################  solution to problem 1: popular travel time
def time_stats(df, month, day):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    print(df['month'])
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    if not df.empty:
        if month == 'all':
            popular_month = df['month'].mode()[0]
            print('popular month is: ', popular_month)
        if day == 'all':
            popular_day = df['day'].mode()[0]
            print('popular day is: ', popular_day)

        popular_hour = df['hour'].mode()[0]  # Use 'hour' instead of 'Start Time'
        print('popular hour is: ', popular_hour)
    else:
        print('No data available for the selected filters.')

      

#####################  solution to problem 2: popular stations and trips

def station_stats(df):
   if not df.empty:  # Check if the DataFrame is not empty  
       start_station_counts= df['Start Station'].value_counts()
       print(start_station_counts)

       max_start_station_name = start_station_counts.idxmax()
       max_start_station_counts= start_station_counts.max()
       print('The most common start station is: ', max_start_station_name)


       #common end station 
       end_station_counts= df['End Station'].value_counts()
       print(end_station_counts)

       max_end_station_name = end_station_counts.idxmax()
       max_end_station_counts= end_station_counts.max()
       print('The most common end station is: ', max_end_station_name)

       #common trip comination name
       df['Combined_Column'] = df['Start Station'].str.cat(df['End Station'], sep=',')
       trips_counts= df['Combined_Column'].value_counts()
       max_trip_name = trips_counts.idxmax()
       print('The most common trip  is: ', max_trip_name)

   else:
    print('No data available for the selected filters.')



#################################### solution to problem 3: Trip Duration


def trip_duration_stats(df):
    if not df.empty:  # Check if the DataFrame is not empty 
       total_travel_time=df['Trip Duration'].sum()
       total_travel_time_minutes = total_travel_time / 60
       print('The total travel time in minutes is: ', total_travel_time_minutes)

       average_travel_time=df['Trip Duration'].mean()
       average_travel_time_minutes =average_travel_time/ 60
       print('The average travel time is: ', average_travel_time_minutes)
    else:
      print('No data available for the selected filters.')



#################################### solution to problem 4: User Types
def user_stats(df, city):
    if not df.empty:  # Check if the DataFrame is not empty 
        user_type_counts= df['User Type'].value_counts()
        print(user_type_counts)

        if city != 'washington':
          gender_counts=df['Gender'].value_counts()
          print(gender_counts)

          birth_year_counts=df['Birth Year'].value_counts()
          common_birth_year = birth_year_counts.idxmax()
          print('common year is: ', common_birth_year)
    else:
      print('No data available for the selected filters.')
      
      
def display_data(df):
    start_row = 0
    while True:
        display = input("Do you want to see 5 rows of data? Enter 'yes' or 'no': ").lower()
        if display == 'yes':
            print(df.iloc[start_row:start_row + 5])
            start_row += 5
        elif display == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)
    
    if df is not None:  # Check if df is not None before proceeding
        display_data(df)
        time_stats(df, month, day)  # Pass month and day parameters
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
    else:
        print("No data available for the selected filters.")


if __name__ == "__main__":
    main()
