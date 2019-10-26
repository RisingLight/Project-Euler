current_day = 0
current_month = 0
current_year = 1901

end_date = [31,12,2000]
week_index = 1

thirty_one_months = [0,2,4,6,7,9,11]
sunday_count = 0

def check_leap_year(year):
    return True if year % 4 == 0 and year % 400 != 0 else False

while [current_day+1,current_month+1,current_year] != end_date:
    if week_index == 6 and current_day == 0:
        sunday_count+=1
    if current_month == 1:
        feb_days = 28 if check_leap_year(current_year) else 27
        if current_day == feb_days:
            current_day = 0
            current_month = (current_month+1)%12
        else:
            current_day+=1
    elif current_month in thirty_one_months:
        if current_day == 30:
            current_day = 0
            if current_month == 11:
                current_month = 0
                current_year += 1
            else:
                current_month +=1
        else:
            current_day+=1
    else:
        if current_day == 29:
            current_day = 0
            current_month = (current_month+1)%12
        else:
            current_day+=1
    week_index=(week_index+1)%7
print(sunday_count)
