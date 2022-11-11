# Docker-Stocks
Use docker-compose to set up APIs for CRUDing stock indices with MySQL.

Fetch indices of W for current 3 days:
```
$ curl 127.0.0.1:8000/indices/w/3
[
  {
    "stock_id": 25671,
    "date": "2022-10-27",
    "index": 35.24
  },
  {
    "stock_id": 25671,
    "date": "2022-10-26",
    "index": 35.11
  },
  {
    "stock_id": 25671,
    "date": "2022-10-25",
    "index": 34.52
  }
]
```
[![](https://i.imgur.com/IbQypPg.png)]()