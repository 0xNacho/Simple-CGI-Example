import json
print "Content-type: application/json"
print 
response={'p1':0,'p2':'1'}
print(json.JSONEncoder().encode(response))