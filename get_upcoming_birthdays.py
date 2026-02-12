import datetime



def get_upcoming_birthdays(users):
    today = datetime.date.today()
    upcoming_birthdays = []
    
    for user in users:
        
        birthday_date = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        
        if birthday_this_year <= today + datetime.timedelta(days=7) and birthday_this_year >= today and not birthday_this_year.weekday() in [5, 6]:
            birthday_string = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_string})
        elif birthday_this_year <= today + datetime.timedelta(days=7) and birthday_this_year >= today and birthday_this_year.weekday() in [5, 6]:
            birthday_this_year += datetime.timedelta(days=(7 - birthday_this_year.weekday()))
            birthday_string = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_string})
    
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.02.15"},
    {"name": "Jane Smith", "birthday": "1990.02.18"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
