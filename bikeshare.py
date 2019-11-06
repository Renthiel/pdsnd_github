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
    city = input('Would you like to see data for Chicago, New York, or Washington?\n'
                 'Please choose Chicago, New York City, or Washington to continue.\n')
    if city.lower() in ['chicago','new york city','washington']:
      print('Showing you data for the City of:', city)
    else:
      city = input('\nThat is not a valid choice, please choose again.\n')
    city = CITY_DATA[city.lower()]

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please choose a month to see more data.\n'
                  'Please choose: all, january, february, march, april, may, or june.\n')
    if month.lower() in['january', 'february', 'march', 'april', 'may', 'june', 'all']:
      print('Showing data for the month of:', month)
    else:
      month = input('n\That is not a valid month, please choose again.\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease choose a day of the week. sunday, monday, tuesday, wednesday, thursday, friday, saturday, or all?\n')
    if day.lower() in ['sunday', 'monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'all']:
      print('You have chosen:', day)
    else:
      day = input('\nThat is not a listed day, please choose again.\n')

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
    df = pd.read_csv(city)
    start_time = pd.to_datetime(df['Start Time'])             
    df['month'] = start_time.dt.strftime("%B")
    df['day'] = start_time.dt.strftime("%A")
    df['hour'] = start_time.dt.strftime("%H")
                 
    if month != 'all':
      df = df[df['month'] == month.title()]
                 
    if day != 'all':
      df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month for bike use was:', common_month)             

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day for bike use:', common_day)             

    # TO DO: display the most common start hour
    mostcommonhour = int(df['hour'].mode()[0])
    if mostcommonhour == 0:
      print('The most common hour is: 12 a.m.')
    if mostcommonhour == 12:
      print('The most common hour is: 12 p.m.')
    if mostcommonhour <= 11:
      print('The most common hour is: {} a.m.'.format(mostcommonhour))
    if mostcommonhour > 12:
      mostcommonhour -= 12
      print('The most common hour is: {} p.m.'.format(mostcommonhour))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstat = df['Start Station'].mode()[0]
    print('Most popular start station was:', startstat)

    # TO DO: display most commonly used end station
    endstat = df['End Station'].mode()[0]
    print('Most popular end station was:', endstat)

    # TO DO: display most frequent combination of start station and end station trip
    df['combined_start_end'] = 'Starting Station:' + df['Start Station'] + 'to Ending Station:' + df['End Station']
    most_common_trip = df['combined_start_end'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['total_travel_time'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    
    #TO DO: calculate total travel time
    totaltravtime = df['total_travel_time'].sum()
    print('Total bike ride time:', totaltravtime)

    # TO DO: display mean travel time
    mean_time = df['total_travel_time'].mean()
    print('Average travel time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    u_types = df['User Type'].value_counts()
    print(u_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
      gender_count = df['Gender'].value_counts()
      print(gender_count)
    else:
        print('There is no gender information for Washington')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
      early_year = df['Birth Year'].min()
      print('The earliest birth year was:', int(early_year))
      recent_year = df['Birth Year'].max()
      print('The mose recent birth year was:', int(recent_year))
      common_year = df['Birth Year'].mode()[0]
      print('The most common birth year was:', int(common_year))
    else:
        print('There is no birth year info for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start = 0
        while True:
            if start == 0:
                raw_data = input('\nWould you like to see five rows of data that was used to calculate the stats?\n'
                                 'Please enter yes or no.\n')
            else:
                raw_data = input('\nWould you care to see five more rows of data?\n'
                                 'Please enter yes or no.\n')
                
            if raw_data.lower() == 'no':
                break
            elif raw_data.lower() == 'yes':
                print(df.iloc[start:start+5])
                start += 5
            else:
                print('That is not a valid choice, please type yes or no')
                
        restart = input('\nWould you like to restart? Enter yes or no. If you choose no, the program will end.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
