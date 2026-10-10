orders = [{"id": "o1", "amount_cents": 1000},
          {"id": "o2", "amount_cents": 500}]
seen = {}
seen[orders[0]["id"]] = orders[0]
known_ids = {"o1", "o1", "o2"}
orders.append({"id":"o3","amount_cents":700})
seen[orders[2]["id"]] = orders[2]
assert len(orders) == 3
print(seen["o2"]["amount_cents"] == 700)
print(type(orders).__name__,type(orders[0]).__name,type(orders[0]["id"]).__name__)
print("o2" in seen)
# print("o1" in seen, "o2" in seen)
# print(seen["o1"]["amount_cents"])
# print(len(known_ids), "o2" in known_ids)
# print(type({}).__name__, type(set()).__name__)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = []

for i in range(3):
    row = []
    for item in matrix:
        # print(item[i])
        row.append(item[i])

    result.append(row)

# print(result)

a = {1,2,3}
b = set([1,2,2,3])
c = set("hello")
print(b)
print(2 in a)
print(c)


# 1. list 可重复且有顺序的列表存储
#  1.1 操作
#     1.1.1 append vs extends
#          append(x) x是作为一个整体被添加到列表末尾
#          extends(xs)  遍历xs，把其中的元素依次添加到列表末尾
#     1.1.2 insert(i,x) 在i位置前插入x
#     1.1.3 remove vs pop
#       remove(x) 删除第一个x，没有找到报错，返回值None
#       pop(i)  根据元素的下标i删除，返回被删除的元素
#       pop() == pop(-1) 不传递参数就默认删除最后一个
#     1.1.4 clear 清空
#     1.1.5 index(x,start,stop) 在指定区间找首次出现位置
#     1.1.6 count(x) 计数，没有则返回0
#     1.1.7 sort(list,key=...,reverse=...)
#     1.1.8 reverse() 原地反转当前顺序
#     1.1.9 copy()  浅拷贝
#         只pop返回当前取的项，其他返回None
#     1.1.10 x in s 判断成员
#  1.2 赋值与拷贝
#         拷贝的三种方法
#         1. 直接使用 =  不会创建新外层，内部对象没变
#         2. 使用copy()方法
#            创建新外层，内容对象没变
#         3. 使用deepcopy()方法
#            创建新外层，创建内部对象

#   
# 2. dict 按插入顺序的键值对且键唯一、键必须可哈希、重复键会新值覆盖旧值
#  2.1 创建 键名要加上双引号或者单引号
#      字面量 { "A":1 }
#      键值对序列 dict(["A",1])
#      关键字参数 dict(A=1)
#      字典推导式 {k:v for k,v in pairs } 
#           pairs = [("A"，1)]
#           d4 = {k:v for k,v in pairs }
#  2.2 操作
#      访问
#         直接访问
#           d[k] 找不到抛出错误KeyError
#         安全访问
#            d.get(k) 找不到返回None
#            指定默认值 d.get(k,default)
#      删除 del d[k]
#      判断键是否存在    k in d
#       
# 3. 集合set 没有重复的集合(通过hash判断值是否相等，做去重)， 适合查找元素是否在集合里面
#  3.1 vs JS set
#    JS Set 比较的是对象引用是否相同，可以存对象和数组
#    Python Set 比较的是hash值是否相等，不可以存储对象和数组(因为对象、数组的值可以改变=>对应哈希值不稳定)
#  3.2 创建 - 使用花括号{}创建非空集合，或通过set()将可迭代对象(如列表、元组、字符串等)转为集合。
#    b = {1,2,3} 花括号非空集合
#    b = {} 空集合
#    b = set([1,2,3,4]) 可迭代对象创建
#    b = set('hello') 字符串转集合 会去重但不能保证顺序
# 4. hash 哈希是为一个对象计算出一个用于快速查找的整数值  dict和set是通过哈希值来快速查找对象
#   4.1 能提供哈希查找使用的哈希值  - 通过hash()可以为对象计算得到一个证书
#   4.2 在对象生存期内稳定的哈希值  - 同一个对象，同一个进程里，在存续期间hash值保持不变
#   4.3 相等对象的哈希值一致       - 若 obj1 = obj2,则 hash(obj1) == hash(obj2),但反之则不成立 若 hash(obj1) = hash(obj2),不能证明obj1 = obj2
#   vs ==  hash是快速定位数据的线索，而 == 才负责确认对象是否相等
# 5. tuple 元组 创建后不能修改元素的有序集合 关键符号是,不是圆括号
#   b = (1,2)    可哈希
#   c = (1,[1,2]) 不可以哈希 => [1,2]可以被改变

# 6.推导式 [输出表达式 for 元素 in 来源 if 条件]
#  6.1 多层嵌套for/if，与普通嵌套for、if 从外到内的书写顺序一致





# TODO: 能把简单推导式展开为for
