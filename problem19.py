# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

MONTH_LENGTHS = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def find_days_in_feb(year):
    if year % 4 == 0:
        return 29
    else:
        return 28


def add_week(date):
    new_year = date["year"]
    new_month = date["month"]
    new_day = date["day"] + 7
    
    max_days = find_days_in_feb(date["year"]) if date["month"] == 2 else MONTH_LENGTHS[date["month"]]
    if new_day > max_days:
        # increase the month
        new_day = new_day - max_days
        new_month += 1
        # if month changes to Jan, increase the year
        if new_month > 12:
            new_month = 1
            new_year += 1
    
    return {"year": new_year, "month": new_month, "day": new_day}


curr_date = {"year": 1901, "month": 1, "day": 6}
num_sundays = 0

while curr_date["year"] < 2001:
    if curr_date["day"] == 1:
        num_sundays += 1
    curr_date = add_week(curr_date)

print(num_sundays)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
