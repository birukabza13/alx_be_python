from datetime import datetime, timedelta


def display_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    now = datetime.now()
    future_date = now + timedelta(days=days_to_add)
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")

