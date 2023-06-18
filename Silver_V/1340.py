# 연도 진행바

date_list = input().split(" ")

# print(date_list)

month_dict = {"January": 1, "February": 2, "March": 3, "April" : 4, 
              "May" : 5, "June" : 6, "July" : 7, "August" : 8, 
              "September" : 9, "October" : 10, "November" : 11, "December" : 12}

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = month_dict[date_list[0]]
day = int(date_list[1].replace(",", ""))
year = int(date_list[2])
hour = int(date_list[3][0:2])
minute = int(date_list[3][3:])

total_minutes = 365 * 24 * 60
year_count = 0

# 윤년 파악
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0): 
    total_minutes = 366 * 24 * 60
    year_count = 1

# 윤년이고 2월이 지난 시점
if year_count == 1 and month > 2:
    curr_minutes = (sum(days_per_month[:month-1])+day) * 24 * 60 + hour * 60 + minute

# 윤년이 아닐 때
else:
    curr_minutes = (sum(days_per_month[:month-1])-1+day) * 24 * 60 + hour * 60 + minute

if curr_minutes < 0:
    curr_minutes = 0

# print(sum(days_per_month[:month-1])-1)
# print("year: ", year)
# print("month: ", month)
# print("day: ", day)
# print("hour: ", hour)
# print("minute: ", minute)

# print("curr_minutes: ", curr_minutes)
# print("total_minutes: ", total_minutes)
print(curr_minutes / total_minutes * 100)
    


