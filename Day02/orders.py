from functools import reduce
orders = [
    {"id": "A", "amount": 120, "status": "paid"},
    {"id": "B", "amount": 0, "status": "paid"},
    {"id": "C", "amount": 200, "status": "unpaid"},
]

def select_paid_orders(orders):
    result = []
    for order in orders:
        if(order["status"] == "paid"):
            result.append(order)
    return sorted(result,key=lambda x:x["amount"],reverse=True)
    # key = lambda x 创建一个匿名函数 并且表明返回对象也是x


# 筛选已经支付的订单，按照订单的数量降序排序并输出
paid = select_paid_orders(orders)
# print(paid)

# 统计已经支付的订单id
# print([order["id"] for order in paid])

# 统计已经支付的订单总金额
# print(sum(order["amount"] for order in paid))

# 判断已经支付的订单id 是不是 ["A","B"]
assert [order["id"] for order in paid] == ["A","B"]

# 判断 计算已支付订单列表的方法 在传入空列表时，返回的结果也必须是空列表
assert select_paid_orders([]) == []

# 对于所有订单，按照支付状态进行分组，并进行统计。
group = {}
for order in orders:
    group.setdefault(order["status"],[]).append(order["id"])

# print(group)


# map
# print([order["amount"] for order in orders])
# result = []
# for order in orders:
#     result.append(order["amount"])
# print(result)

# filter
# print([
#     order
#     for order in orders
#     if(order["status"] == 'paid')
# ])

# reduce
# 求和
# print(sum(order["amount"] for order in orders))

# 分组
# group = {}
# for order in orders:
#     group.setdefault(order["status"],[]).append(order["id"])
# print(group)

# print(reduce(
#     lambda acc,order:acc+order["amount"],
#     orders,
#     0
# ))


# fruits = ['orangle','apple','pear','banana','kiwi','apple','banana']
# print(fruits.count('apple'))
# print(fruits.count('tangerine'))
# print(fruits.index('banana'))
# print(fruits.index('banana',4))
# print(fruits.reverse())
# print(fruits)
# fruits.append('grape')
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.pop()
# print(fruits)

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
