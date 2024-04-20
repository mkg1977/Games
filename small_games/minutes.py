user_input = int(input("Enter the numbers of minutes: "))


minutes_in_hour = 60
minutes_in_day = 60 * 24
minutes_in_month = 60 * 24 * 30
minutes_in_year = 60 * 24 * 365

def years_days(minutes):
    years = minutes // minutes_in_year
    remaining_minutes = minutes % minutes_in_year

    months = remaining_minutes // minutes_in_month
    rest_minutes = remaining_minutes % minutes_in_month

    days = rest_minutes // minutes_in_day
    final_rest_minutes = rest_minutes % minutes_in_day

    return years, months, days, final_rest_minutes

years, months, days, rest_minutes = years_days(user_input)
print(f"{user_input} = {years} yeras, {months} months, {days} days and {rest_minutes} minutes")

