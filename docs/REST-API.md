# REST API USAGE

## API ROOT
localhost:8000/api

## API AUTH ROOT
localhost:8000/auth

## Side load relationship
load related data along side. I.E. 

1. load default date: `(GET) /api/instruments/10`
```json
{
    "instrument": {
        "status": "R",
        "reservation_time_unit": 15,
        "description": "可支持偏振、TRF、FRET等功能",
        "links": {
            "reservation_type": "reservation_type/"
        },
        "image": "http://172.16.15.225:8000/media/uploads/%E6%B5%81%E5%BC%8F%E7%BB%86%E8%83%9E%E4%BB%AA_WO8otBe.jpg",
        "accessories": "放置96/48/24/6孔板的托盘",
        "reservation_type": [
            1
        ],
        "reservation_end_time": "20:00:00",
        "id": 10,
        "sci_discount": true,
        "charge_type": 2,
        "name": "全波长酶标仪",
        "admin": 7,
        "application": "分子/细胞各类检测功能",
        "location": "N202",
        "reservation_start_time": "08:00:00",
        "department": 1,
        "model": "Varioskan Flash",
        "manufacturer": 5
    }
}
```
2. load admin information alongside: `(GET) /api/instruments/10/?include[]=admin.*`
```json
{
    "instrument": {
        "status": "R",
        "reservation_time_unit": 15,
        "description": "可支持偏振、TRF、FRET等功能",
        "links": {
            "reservation_type": "reservation_type/"
        },
        "image": "http://172.16.15.225:8000/media/uploads/%E6%B5%81%E5%BC%8F%E7%BB%86%E8%83%9E%E4%BB%AA_WO8otBe.jpg",
        "accessories": "放置96/48/24/6孔板的托盘",
        "reservation_type": [
            1
        ],
        "reservation_end_time": "20:00:00",
        "id": 10,
        "sci_discount": true,
        "charge_type": 2,
        "name": "全波长酶标仪",
        "admin": 7,
        "application": "分子/细胞各类检测功能",
        "location": "N202",
        "reservation_start_time": "08:00:00",
        "department": 1,
        "model": "Varioskan Flash",
        "manufacturer": 5
    },
    "users": [
        {
            "username": "limi",
            "first_name": "咪",
            "last_name": "李",
            "is_superuser": false,
            "is_active": true,
            "id": 7,
            "phone": "111111",
            "is_staff": false,
            "last_login": null,
            "groups": [],
            "birth_date": null,
            "user_permissions": [],
            "password": "pbkdf2_sha256$36000$9izMGBeZUcNl$+jK2KnkGVKZo+aZF5dp+1TzPuInZlo8YdRF2+uzp2Tw=",
            "email": "x@x.com",
            "date_joined": "2017-07-11T06:46:00"
        }
    ]
}
```

## Filtering
1. Filter by string/number (exact match)
`(GET) /api/users/?filter{username}=admin`
```json
{
    "users": [
        {
            "username": "admin",
            "first_name": "管理员",
            "last_name": "",
            "is_superuser": true,
            "is_active": true,
            "id": 1,
            "phone": null,
            "is_staff": true,
            "last_login": "2017-07-19T07:51:47.655322",
            "groups": [],
            "birth_date": null,
            "user_permissions": [],
            "password": "pbkdf2_sha256$36000$9izMGBeZUcNl$+jK2KnkGVKZo+aZF5dp+1TzPuInZlo8YdRF2+uzp2Tw=",
            "email": "admin@tjab.org",
            "date_joined": "2017-07-10T02:11:00"
        }
    ],
    "meta": {
        "total_results": 1,
        "per_page": 10,
        "total_pages": 1,
        "page": 1
    }
}
```
2. Filter by relationship data, get all reservation of user zhonghua (user.id=12) `(GET) /api/reservations/?include[]=user.*&filter{user.id}=12`

## Ordering
Ordering all instrument list by name
`(GET) /api/instruments/?sort[]=name`
```json
{
    "instruments": [
        {
            "status": "R",
            "reservation_time_unit": 15,
            "description": "可支持偏振、TRF、FRET等功能",
            "links": {
                "reservation_type": "reservation_type/"
            },
            "image": "http://172.16.15.225:8000/media/uploads/%E6%B5%81%E5%BC%8F%E7%BB%86%E8%83%9E%E4%BB%AA_WO8otBe.jpg",
            "accessories": "放置96/48/24/6孔板的托盘",
            "reservation_type": [
                1
            ],
            "reservation_end_time": "20:00:00",
            "id": 10,
            "sci_discount": true,
            "charge_type": 2,
            "name": "全波长酶标仪",
            "admin": 7,
            "application": "分子/细胞各类检测功能",
            "location": "N202",
            "reservation_start_time": "08:00:00",
            "department": 1,
            "model": "Varioskan Flash",
            "manufacturer": 5
        },
        ......
    ],
    "meta": {
    ......
    }
}
```

## Add new an entity
1. add new reservation `(POST) /api/reservations/` with body 
```json
   {
        "user": 12,
        "instrument": 5,
        "start_time": "2017-07-31T16:17:00",
        "end_time": "2017-07-31T17:15:00"
    }
```
2. update a reservation `(PUT) /api/reservations/5/` with body
```json
{
        "user": 12,
        "instrument": 5,
        "start_time": "2017-07-31T16:18:00",
        "end_time": "2017-07-31T17:15:00",
        "id": 5
    }
```
3. partial update end time `(PATCH) /api/reservations/5/` with body
```json
{
        "end_time": "2017-07-31T17:19:00",
        "id": 5
    }
```
4. delete a reservation `(delete) /api/reservations/5/`

For *POST*, *PUT*, *PATCH* and *DELETE* method user token should be added to HTTP header:
 ```json
{
        "Authorization": "Token user_token_string"
}
```
