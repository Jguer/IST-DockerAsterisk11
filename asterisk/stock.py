#!/usr/bin/python

import json
import re
import sys
import urllib.request


def checkresult(params):
    params = params.rstrip()
    if re.search('^200', params):
        result = re.search('result=(\d+)', params)
        if not result:
            sys.stderr.write("FAIL ('%s')\n" % params)
            sys.stderr.flush()
            return -1
        result = result.group(1)
        sys.stderr.write("PASS (%s)\n" % result)
        sys.stderr.flush()
        return result
    else:
        sys.stderr.write("FAIL (unexpected result '%s')\n" % params)
        sys.stderr.flush()
        return -2


def saynumber(params):
    sys.stderr.write("SAY NUMBER %s \"\"\n" % params)
    sys.stderr.flush()
    sys.stdout.write("SAY NUMBER %s \"\"\n" % params)
    sys.stdout.flush()
    result = sys.stdin.readline().strip()
    checkresult(result)


MESSAGE = {
    'instruments': [{
        "code": "PTING0200002",
        "exchangeCode": "XLIS",
        "codification": "ISIN"
    }]
}

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
