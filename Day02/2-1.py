orders = [
    {"id": "o1", "amount_cents": 1000},
    {"id": "o2", "amount_cents": 500},
]
first = orders[0]
order_id = first["id"]
print(type(orders).__name__, type(first).__name__, type(order_id).__name__)
print(order_id, len(orders))
print("o1" in orders, "id" in first)
print({"id": "o1", "amount_cents": 1000} in orders)

# type(变量).__name__ 获得对应类型名称
