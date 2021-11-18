import sys

for line in sys.stdin:
  line = line.strip()
  yearMonthDay = line[15:23]
  temperature = line[87:92] 
  quality = line[93]

    try:
        temperature = int(temperature)
        quality = int(quality)
    except ValueError:
        continue

  if temperature == 9999 or quality == 0 or quality == 1 or quality == 4 or quality = 5 or quality = 9:
    return

  print ('%s\t%d' % (yearMonthDay, temperature))