elif birthday_this_year <= today + datetime.timedelta(days=7) and birthday_this_year >= today and birthday_this_year.weekday() in [5, 6]:
            birthday_this_year += datetime.timedelta(days=(7 - birthday_this_year.weekday()))
            birthday_string = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_string})