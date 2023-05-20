import requests

res = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001')
res_json = res.json()
results = res_json['results'][0]
address = results['address1'] + results['address2'] + results['address3']
print(address)