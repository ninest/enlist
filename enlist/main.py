import json
from models.event import Event

# https://www.cmpb.gov.sg/web/wcm/connect/cmpb/cmpbContent/CMPBHome/before-ns/Enlistment-dates/enlistment-dates?srv=cmpnt&source=library&cmpntname=CMPBDesign/sections/page-2-BeforeNS/enlistment-dates/NAV%20Calendar%20Events%20Json"

with open('./enlist/data/2020-dates.json') as f:
  data = json.load(f)


event_list = []
for event_dict in data["calendarEventList"][1:]:
  event = Event.from_json(event_dict)
  event_list.append(event)
  print(event)
