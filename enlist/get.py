import json
from datetime import datetime
from .models.event import Event
from .values import CURRENT_YEAR

# https://www.cmpb.gov.sg/web/wcm/connect/cmpb/cmpbContent/CMPBHome/before-ns/Enlistment-dates/enlistment-dates?srv=cmpnt&source=library&cmpntname=CMPBDesign/sections/page-2-BeforeNS/enlistment-dates/NAV%20Calendar%20Events%20Json"


def get(in_json=False):
  with open('./enlist/data/2020-dates.json') as f:
    data = json.load(f)

  event_list = []
  for event_dict in data["calendarEventList"][1:]:
    event = Event.from_json(event_dict)

    now = datetime.now()
    if event.start.date() > now.date():
      # only add to list if after today
      event_list.append(event.to_json() if in_json else event)



  return event_list
