import datetime
from enlist.models.event import Event
from enlist.models.category import Category

e = Event.from_json({
    "title": "New Yearunknown/unknown",
    "startDate": "Jan 1, 2019",
    "endDate": "Jan 1, 2019",
    "categories": "/CMPB Portal Content/Calendar Taxonomy/Public Holiday",
})

print(e.start)
print(datetime.datetime(2019, 1, 1) == e.start)
