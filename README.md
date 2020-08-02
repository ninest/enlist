# Enlist
> An API to get enlistment dates and public holidays

## 🤔 Usage

The endpoint [ns-enlist.vercel.app/api](https://ns-enlist.vercel.app/api) returns the current year and a list of events (Public holidays or BMT enlistments) that are not yet over.

#### Example

```json
{
  "year":2020,
  "events_list":[
    {
      "title":"National Day",
      "start":1596931200000,
      "category":"Public Holiday"
    },
    {
      "title":"National Day observed",
      "start":1597017600000,
      "category":"Public Holiday"
    },
    {
      "title":"Deepavali",
      "start":1605312000000,
      "category":"Public Holiday"
    },
    {
      "title":"Christmas Day",
      "start":1608854400000,
      "category":"Public Holiday"
    },
    
    ...

  ]
}
```

## 📁 JSON file
If you do not want to rely on the API, you can download `2020-dates.json`. It is used in [ninest/NSR](https://github.com/ninest/nsr) for the [Dates page](https://nsr.now.sh/dates).

## 📜 Licence
MIT

All data about public holidays and enlistment dates are from [mom.gov.sg](https://www.mom.gov.sg/employment-practices/public-holidays) or [cmpb.gov.sg](https://www.cmpb.gov.sg/web/portal/cmpb/home/before-ns/enlistment-dates).