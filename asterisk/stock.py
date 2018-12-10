#!/usr/bin/python

import sys
import re
import time
import random
import json
import urllib.request

MESSAGE = {
    'instruments': [{
        "code": "PTING0200002",
        "exchangeCode": "XLIS",
        "codification": "ISIN"
    }]
}

def saynumber (params):
   sys.stderr.write("SAY NUMBER %s \"\"\n" % params)
   sys.stderr.flush()
   sys.stdout.write("SAY NUMBER %s \"\"\n" % params)
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   checkresult(result)

STOCK_URL = "http://gateway.euronext.com/api/ticker/instrumentDetail"
req = urllib.request.Request(STOCK_URL)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(MESSAGE)
jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
r = urllib.request.urlopen(req, jsondataasbytes)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
# print(data)
# print(data["results"][0]["lastPrice"])
saynumber(data["results"][0]["lastPrice"])
