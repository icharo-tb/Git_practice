hour = int(input('Start Hour: '))
mins = int(input('Start Mins: '))
mins_to_add = int(input('Mins added: '))

print(f"\nStarting time: {hour}:{mins:02}\n")

for i in range(5):
    mins = mins + mins_to_add
    if mins >= 60:
        hour += 1
        mins -= 60
        print(f"{hour}:{mins:02}")
    elif mins < 60:
        mins = mins
        print(f"{hour}:{mins:02}")