import sys

for line in sys.stdin:
  line = line.strip()
  yearMonthDay = line[15:23]
  temperature = line[87:92] 
  quality = line[92]
  
  try:
    temperature = int(temperature)
    quality = int(quality)
  except ValueError:
    continue

  if temperature == 9999:
    continue
  
  if quality != 0 and quality != 1 and quality != 4 and quality != 5 and quality != 9:
    continue

  print ('%s\t%d' % (yearMonthDay, temperature))