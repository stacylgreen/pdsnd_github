import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
        city = input('Which city would you like to explore, Chicago, New York City or Washington? ').lower()
        if city in CITY_DATA.keys():
            break
        print("Sorry, that is not a valid response. Please select from listed cities")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Please select a month between January - June or select all: ' ).lower()
        if month in MONTHS:
            break
        print("Please select a month from January through June or type all for all months")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please select a day of the week you would like to explore or select all: ' ).lower()
        if day in DAYS:
            break
        print("Please select day of the week or all")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]

    if day != 'all':
        df = df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}.'.format(MONTHS[most_common_month].title()))

    # TO DO: display the most common day of week
    common_day = df['day'].value_counts()
    print('The most common day is: ', common_day)


    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().head(1)
    print('The most common used start station is: ', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().head(1)
    print('The most common used end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = (df['Start Station'] + df['End Station']).value_counts().head(1)
    print('The most commingly used start and end station: ', most_common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print('The total travel time is: ', travel_time_total, 'seconds')

    # TO DO: display mean travel time
    travel_time_average = df['Trip Duration'].mean()
    print('The average travel time is: ', travel_time_average, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    group_by_user_type = df.groupby(['User Type']).size()
    print("Count of user types:\n ", group_by_user_type)

    # TO DO: Display counts of gender
    try:
        group_by_gender = df['Gender'].value_counts()
        print('Count of each gender:\n', group_by_gender)
    except:
        print('No gender data available for selected city')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min().astype(int)
        most_recent = df['Birth Year'].max().astype(int)
        most_common = df['Birth Year'].mode()[0].astype(int)
        print("The oldest user was born in {}. The youngest was born in {}. People born in {} uses this service most".format(earliest, most_recent, most_common))
    except KeyError:
        print('No birth year data available for selected city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('Would you like to view individual trip data? Yes or no ')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print('Please select yes or no.')
    if display.lower() == 'yes':

        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('Would you like to view more individual trip data? Yes or no.')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print('Please specify yes or no.')
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
