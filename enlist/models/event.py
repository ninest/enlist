import datetime

from .category import Category
from .event_types import BMT


class Event:
  def __init__(self, title, start, end, category):
    self.title = title
    self.start = start
    self.end = end
    self.category = category

  @staticmethod
  def from_json(json_dict):

    # remove unknown/unknown from title
    title = json_dict["title"].split("unknown/unknown")[0]

    # parse dates
    date_format = "%b %d, %Y"
    try: start = datetime.datetime.strptime(json_dict["startDate"], date_format)
    except: start = None

    try: end = datetime.datetime.strptime(json_dict["endDate"], date_format)
    except: end = None

    # category is can be BMT or public holiday
    category = json_dict["categories"]
    if "BMT" in category:
      category = Category.BMT
    else:
      category = Category.PUBLIC_HOLIDAY

    return Event(title=title, start=start, end=end, category=category,)

  def __str__(self):
    if self.start == self.end:
      return f"<{self.title} - {self.category} - {self.start}>"
    else:
      return f"<{self.title} - {self.category} - {self.start} to {self.end} >"


e = Event.from_json({
    "title": "New Yearunknown/unknown",
    "startDate": "Jan 1, 2019",
    "endDate": "Jan 1, 2019",
    "categories": "/CMPB Portal Content/Calendar Taxonomy/Public Holiday",
})

print(e)
