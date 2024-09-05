import datetime as dt

# prompt user input, ask for what feature that they want


def countdown_full_date(input_date: str):
    '''
    Return how many days between input date and current date. Could be negative if input date is in the past

    Parameters:
        input_date (str): yyyy/mm/dd
            example input: '2025/01/01'

    Returns:
        countdown in days
            example output: '117 days'
    '''
    try:
        year, month, day = (int(x) for x in input_date.split('/'))
    except Exception:
        return 'Please enter a date in yyyy/mm/dd format.'

    try:
        future_date = dt.datetime(year, month, day)
    except Exception as e:
        return e

    curr_date = dt.datetime.now()

    return str((future_date - curr_date).days) + ' days'


u_input = input('enter a date (yyyy/mm/dd): ')
print(countdown_full_date(u_input))
