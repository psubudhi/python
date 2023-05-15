import datetime
import time


def find_second_highest(arr):
    # Initialize variables to store highest and second highest numbers
    highest = arr[0]
    second_highest = float('-inf')

    # Loop through the array to find the highest and second highest numbers
    for num in arr:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num

    # Return the second highest number
    return second_highest
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(current_time)
arr = [3, 1, 4, 2, 5]
print(find_second_highest(arr))
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(current_time)

arr = [3, 1, 4, 2, 5]
arr.sort()
print(arr[(len(arr)-2)])
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(current_time)
current_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
print(current_timestamp)


