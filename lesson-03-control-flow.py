"""
============================================================
第 4 课 & 第 5 课：条件判断 + 循环
============================================================
内容：if/elif/else、match case、for、while、break、continue
"""

print('=' * 50)
print('第 4 课：条件判断 —— 让程序会"思考"')
print('=' * 50)

# ========== 4.1 if / elif / else ==========
print('\n--- 4.1 if/elif/else ---')
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'分数: {score}, 等级: {grade}')

# ========== 4.2 比较运算符 ==========
print('\n--- 4.2 比较运算符 ---')
print('==  等于 (注意是双等号！不等于赋值号 =)')
print('!=  不等于')
print('>  >=  <  <=')

# ========== 4.3 逻辑运算符 ==========
print('\n--- 4.3 逻辑运算符 ---')
print('and  与：两个条件都成立')
print('or   或：任一条件成立')
print('not  非：取反')

age, has_id = 20, True
if age >= 18 and has_id:
    print(f'age={age}, has_id={has_id} -> 允许进入')
else:
    print('禁止进入')

# ========== 4.4 match case ==========
print('\n--- 4.4 match case (Python 3.10+) ---')
day = 3
match day:
    case 1:
        day_name = 'Monday'
    case 2:
        day_name = 'Tuesday'
    case 3:
        day_name = 'Wednesday'
    case 4 | 5:
        day_name = 'Thu/Fri'
    case _:                     # _ 是通配符，匹配任何值
        day_name = 'Weekend'
print(f'Day {day}: {day_name}')


print('\n' + '=' * 50)
print('第 5 课：循环 —— 让程序会"重复"')
print('=' * 50)

# ========== 5.1 for 循环 ==========
print('\n--- 5.1 for 循环 ---')

# 遍历列表
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(f'水果: {fruit}')

# range() 函数：生成一系列数字
print('\nrange(5) 遍历 0~4:')
for i in range(5):
    print(f'  第{i+1}次')

# 嵌套循环：九九乘法表
print('\n九九乘法表:')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}x{i}={i*j}', end='\t')
    print()

# ========== 5.2 while 循环 ==========
print('\n--- 5.2 while 循环 ---')

count = 1
while count <= 5:
    print(f'循环第{count}次')
    count += 1           # 等价于 count = count + 1

# ========== 5.3 break 和 continue ==========
print('\n--- 5.3 break: 立即结束循环 ---')
for i in range(1, 10):
    if i == 5:
        break            # i=5 时直接跳出循环
    print(i, end=' ')
print()

print('\n--- 5.4 continue: 跳过本次，继续下次 ---')
for i in range(1, 11):
    if i % 2 == 0:       # i 是偶数
        continue         # 跳过偶数
    print(i, end=' ')
print()


print('\n\n=== 循环要点总结 ===')
print('for x in 序列   -> 遍历每个元素')
print('range(n)        -> 生成 0 到 n-1 的整数序列')
print('while 条件      -> 条件成立就一直循环')
print('break           -> 立即跳出整个循环')
print('continue        -> 跳过这次，继续下一次')
