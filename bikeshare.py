import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = CITY_DATA.keys()
        city = input("Type a city to explore. Please enter chicago, new york city, or washington").lower()
        if city in cities:
            
            break
        else:
            print('please enter a valid city')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = input("Which month would you like to explore?  valid months: all,january, february, march, april, may, or june").lower()
        
        if month == 'all':
            print("you're going to explore the data for all the months")
            break
        elif month in months:
            print("you're going to explore the data for{}".format(month.title()))
            break
        else:
            print('please enter a valid month')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ('saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday')
        day = input("Type a day to explore. Please enter 'all'or any spesific day ").lower()
        
        if day == 'all':
            print("you're going to explore the data for all the days")
            break
        elif day in days:
            print("you're going to explore the data for {}".format(day.title()))
            break
        else:
            print('please enter a valid day')
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # TO DO: display the most common month
    the_most_common_month = df['month'].mode()[0]
    print("The most common month is: ", the_most_common_month)

    # TO DO: display the most common day of week

    the_most_common_day = df['day_of_week'].mode()[0]
    print("The most common day is: ", the_most_common_day)
    
    # TO DO: display the most common start hour
    the_most_common_hour = df['hour'].mode()[0]
    print("The most common hour is: ", the_most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_st_station = df['Start Station'].value_counts().nlargest(1)
    print("The most commonly used start station is: ", most_used_st_station)


    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].value_counts().nlargest(1)
    print("The mmost commonly used end station is: ", most_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination =df.groupby(['End Station'])['Start Station'].count().nlargest(1)
    print(' The most frequent combination is ',most_frequent_combination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() 
    print("The total travel time is: ", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() 
    print("The mean travel time is: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df.groupby(['Gender'])['User Type'].count()
    #count_of_user_types = df['User Type'].value_counts().sum()
    print("The counts of user type is: ", count_of_user_types)


    # TO DO: Display counts of gender
#    count_of_gender = df.groupby(['User Type'])['Gender'].count()
    #count_of_gender = df['Gender'].value_counts().sum()
    #print("The counts of gender are: ", count_of_gender)

    if city != 'washington':
            print('The count of gender are: ' , df['Gender'].value_counts() )
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].nsmallest(1)
    most_recent_year = df['Birth Year'].nlargest(1)
    most_common_year=df['Birth Year'].value_counts().nlargest(1)
    print(" The earliest year of birth is ",earliest_year)
    print("The most recent is",most_recent_year)
    print("and the most common year is ", most_common_year)
    
    # view raw data
def show_row_data(df):
    start_loc = 0
    while True:
        view_raw_data = input("Would you like to view 6 rows of individual trip data? Enter 'y' or 'n'").lower()
        if view_raw_data == "y":
            print( df.iloc[ start_loc : start_loc + 6] )
            start_loc += 6
        elif view_raw_data == "n":
            break
        else:
            print(" Sorry you entered invalid Input , try again")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_row_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
