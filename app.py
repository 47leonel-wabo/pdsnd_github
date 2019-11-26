import pandas as pd
import numpy as np
import os
import time

#***********************************************************************************
# This code is a bit longer, due to extra work made to filter user incorrect inputs
# just for fun. :)
#***********************************************************************************

# Use to clean the console for easy navigation throwgh the whole program
def clear_console():
    '''Clear the console for better readability'''
    
    os.system('cls' if os.name == 'nt' else 'clear')

# Use to get user input and filter it from menu
def user_selected_dataset():
    '''Display a message for dataset selection, control user's input and return user choice'''
    
    d = input('Which dataset would you like to load: ')
    t = True
    while t:
        try:
            d = int(d)
        except ValueError:
            clear_console()
            show_start_menu()
            print('>>> INVALID INPUT! => "{}" <<<'.format(d))
            d = input('Please enter a valid input (1, 2, or 3): ')
        else:
            if d==1 or d==2 or d==3:
                t = False
                return d
            else:
                clear_console()
                show_start_menu()
                print('>>> NO SUCH INPUT! => "{}" <<<'.format(d))
                d = input('Please enter a valid input (1, 2, or 3): ')
filename = ''
# Use to load targeted file based on choice made previously (on the menu 'user_selected_dataset()')
def load_targeted_data(choice):
    ''' Load expected csv file based on user selection through "choice" argument
        RETURN:
            expected dataframe '''
    
    global filename
    if choice == 1:
        print('Loading Chicago...')
        filename = 'chicago.csv'
        return pd.read_csv('./datasets/chicago.csv')
    elif choice == 2:
        print('Loading New York...')
        filename = 'new_york_city.csv'
        return pd.read_csv('./datasets/new_york_city.csv')
    else:
        print('Loading Washington...')
        filename = 'washington.csv'
        return pd.read_csv('./datasets/washington.csv')

# Use to show menu of possible choices to user
def show_start_menu():
    '''Display the main menu - a list of available dataset'''
    
    clear_console()
    print('***********************************************')
    print('****   WHICH DATASET?                      ****')
    print('****      1 - Chicago                      ****')
    print('****      2 - New York                     ****')
    print('****      3 - Washington                   ****')
    print('****> Use number of dataset (1, 2, or 3) < ****')
    print('***********************************************')

# Use to test if user wants to see raw data or not
def ask_for_raw_data():
    '''Display a message asking whether user wants to see raw data, and control user's incorrect inputs
        and return corresponding response (yes or no)'''
    
    raw = input('Would you like to see raw data (y/n): ')
    t = True
    while t:
        try:
            raw = str(raw)
        except:
            clear_console()
            print('INVALID INPUT >>{}<<'.format(raw))
            raw = input('Would you like to see raw data (y/n): ')
        else:
            raw = raw.lower()
            if raw != '':
                raw = raw[0]
            if raw == 'n' or raw == 'y':
                t = False
                return raw
            else:
                clear_console()
                print('INVALID INPUT >>{}<<'.format(raw))
                raw = input('Would you like to see raw data (y/n): ')

def select_filtering_period():
    '''Display a menu of possible filters to be applied to dataset selected previously'''
    
    clear_console()
    print('**************************************')
    print('**** WHICH FILTER TO APPLY?       ****')
    print('****    1 - day                   ****')
    print('****    2 - Month                 ****')
    print('****    3 - both                  ****')
    print('****    4 - None at all           ****')
    print('****> Use number  (1, 2, 3, or 4) < **')
    print('**************************************')
    print('>>>> Filename: '+ filename)

def get_filter_input():
    '''Display available filter for selection, and control user's inputs'''
    
    d = input('Which filter would you like to apply: ')
    t = True
    while t:
        try:
            d = int(d)
        except ValueError:
            clear_console()
            select_filtering_period()
            print('>>> INVALID INPUT! => "{}" <<<'.format(d))
            d = input('Please enter a valid number (1, 2, 3, or 4): ')
        else:
            if d==1 or d==2 or d==3 or d == 4:
                t = False
                return d
            else:
                clear_console()
                select_filtering_period()
                print('>>> NO SUCH INPUT! => "{}" <<<'.format(d))
                d = input('Please enter a valid number (1, 2, 3, or 4): ')

def show_raw_data(df):
    '''Take a dataframe as argument presenting available datasets for selection, and control user's inputs'''
    
    t = True
    end_pt = 6
    yield df[0:end_pt]
    end_pt += 5
    while t:
        try:
            more_data = input('Would you like to see more (y/n): ')
            more_data = str(more_data)
        except:
            clear_console()
            print('INVALID INPUT >>{}<<'.format(more_data))
            more_data = input('More data (y/n): ')
        else:
            more_data = more_data.lower()
            if more_data != '':
                more_data = more_data[0]
            if  more_data == 'y':
                clear_console()
                yield df[0:end_pt]
                end_pt += 5
            elif more_data == 'n':
                t = False
            else:
                clear_console()
                print('INVALID INPUT >>{}<<'.format(more_data))

def one_more_time():
    '''Ask user at the end, whether they want to perform again, and control user's inputs if incorrect'''
    
    t = True
    while t:
        try:
            restart = input('Would you like to restart (y/n): ')
            restart = str(restart)
        except:
            clear_console()
            print('INVALID INPUT >>{}<<'.format(restart))
        else:
            restart = restart.lower()
            restart = restart[0]
            if  restart == 'y' or restart == 'n' and restart != '':
                return restart
            else:
                clear_console()
                print('INVALID INPUT >>{}<<'.format(restart))
                
days_of_week_dict = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}
def print_a_dict(a_dict):
    '''Dispaly a dictionary passed as argument'''
    
    for i, j in a_dict.items():
        print('\t\t {} => {}'.format(i, j))

def filter_per_day(days_of_week_dict):
    '''Get a dictionary representing available days, and control user's inputs'''
    
    print_a_dict(days_of_week_dict)
    selection = input('Which day (1-Sunday; 2-Monday; and so on as listed): ')
    t = True
    while t:
        try:
            selection = int(selection)
        except:
            clear_console()
            print_a_dict(days_of_week_dict)
            print('INVALID INPUT, SELECT CORRESPONDING NUMBER')
            selection = input('Which day (1-Sunday; 2-Monday; and so on as listed): ')
        else:
            if selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5 or selection == 6 or selection == 7:
                t = False
                return selection
            else:
                clear_console()
                print_a_dict(days_of_week_dict)
                print('INVALID INPUT, SELECT CORRESPONDING NUMBER')
                selection = input('Which day (1-Sunday; 2-Monday; and so on as listed): ')

def filter_per_month(month_dict):
    '''Get a dictionary representing available months, and control user's inputs'''
    
    print_a_dict(month_dict)
    month_selected = input('Which month (1-January; 2-February; and so on as listed): ')
    t = True
    while t:
        try:
            month_selected = int(month_selected)
        except:
            clear_console()
            print_a_dict(month_dict)
            print('INVALID INPUT, SELECT CORRESPONDING NUMBER')
            month_selected = input('Which month (1-January; 2-February; and so on as listed): ')
        else:
            if month_selected == 1 or month_selected == 2 or month_selected == 3 or month_selected == 4 or month_selected == 5 or month_selected == 6:
                t = False
                return month_selected
            else:
                clear_console()
                print_a_dict(month_dict)
                print('INVALID INPUT, SELECT CORRESPONDING NUMBER')
                month_selected = input('Which month (1-January; 2-February; and so on as listed): ')

month_dict = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June'
}
def dataframe_for_a_given_day(df, a_day):
    '''Prepare a dataframe for a specific day
    INPUT:
        (data) dataframe object
        (a_day) a number representing a day of week
    RETURN:
        returns a dataframe which match a day passed as argument'''
    
    return data.loc[data['days'] == a_day]

def dataframe_for_a_given_month(data, a_month):
    '''Prepare a dataframe for a specific month
    INPUT:
        (data) dataframe object
        (a_month) a number representing a month
    RETURN:
        returns a dataframe which match a month passed as argument'''
    
    return data.loc[data['months'] == a_month]

def dataframe_for_a_given_day_and_month(data, a_day, a_month):
    '''Prepare a dataframe for a specific day,  and month
    INPUT:
        (data) dataframe object
        (a_day) a number representing a day of week
        (a_month) a number representing a month
    RETURN:
        returns a dataframe which match day and month passed as argument'''
    
    dfd = data.loc[data['days'] == a_day]
    return dfd.loc[dfd['months'] == a_month]

def most_popular_hour(df):
    '''Display stats on most common hour'''
    
    h = df['hours'].value_counts()
    print('* The most common hour is: {}\n\tCount: {}'.format(h.idxmax(), h[h.idxmax()]))

def most_popular_day(df):
    '''Display stats on most common day'''
    
    d = df['days'].value_counts()
    print('* The most common day is: {}\n\tCount: {}'.format(d.idxmax(), d[d.idxmax()]))

def most_popular_month(df):
    '''Display stats on most common month month'''
    
    m = df['months'].value_counts()
    print('* The most common month is: {} ({})\n\tCount: {}'.format(m.idxmax(), month_dict[m.idxmax()], m[m.idxmax()]))

def trip_duration(df):
    '''Display stats on common trip, and mean trip duration'''
    
    td = df['Trip Duration'].value_counts()
    print('* The most common trip duration: {}\n\tCount: {}'.format(td.idxmax(), td[td.idxmax()]))
    print('\tMean: {}'.format(df['Trip Duration'].mean()))

def total_trip_duration(df):
    '''Display total trip duration for a certain period of time, dataframe is already filtered accordingly'''
    
    ttd = df['Trip Duration'].sum()
    print('* Total trip duration (seconds): {}'.format(ttd))

def most_start_and_end_station(df):
    '''Display stats on different stations'''
    
    st = df['Start Station'].value_counts()
    es = df['End Station'].value_counts()
    print('* The most common start station: \n\t{}\n\tCount: {}'.format(st.idxmax(), st[st.idxmax()]))
    print('* The most common end station: \n\t{}\n\tCount: {}'.format(es.idxmax(), es[es.idxmax()]))

def gender_representation(df):
    '''Display stats on different user gender'''
    
    print('** Gender field records {} missing values **'.format((df.isna().sum())['Gender']))
    print('However, Gender distribution is')
    g = df['Gender'].value_counts()
    print('\t{}\n\tCount: {}'.format(g.idxmax(), g[g.idxmax()]))
    print('\t{}\n\tCount: {}'.format(g.idxmin(), g[g.idxmin()]))

def user_bith_years(df):
    '''Display stats on user birth year'''
    
    print('** Birth year field records {} missing values **'.format((df.isna().sum())['Gender']))
    b = df['Birth Year'].value_counts()
    print('The most common birth year is: {} \n\tCount: {}'.format(b.idxmax(), b[b.idxmax()]))

def user_types(df):
    '''Display stats on different user type'''

    print('* Different type of users are:')
    du = df['User Type'].value_counts()
    for cat, num in du.items():
        print('\t{}'.format(cat))
        print('\tCount: {}'.format(num))

def processing_core_operations(input_filter, df):
    '''
    This is the core function, it uses all functions defined above to process expected operation

    INPUT:
        An integer (1, 2, 3, or 4) corresponding to following filters (day, month, both, or not at all) respectively
        A dataframe reference on which different operation is performed

    RETURN:
        None
    '''
    start_time = time.time()
    clear_console()
    if input_filter == 1:
        print('On {} \nDay filter applied'.format(filename))
        selected_day = filter_per_day(days_of_week_dict)
        clear_console()
        print('-' * 70)
        print('On {} dataset\nApplies {} as day filter, following are some stats'.format(filename, days_of_week_dict[selected_day]))
        print('-' * 70)
        dfd = df.loc[df['days'] == selected_day]
        most_popular_hour(dfd)
        trip_duration(dfd)
        total_trip_duration(dfd)
        most_start_and_end_station(dfd)
        if filename != 'washington.csv':
            gender_representation(dfd)
            user_bith_years(dfd)
        user_types(dfd)
        print('-' * 70)

    elif input_filter == 2:
        print('On {} \nMonth filter applied'.format(filename))
        selected_month = filter_per_month(month_dict)
        print('-' * 70)
        print('On {} dataset\nApplies {} month as filter, following are some stats'.format(filename, month_dict[selected_month]))
        print('-' * 70)
        dfm = df.loc[df['months'] == selected_month]
        most_popular_hour(dfm)
        trip_duration(dfm)
        total_trip_duration(dfm)
        most_start_and_end_station(dfm)
        if filename != 'washington.csv': # Because washington dataset has no 'Gender' and 'Birth Year' fields
            gender_representation(dfm)
            user_bith_years(dfm)
        user_types(dfm)
        print('-' * 70)
        print('-' * 70)

    elif input_filter == 3:
        print('On {} \nDay and Month filter applied'.format(filename))
        selected_day = filter_per_day(days_of_week_dict)
        clear_console()
        selected_month = filter_per_month(month_dict)
        print('-' * 70)
        print('On {} dataset\nApplies {} day and {} month as filter, following are some stats'.format(filename, days_of_week_dict[selected_day], month_dict[selected_month]))
        print('-' * 70)
        dfd = df.loc[df['days'] == selected_day]
        dfd_and_m = dfd.loc[dfd['months'] == selected_month]
        most_popular_hour(dfd_and_m)
        trip_duration(dfd_and_m)
        total_trip_duration(dfd_and_m)
        most_start_and_end_station(dfd_and_m)
        if filename != 'washington.csv': # Because washington dataset has no field 'Gender'
            gender_representation(dfd_and_m)
            user_bith_years(dfd_and_m)
        user_types(dfd_and_m)
        print('-' * 70)
        print('-' * 70)

    else:
        print('-' * 70)
        print('-' * 70)
        print('On {} \nNo filter applied'.format(filename))
        print('-' * 70)
        most_popular_hour(df)
        most_popular_day(df)
        most_popular_month(df)
        trip_duration(df)
        total_trip_duration(df)
        most_start_and_end_station(df)
        if filename != 'washington.csv': # Because washington dataset has no field 'Gender'
            gender_representation(df)
            user_bith_years(df)
        user_types(df)
        print('-' * 70)
        print('-' * 70)
    print('Operation processed in {} s'.format(time.time() - start_time))
    print('-' * 70)
    print('-' * 70)

def main():
    while True:
        show_start_menu()
        df = load_targeted_data(user_selected_dataset())
        # Convert to date time
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        # Creation of new columns for 'days' and 'months' for further processing based on "Date Time" column
        df['hours'] = df['Start Time'].dt.hour
        df['days'] = df['Start Time'].dt.day
        df['months'] = df['Start Time'].dt.month

        if ask_for_raw_data() == 'y':
            print('Loading raw data....')
            for i in show_raw_data(df):
                print(i)
        else:
            pass

        select_filtering_period()
        processing_core_operations(get_filter_input(), df)
        if one_more_time() == 'n':
            break

if __name__ == '__main__':
    main()