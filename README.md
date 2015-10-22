# SORACOM SDK for Python

SORACOM provides sets of APIs to control their IoT platform service. This package will let you call SORACOM API from your python program.

## Status
- ~~Authentication~~
- ~~API wrapper~~
- Auto method population based on [Swagger format JSON](https://dev.soracom.io/jp/docs/swagger/soracom-api.ja.json)
- High level interface (resource based)

## Installation

```
$ pip install soracom 
```

## Usage

```
$ ipython
Python 2.7.9 (default, Feb 10 2015, 03:28:08)
Type "copyright", "credits" or "license" for more information.

IPython 3.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from soracom.client import * ; client = SoracomClient()

In [2]: client.auth()

In [3]: client.get("/subscribers")
Out[3]:
[{u'apn': u'soracom.io',
  u'createdAt': 1444969017790,
  u'createdTime': 1444969017790,
  u'expiredAt': None,
  u'expiryTime': None,
  u'groupId': None,
  u'imsi': u'440100000000000',
  u'ipAddress': u'10.000.000.000',
  u'lastModifiedAt': 1445504276137,
  u'lastModifiedTime': 1445504276137,
  u'moduleType': u'nano',
  u'msisdn': u'817000000000',
  u'operatorId': u'OP000000000000',
  u'plan': 1,
  u'sessionStatus': {u'dnsServers': None,
   u'imei': None,
   u'lastUpdatedAt': 1444980554719,
   u'location': None,
   u'online': False,
   u'ueIpAddress': None},
  u'speedClass': u's1.fast',
  u'status': u'inactive',
  u'tags': {},
  u'terminationEnabled': False,
  u'type': u's1.fast'}]
In [4]: client.post("/subscribers/440100000000000/update_speed_class",payload={'speedClass':'s1.minimum'})
Out[4]:
  {u'apn': u'soracom.io',
   u'createdAt': 1444969017790,
   u'createdTime': 1444969017790,
   u'expiredAt': None,
   u'expiryTime': None,
   u'groupId': None,
   u'imsi': u'440100000000000',
   u'ipAddress': u'10.000.000.000',
   u'lastModifiedAt': 1445505124834,
   u'lastModifiedTime': 1445505124834,
   u'moduleType': u'nano',
   u'msisdn': u'817000000000',
   u'operatorId': u'OP000000000000',
   u'plan': 1,
   u'sessionStatus': {u'dnsServers': None,
    u'imei': None,
    u'lastUpdatedAt': 1444980554719,
    u'location': None,
    u'online': False,
    u'ueIpAddress': None},
   u'speedClass': u's1.minimum',
   u'status': u'inactive',
   u'tags': {},
   u'terminationEnabled': False,
   u'type': u's1.minimum'}
```

## Special Thanks

Special thanks to [Toshiaki Enami](https://twitter.com/toshiakienami) for his [Qiita Post](http://qiita.com/ToshiakiEnami/items/8e0a6853d6017ac693ce)
