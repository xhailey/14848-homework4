import sys

current_temperature = 0
curremt_date = None

for line in sys.stdin:
  line = line.strip()

  yearMonthDay, temperature = line.split('\t', 1)

  try:
    temperature = int(temperature)
  except ValueError:
        continue
  
  if current_date == current_date:
    if temperature > current_temperature:
      current_temperature = temperature
  else:
    if current_word:
      print ('%s\t%d' % (current_date, current_temperature))
    current_date = date
    current_temperature = temperature


if current_date == date:
    print ('%s\t%d' % (current_date, current_temperature))
