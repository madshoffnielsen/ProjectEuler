def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def count_sundays_on_first_of_month(start_year, end_year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = 1  # 1 Jan 1900 was a Monday, so 1 Jan 1901 is a Tuesday (day_of_week = 2)
    sundays_count = 0

    for year in range(1900, end_year + 1):
        for month in range(12):
            if year >= start_year and day_of_week == 0:
                sundays_count += 1
            if month == 1 and is_leap_year(year):
                day_of_week = (day_of_week + 29) % 7
            else:
                day_of_week = (day_of_week + days_in_month[month]) % 7

    return sundays_count

if __name__ == "__main__":
    start_year = 1901
    end_year = 2000
    result = count_sundays_on_first_of_month(start_year, end_year)
    print(f"The number of Sundays that fell on the first of the month during the twentieth century is {result}")