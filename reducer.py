import sys

current_temperature = 0
current_date = None

for line in sys.stdin:
  line = line.strip()

  date, temperature = line.split('\t', 1)

  try:
    temperature = int(temperature)
  except ValueError:
        continue
  
  if current_date == date:
    if temperature > current_temperature:
      current_temperature = temperature
  else:
    if current_date:
      print ('%s\t%d' % (current_date, current_temperature))
    current_date = date
    current_temperature = temperature


if current_date == date:
    print ('%s\t%d' % (current_date, current_temperature))
