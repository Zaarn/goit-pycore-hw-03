import datetime


date = input("Enter a date (YYYY-MM-DD): ")
def get_days_from_today(date):
    try:  
        today = datetime.date.today()
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        delta = date_obj - today
        return print(delta.days)
    except ValueError:
        print("Invalid input. Please enter a date in the format YYYY-MM-DD.")
get_days_from_today(date)


