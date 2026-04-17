import json
import urllib.request

url = 'http://127.0.0.1:8000/api/medicines'
data = json.dumps({'name': 'TestMed', 'stock_quantity': 10, 'unit_price': 12.5}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print('STATUS', resp.status)
        print(resp.read().decode('utf-8'))
except Exception as e:
    print('ERROR', type(e).__name__, e)
