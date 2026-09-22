sting_number = '1h 45m,360s,25m,30m 120s,2h 60s'
minutes = 0
list_numbers = sting_number.split(',')

for number in list_numbers:
    list_number = number.split()
    for num in list_number:
        if 'h' in num:
            minutes += int(num.replace('h', '')) * 60
        elif 'm' in num:
            minutes += int(num.replace('m', ''))
        elif 's' in num:
            minutes += int(num.replace('s', '')) // 60

print(minutes)