"""
============================================================
第 2 课 & 第 3 课：数据类型（数字 + 四种容器）
============================================================
内容：int/float、字符串、列表、元组、字典、集合
"""

print('=' * 50)
print('第 2 课：数字类型与字符串')
print('=' * 50)

# ========== 2.1 数字类型 ==========
print('\n--- 2.1 数字运算 ---')
a, b = 17, 3
print(f'加法:  {a} + {b} = {a + b}')
print(f'减法:  {a} - {b} = {a - b}')
print(f'乘法:  {a} * {b} = {a * b}')
print(f'除法:  {a} / {b} = {a / b}')       # 普通除法，结果是小数
print(f'整除:  {a} // {b} = {a // b}')      # 地板除，只取整数部分
print(f'取余:  {a} % {b} = {a % b}')         # 取余数
print(f'乘方:  2 ** 10 = {2 ** 10}')         # 2的10次方

print('\n类型转换:')
print(f'  float(5) = {float(5)}')
print(f'  int(3.99) = {int(3.99)}   # 直接截断，不是四舍五入')
print(f'  int("123") + 1 = {int("123") + 1}')

# ========== 2.2 字符串 ==========
print('\n--- 2.2 字符串 ---')
s = 'Hello Python'

# 索引：取单个字符（从0开始数！）
print(f'第1个字符 s[0]:  {s[0]}')
print(f'第7个字符 s[6]:  {s[6]}')
print(f'最后一个 s[-1]:  {s[-1]}')           # 负数索引从末尾开始

# 切片：取一段 [开始:结束] 包含开始，不包含结束
print(f'前5个 s[0:5]:    {s[0:5]}')
print(f'6到末尾 s[6:]:   {s[6:]}')
print(f'每隔2个 s[::2]:  {s[::2]}')

# 运算
print(f'拼接: {s + " World"}')
print(f'重复: {s[:5] * 3}')
print(f'长度: {len(s)}')


print('\n' + '=' * 50)
print('第 3 课：四种容器——列表、元组、字典、集合')
print('=' * 50)

# ========== 3.1 列表 list ==========
print('\n--- 3.1 列表 (可修改，有序) ---')
fruits = ['apple', 'banana', 'orange', 'grape']
print(f'原始: {fruits}')

fruits.append('mango')               # 末尾添加
print(f'append后: {fruits}')

fruits[1] = 'pear'                   # 修改第2个
print(f'修改后: {fruits}')

removed = fruits.pop()               # 删除并取出最后一个
print(f'pop弹出: {removed} -> 剩余: {fruits}')

del fruits[0]                        # 删除第1个
print(f'del后: {fruits}')

print(f'元素个数: {len(fruits)}')
print(f'是否含有orange: {"orange" in fruits}')

print('遍历:')
for f in fruits:
    print(f'  - {f}')

# ========== 3.2 元组 tuple ==========
print('\n--- 3.2 元组 (不可修改，有序) ---')
point = (3, 4)
print(f'元组: {point}')
print(f'x={point[0]}, y={point[1]}')
# point[0] = 5  # 报错！元组不可修改

# ========== 3.3 字典 dict ==========
print('\n--- 3.3 字典 (键值对) ---')
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(f'字典: {person}')
print(f'姓名: {person["name"]}')

person['phone'] = '13800138000'      # 添加新键值对
print(f'添加后: {person}')
print(f'所有键: {list(person.keys())}')
print(f'所有值: {list(person.values())}')

# ========== 3.4 集合 set ==========
print('\n--- 3.4 集合 (不重复，无序) ---')
nums = {1, 2, 3, 2, 1, 4, 5, 3}     # 重复的会自动去掉
print(f'集合(自动去重): {nums}')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f'交集 a & b: {a & b}')         # 两个集合都有的
print(f'并集 a | b: {a | b}')         # 全部
print(f'差集 a - b: {a - b}')         # 在a但不在b的


print('\n\n=== 四种容器对比 ===')
print('列表 []  : 可修改，有序     -> 存一组同类数据，如学生名单')
print('元组 ()  : 不可修改，有序   -> 不希望被改的数据，如坐标')
print('字典 {}  : 键值对，键不重复 -> 用名字查信息，如通讯录')
print('集合 {}  : 不重复，无序     -> 去重、求交集并集')
