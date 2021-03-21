import requests
import json

# host_url = "https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders.json"

# res_code = requests.get("https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders.json?status=any&limit=250&created_at_min=2021-03-11T00:00:00-04:00&created_at_max=2021-03-15T23:59:00-04:00&fulfillment_status:partial")
res_code = requests.get("https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders.json?status=any&created_at_min = 2021-03-10&created_at_max = 2021-03-20")

# print(res_code.json())

# res = res_code.json()
# print(len(res["orders"]))

res = (json.dumps(res_code.json(),indent = 4))
# print(res)

# for itm in res['orders']:
# 	print("-->> ",itm["created_at"])

#  ----------------count order ---------------------------

count_per_day = requests.get("https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders/count.json?status=any&created_at_min=2021-03-10&created_at_max=2021-03-20")

# res = json.dumps(count_per_day)
print(count_per_day.json())

for i in range(1,11):
	date = "&created_at_min=2021-03-{}&created_at_max=2021-03-{}".format(20-i-1, 20-i)
	url = "https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders/count.json?status=open"
	url = url + date
	req = requests.get(url)
	print(date)


	print("Day - {} | resp - {}".format(i,req.json()))
