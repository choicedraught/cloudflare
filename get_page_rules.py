#!/usr/bin/env python

import pycurl
import cStringIO
import json 

APIKEY  = 'X-Auth-Key: ---MY CLOUDFLARE API KEY---'
USER    = 'X-Auth-Email: joe@bloggs.com'
ZONE    = '---MY CLOUDFLARE ZONE---' 
URL     = 'https://api.cloudflare.com/client/v4/zones/' + ZONE + '/pagerules?status=active&order=status&direction=desc&match=all'
CONTENT = 'Content-Type: application/json'

buffer = cStringIO.StringIO()

curlcmd = pycurl.Curl()
curlcmd.setopt(pycurl.URL, URL)
curlcmd.setopt(pycurl.HTTPHEADER, [USER, APIKEY, CONTENT])
curlcmd.setopt(curlcmd.WRITEFUNCTION, buffer.write)
curlcmd.perform()

result = buffer.getvalue()

parsed = json.loads(result)

print json.dumps(parsed, indent=4, sort_keys=True)



