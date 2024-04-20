def min_to_day_year(minutes):

    day_min = 60 * 24
    year_min = 60 * 24 * 365

    days = minutes // day_min
    years = minutes // year_min
    
    return days, years
minutes_input = int(input("Enter the number of minutes: "))
days_output, years_output = min_to_day_year(minutes_input)
print(f"{minutes_input} minutes is approximately {days_output} days and {years_output} years.")