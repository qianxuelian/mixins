import copy
# orders = [{"id": "o1", "amount_cents": 1000}]
# alias = orders 
# alias = orders 让两个名字指向了同一个列表，不会创建新列表
# shallow = orders.copy()
# copy() 创建了新列表
# snapshot = copy.deepcopy(orders)
# print(alias is orders, shallow is orders)
# print(shallow[0] is orders[0], snapshot[0] is orders[0])
# shallow[0]["amount_cents"] = 2000
# print(orders[0]["amount_cents"], snapshot[0]["amount_cents"])
# shallow.append({"id": "o2", "amount_cents": 500})
# print(len(orders), len(shallow))

raw = {"id": " o1 ", "customer_id": " A ", "amount_cents": 1000, "status": "paid"}
normalized = {
    "id": raw["id"].strip(),
    "customer_id": raw["customer_id"].strip(),
    "amount_cents": raw["amount_cents"],
    "status": raw["status"],
}
# print(repr(raw["id"]), repr(normalized["id"]))
# print(raw is normalized)
# assert raw["id"] == " o1 "
# assert normalized["id"] == "o1"
# repr把空格和引号显示出来 
# strip() 去除多余的空格
# strip(sign) 通过指定sign来指定要去除的字符
# lstrip() 去除左边多余的空格
# rstrip() 去除右边多余的空格

# left = {"A":1}
# right = {"B":1}
# alias = left
# alias["C"] = 3
# print(left)
# print(alias)

import copy
order = {"id": "o1", "tags": ["new"]}
cloned = copy.deepcopy(order)
# print(cloned is order)
# print(cloned["tags"] is order["tags"])
# print(cloned["id"] is order["id"])
cloned["tags"].append("paid")
cloned["id"] = "o2"
# cloned["id"]可以重新赋值一个新的字符串，但是不能在原有的字符串修改
# print(cloned["id"] is order["id"])
# print(order)
# print(cloned)

# import copy
# order = {"id": "o1", "tags": ["new"]}
# cloned = copy.deepcopy(order)
# print(cloned is order) 
# print(cloned["tags"] is order["tags"]) 
# print(cloned["id"] is order["id"]) 
# cloned["tags"].append("paid")
# cloned["id"] = "o2"
# print(order) 
# print(cloned)


# import copy
# a = []
# a.append(a)
# # 没有复制一份列表
# print(a) # [[...]]
# print(a[0] is a) #True
# b = copy.deepcopy(a) 
# print(b is a) # False
# print(b[0] is b, b[0] is a) # True False


import copy
shared_tags = ["new"]
orders = [{"tags": shared_tags}, {"tags": shared_tags}]
cloned = copy.deepcopy(orders)
# print(orders[0]["tags"] is orders[1]["tags"]) # True
# 原数据中的两条订单，共享同一个标签列表
# print(cloned[0]["tags"] is cloned[1]["tags"]) # True 
# 副本中的两条订单，共享同一个标签列表
# print(orders[0]["tags"] is shared_tags) # True
# print(cloned[0]["tags"] is shared_tags) # False
# 副本共享出来的已经新列表，不是原来的列表
cloned[0]["tags"].append("paid")
# print(cloned[1]["tags"]) # ["new","paid"]
# print(shared_tags) # ["new"]

import copy
def calculate():
    return 1
class Order:
    pass

# print(copy.copy(calculate) is calculate, copy.deepcopy(calculate) is calculate) # False  False
# print(copy.copy(Order) is Order, copy.deepcopy(Order) is Order) # False False
# instance = Order()
# print(copy.copy(instance) is instance) # False

# a = [["new"]]
# d = {"tags": a[0]}
# s = {"A", "B"}
# ac = a.copy()
# dc = d.copy()
# sc = s.copy()
# print(ac is a, ac[0] is a[0]) # False True
# print(dc is d, dc["tags"] is d["tags"]) # False True
# print(sc is s, sc == s) # False True 比较是的元素是否相等


import copy
class OrderList(list):
    pass
orders = OrderList([{"id": "o1"}])
print(type(orders).__name__)
print(type(orders.copy()).__name__)
print(type(orders[:]).__name__)
print(type(copy.copy(orders)).__name__)
