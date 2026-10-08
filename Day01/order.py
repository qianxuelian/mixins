def summarize_order(orders,min_amount):
    total_amount = 0
    order_ids = []

    for order in orders:
        if(order["status"] == 'paid' and order["amount"] >= min_amount):
            total_amount += order["amount"]
            order_ids.append(order["id"])

    return {
        "count":len(order_ids),
        "total_amount": total_amount,
        "order_ids":order_ids
    }

sample_orders = [
    {"id":"A001","amount":120,"status":"paid"},
    {"id":"A002","amount":80,"status":"unpaid"},
    {"id":"A003","amount":200,"status":"paid"},
]

result = summarize_order(sample_orders,150)
print(result)
    