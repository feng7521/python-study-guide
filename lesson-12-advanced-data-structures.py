"""
============================================================
第 12 课：数据结构进阶
============================================================
内容：列表推导式、栈、队列、字典推导式、集合推导式
"""
from collections import deque

print('=' * 50)
print('第 12 课：数据结构进阶')
print('=' * 50)

# ========== 12.1 列表推导式 ==========
print('\n--- 12.1 列表推导式 ---')

# 传统写法
squares = []
for x in range(10):
    squares.append(x ** 2)
print(f'传统: {squares}')

# 列表推导式：一行搞定
squares2 = [x**2 for x in range(10)]
print(f'推导: {squares2}')

# 带条件的推导
evens = [x for x in range(20) if x % 2 == 0]
print(f'偶数: {evens}')

# 嵌套推导（矩阵 / 乘法表）
matrix = [[i*j for j in range(1, 5)] for i in range(1, 4)]
print('矩阵:')
for row in matrix:
    print(f'  {row}')

# ========== 12.2 字典推导式 & 集合推导式 ==========
print('\n--- 12.2 字典推导式 & 集合推导式 ---')

# 字典推导式
squares_dict = {x: x**2 for x in range(6)}
print(f'字典: {squares_dict}')

# 集合推导式
unique_lengths = {len(word) for word in ['apple', 'banana', 'cat', 'dog', 'egg']}
print(f'集合(去重): {unique_lengths}')

# ========== 12.3 栈 Stack ==========
print('\n--- 12.3 栈 (后进先出 LIFO) ---')
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(f'入栈后: {stack}')
print(f'出栈: {stack.pop()} -> {stack}')
print(f'出栈: {stack.pop()} -> {stack}')

# ========== 12.4 队列 Queue ==========
print('\n--- 12.4 队列 (先进先出 FIFO) ---')
queue = deque()
queue.append('a')
queue.append('b')
queue.append('c')
print(f'入队后: {list(queue)}')
print(f'出队: {queue.popleft()} -> {list(queue)}')
print(f'出队: {queue.popleft()} -> {list(queue)}')

# ========== 12.5 遍历技巧 ==========
print('\n--- 12.5 遍历技巧 ---')
fruits = ['apple', 'banana', 'orange']

# enumerate: 同时获取索引和值
for i, fruit in enumerate(fruits):
    print(f'  [{i}] {fruit}')

# zip: 并行遍历多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print('zip 并行遍历:')
for name, age in zip(names, ages):
    print(f'  {name}: {age}')

# reversed: 反向遍历
print('reversed:', list(reversed(fruits)))

# sorted: 排序后遍历
print('sorted:', sorted(fruits))


print('\n\n=== 数据结构总结 ===')
print('列表推导 [x for x in seq if cond] -> 一行创建列表')
print('栈        list.append() + pop()   -> 后进先出')
print('队列      deque + popleft()       -> 先进先出')
print('enumerate -> 同时拿索引和值')
print('zip       -> 并行遍历多个序列')
