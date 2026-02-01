print("Enter total number of seconds: ")
total_seconds = int(input())

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(minutes, "minutes and", remaining_seconds, "remaining seconds")
