"""
============================================================
第 6 课：函数 —— 把代码封装成"积木块"
============================================================
内容：def、参数类型、return、lambda
"""

print('=' * 50)
print('第 6 课：函数')
print('=' * 50)

# ========== 6.1 定义和调用函数 ==========
print('\n--- 6.1 定义和调用 ---')

def greet(name):
    """这是一个打招呼的函数"""
    print(f'你好, {name}!')

def add(a, b):
    """返回两个数的和"""
    return a + b

greet('小明')
greet('Alice')

result = add(3, 5)
print(f'3 + 5 = {result}')
print(f'10 + 20 = {add(10, 20)}')

# ========== 6.2 参数的四种写法 ==========
print('\n--- 6.2 参数的四种写法 ---')

# 1. 默认参数——不传就用默认值
def power(x, n=2):
    return x ** n

print(f'3的平方: {power(3)}')         # n默认是2
print(f'3的立方: {power(3, 3)}')      # n指定为3

# 2. 关键字参数——按名称传递，顺序无所谓
def introduction(name, age, city):
    print(f'{name}, {age}岁, 来自{city}')

introduction(age=25, city='Beijing', name='Bob')

# 3. 可变参数 *args——接收任意多个参数
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(f'求和 1+2+3: {sum_all(1, 2, 3)}')
print(f'求和 1~5: {sum_all(1, 2, 3, 4, 5)}')

# 4. 关键字可变参数 **kwargs
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f'  {key}: {value}')

print('**kwargs 示例:')
show_info(name='Tom', age=30, job='Engineer')

# ========== 6.3 lambda 匿名函数 ==========
print('\n--- 6.3 lambda 匿名函数 ---')
square = lambda x: x ** 2
add_xy = lambda x, y: x + y

print(f'lambda: 5的平方 = {square(5)}')
print(f'lambda: 3+7 = {add_xy(3, 7)}')

# lambda 常和 map/filter 一起用
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f'原列表: {nums}')
print(f'平方 map: {squared}')
print(f'偶数 filter: {evens}')


print('\n\n=== 函数要点总结 ===')
print('def 函数名(参数):     -> 定义函数')
print('return               -> 返回值')
print('def fn(x, n=2)       -> 默认参数')
print('def fn(*args)        -> 任意多个参数')
print('lambda x: x**2       -> 匿名函数（一行函数）')
