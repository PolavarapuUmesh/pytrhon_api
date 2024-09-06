# import calendar
# year=int(input("Enter the year:"))
# month=int(input("Enter the month:"))
# if 1<= month <= 12:
#     month_calendar=calendar.monthcalendar(year,month)
#     print("\n",calendar.month_name[month],year)
#     print("Mon Tue Wed Thu Fri Sat Sun")
    
#     for week in month_calendar:
#         print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))
# else:
#     print("Invalid month number. Please enter a number between 1 and 12.")





import calendar
import holidays

year = int(input("Enter the year: "))
month = int(input("Enter the month number (1-12): "))

if 1 <= month <= 12:
    month_calendar = calendar.monthcalendar(year, month)
    
    country_code = 'IN'
    holiday_list = holidays.CountryHoliday(country_code, years=year)

    print("\n", calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    for week in month_calendar:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   " 
            else:
                date_str = f"{year}-{month:02d}-{day:02d}"
                day_str = f"{day:2d}"
                if date_str in holiday_list:
                    day_str += "*"
                    print(f"Holiday on {date_str}: {holiday_list[date_str]}")
                week_str += f"{day_str:3} "
        print(week_str)
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
