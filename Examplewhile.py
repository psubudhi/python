import sys
import datetime
def speed(distance, time):
    return distance / time


print(speed(5, 300))

year_of_birth=int(sys.argv[1])
current_of_birth=int(datetime.date.today().year)

print("Year of persion:",(current_of_birth-year_of_birth))
