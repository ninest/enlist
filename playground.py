import datetime
from enlist.get import get

event_list = get()

for e in event_list:
  print(e)