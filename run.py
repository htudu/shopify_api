import requests
import json
import datetime 

def fetch_past_data_status(start_day, end_day, status):

    today = datetime.datetime.now()
    range_a = today - datetime.deltatime(days = start_day)
    range_b = today - datetime.deltatime(days = end_day)
	date_range = "&created_at_min=2021-03-{}&created_at_max=2021-03-{}".format(str(range_b).split()[0], str(range_a).split()[0])
    status = "status={}".format(status) # open, closed, cancelled, any
    financial_status = "&financial_status=any"
    fulfillment = "&fulfillment_status=unfulfilled"
    base = "https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders/count.json?"
    url = base +  staus + date_range
	req = requests.get(url)
    resp = req.json()

    return resp["count"]

def fetch_past_data_financial_status(start_day, end_day, status):

    today = datetime.datetime.now()
    range_a = today - datetime.deltatime(days = start_day)
    range_b = today - datetime.deltatime(days = end_day)
	date_range = "&created_at_min=2021-03-{}&created_at_max=2021-03-{}".format(str(range_b).split()[0], str(range_a).split()[0])
    # status = "status={}".format(status)
    financial_status = "&financial_status={}".format(status) # pending, authorized, partially_paid, paid ,partially_refunded, refunded, voided
    fulfillment = "&fulfillment_status=unfulfilled"
    base = "https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders/count.json?"
    url = base +  financial_status + date_range
	req = requests.get(url)
    resp = req.json()

    return resp["count"]

def fetch_past_data_fulfillment(start_day, end_day, status):

    today = datetime.datetime.now()
    range_a = today - datetime.deltatime(days = start_day)
    range_b = today - datetime.deltatime(days = end_day)
	date_range = "&created_at_min=2021-03-{}&created_at_max=2021-03-{}".format(str(range_b).split()[0], str(range_a).split()[0])
    # status = "status={}".format(status)
    # financial_status = "&financial_status={}".format(status) # pending, authorized, partially_paid, paid ,partially_refunded, refunded, voided
    fulfillment = "&fulfillment_status={}".format(status) # shipped, partial, unshipped, any, unfulfilled
    base = "https://ff1a65e43a12ece5adab0fbf0ea4cb1d:68b7435f5c3cc1061ba6e1b8df717cee@gynoveda.myshopify.com/admin/api/2021-01/orders/count.json?"
    url = base +  financial_status + date_range
	req = requests.get(url)
    resp = req.json()

    return resp["count"]

records = []

days_range = ["1-10","11-30","31-60","61-90"]

for d in days_range:
    record = {}
    record["report"] = d
    record["from_date"] = ""
    record["to_date"] = ""
    s ,e = d.split("-")
    record["Booked"] = fetch_past_data_status(s,e,status = "any")
    record["Cancel"] = fetch_past_data_status(s,e,fulfillment="any" ,status = "cancelled")
    record["Net Orders"] = fetch_past_data_status(s,e,status = "cancelled")
    record["Unfulfill"] = fetch_past_data_status(s,e,fulfillment="unfulfilled" ,status = "open")
    record["Fulfill"] = fetch_past_data_status(s,e,fulfillment="fulfilled" ,status = "open")
    record["First-Time"] = fetch_past_data_status(s,e,customer_type="firsttime" ,status = "open,cancelled"))
    record["Repeat"] = fetch_past_data_status(s,e,customer_type="Repeat" ,status = "open,cancelled"))
    record["Prepid"] = fetch_past_data_status(s,e,financial="paid,partially_paid,refunded" ,status = "open,cancelled"))
    record["COD"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled")) #

    # record["AWB Created"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["AWB Cancel"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["AWB Net"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["AWB Prepaid"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["AWB COD"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Manifest"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Transit"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Deliverd"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Undeliver"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["RTO"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["RTO COD"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Deliver <=2D"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Deliver 3-5D"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Deliver 6-8D"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Deliver >=9"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Unfulfill >72h"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Manifest >72h"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Others"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["RTO-Transit"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["RTO-Deliver"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["RTO-Inward"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))
    # record["Lost"] = fetch_past_data_status(s,e,financial="other than paid,partially_paid,refunded" ,status = "open,cancelled"))

    records.append(record)





