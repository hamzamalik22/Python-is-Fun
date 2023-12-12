import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'))
print("Hours :",hours)
minutes = int(time.strftime('%M'))
print("Minutes :",minutes)
seconds =int(time.strftime('%S'))
print("Seconds :",seconds)

if(hours>=5 and hours<=10):
  print("Good morning")
elif(hours>10 and hours<=16):
  print("Good afternoon")
elif(hours>16 and hours<=19):
  print("Good Evening")
else:
  print("Good Night\nHave sweet dreams")
  