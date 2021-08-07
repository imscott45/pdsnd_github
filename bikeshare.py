import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington d.c.': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - index of the month in MONTHS to filter by, 0 = all or no filter
        (int) day - index of the day of week to filter by, 7 = all or no filter
    """
    print('\x1bc')
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print(" Please Select a City\n --------------------\n |1. Chicago         |\n |2. New York        |\n |3. Washington D.C. |\n |4. Quit            |\n --------------------\n")
        city = input("Select a number from the menu: ").lower()
        if city == '1':
            print('\x1bc')
            city = 'chicago'
            break
        elif city == '2':
            print('\x1bc')
            city = 'new york city'
            break
        elif city == '3':
            print('\x1bc')
            city = 'washington d.c.'
            break
        elif city == '4':
            quit()
            break
        else:
            print('\x1bc') 
            print("please enter a number from the menu like 1 for Chicago\n")
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        print(" City: " + city.title() + '\n')
        print(" Would you like to filter by Month?\n --------------------\n |1. No              |\n |2. January         |\n |3. February        |\n |4. March           |\n |5. April           |\n |6. May             |\n |7. June            |\n |8. Quit            |\n --------------------\n")
        month = input("Select a number from the menu: ").lower()
        if month == '1':
            print('\x1bc')
            month = 0
            break
        elif month == '2':
            print('\x1bc')
            month = 1
            break
        elif month == '3':
            print('\x1bc')
            month = 2
            break
        elif month == '4':
            print('\x1bc')
            month = 3
            break
        elif month == '5':
            print('\x1bc')
            month = 4
            break
        elif month == '6':
            print('\x1bc')
            month = 5
            break
        elif month == '7':
            print('\x1bc')
            month = 6
            break
        elif month == '8':
            quit()
            break
        else:
            print('\x1bc') 
            print("please enter a number from the menu like 1 for No filter\n")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print(" City: " + city.title())
        print(" Month: " + MONTHS[month].capitalize() + '\n')
        print(" Would you like to filter by a day?\n --------------------\n |1. No              |\n |2. Monday          |\n |3. Tuesday         |\n |4. Wednesday       |\n |5. Thursday        |\n |6. Friday          |\n |7. Saturday        |\n |8. Sunday          |\n |9. Quit            |\n --------------------\n")
        day = input("Select a number from the menu: ").lower()
        if day == '1':
            print('\x1bc')
            day = 7
            break
        elif day == '2':
            print('\x1bc')
            day = 0
            break
        elif day == '3':
            print('\x1bc')
            day = 1
            break
        elif day == '4':
            print('\x1bc')
            day = 2
            break
        elif day == '5':
            print('\x1bc')
            day = 3
            break
        elif day == '6':
            print('\x1bc')
            day = 4
            break
        elif day == '7':
            print('\x1bc')
            day = 5
            break
        elif day == '8':
            print('\x1bc')
            day = 6
            break
        elif day == '9':
            quit()
            break
        else:
            print('\x1bc') 
            print("please enter a number from the menu like 1 for No filter\n")
            continue

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - index of the month in MONTHS to filter by, 0 = all or no filter
        (int) day - index of the day of week to filter by, 7 = all or no filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['start_end'] = df['Start Station'] + ' to ' + df['End Station']

    # filter by month if applicable
    if month != 0:
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 7:
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most popular Month was: ' + MONTHS[df['month'].value_counts().idxmax()].capitalize())

    # display the most common day of week
    print('The most popular Day was: ' + DAYS[df['day'].value_counts().idxmax()].capitalize())

    # display the most common start hour
    print('The most popular Start Hour (24-hour clock) was: ' + str(df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds" % round((time.time() - start_time), 4))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common Starting Location was: ' + df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print('The most common Ending Destination was: ' + df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print('The most common Journey was between: ' + df['start_end'].value_counts().idxmax())

    print("\nThis took %s seconds" % round((time.time() - start_time), 4))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # Calculate human readable time
    def human_time(seconds):
        rem_seconds = int(seconds) % 60
        tot_minutes = int(seconds) // 60
        rem_minutes = tot_minutes % 60
        tot_hours = tot_minutes // 60
        rem_hours = tot_hours % 24
        tot_days = tot_hours // 24
        rem_days = tot_days % 7
        tot_weeks = tot_days // 7
        time_string = str(tot_weeks) + ' weeks, ' + str(rem_days) + ' days, ' + str(rem_hours) + ' hours, ' + str(rem_minutes) + ' minutes, and ' + str(rem_seconds) + ' seconds'
        return time_string
    #Output human readable duration
    print('The Total Travel Time was: ' + human_time(df['Trip Duration'].sum()))

    # display mean travel time
    print('The Average Travel Time was: ' + human_time(round(df['Trip Duration'].mean())))

    print("\nThis took %s seconds" % round((time.time() - start_time), 4))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    users = user_types.index.tolist()
    print('The Types of Users and total for each are: ')
    i = 1
    for user in users:
        print(str(i) +'. ' + user + ' - ' + str(user_types[user]))
        i += 1

    # Display counts of gender
    if city != 'washington d.c.':
        print('\n')
        genders = df['Gender'].value_counts()
        gends = genders.index.tolist()
        print('The Types of Genders and total for each are: ')
        i = 1
        for gend in gends:
            print(str(i) +'. ' + gend + ' - ' + str(genders[gend]))
            i += 1

    # Display earliest, most recent, and most common year of birth
    if city != 'washington d.c.':
        print('\n')
        print('The earliest Birth Year is: ' + str(int(df['Birth Year'].min())))
        print('The latest Birth Year is: ' + str(int(df['Birth Year'].max())))
        print('The most common Birth Year is: ' + str(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds" % round((time.time() - start_time), 4))
    print('-'*40)


def main():
    while True:
        
        city, month, day = get_filters()
        
        print('City:  ' + city.title())
        print('Month: ' + MONTHS[month].capitalize())
        print('Day:   ' + DAYS[day].capitalize())
        print('-'*40)

        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n")
        if view_data.lower() == 'yes':
            start_loc = 0
            while True:
                print(df.iloc[start_loc:(start_loc + 5)])
                start_loc += 5
                view_display = input("\nDo you wish to continue? Enter yes or no.\n").lower()
                if view_display != 'yes':
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
	main()
