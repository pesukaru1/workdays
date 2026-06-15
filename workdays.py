#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 1:
    print("Добавьте в качестве аргумента интересующий вас график. Например: 4/2")
elif not re.fullmatch(r'\d+/\d+', sys.argv[1]):
    print("График должен быть в формате nn/nn, где n - это цифра")
else:
    shedule = re.search(r'(\d+)/(\d+)',sys.argv[1])
    month = 30
    workdays = int(shedule.group(1))
    dayoffs = int(shedule.group(2))
    workweeks = int( month / ( workdays + dayoffs ))
    workdaystotal = workdays * workweeks
    dayoffstotal = dayoffs * workweeks
    print(f"Количество рабочих дней: {workdaystotal}\nКоличество выходных: {dayoffstotal}")

