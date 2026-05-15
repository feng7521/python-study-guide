"""
============================================================
第 7 课 & 第 8 课：模块 + 文件操作
============================================================
内容：import、常用模块、文件读写
"""

import math
import random
import os
from datetime import datetime

print('=' * 50)
print('第 7 课：模块 —— 使用别人写好的代码')
print('=' * 50)

# ========== 7.1 三种导入方式 ==========
print('\n--- 7.1 三种导入方式 ---')
print('import math                # 导入整个模块')
print('from datetime import datetime # 只导入某个函数')
print('import random as rnd        # 取别名')

# ========== 7.2 常用内置模块 ==========
print('\n--- 7.2 math 模块 ---')
print(f'pi = {math.pi}')
print(f'sqrt(16) = {math.sqrt(16)}')
print(f'3! = {math.factorial(3)}')

print('\n--- 7.3 datetime 模块 ---')
now = datetime.now()
print(f'现在时间: {now}')
print(f'日期: {now.year}/{now.month}/{now.day}')

print('\n--- 7.4 random 模块 ---')
print(f'随机数 1~100: {random.randint(1, 100)}')
print(f'随机选择: {random.choice(["red", "green", "blue"])}')

# 查看模块内容
print('\n--- 7.5 查看模块内容 ---')
print(f'math 模块函数: {dir(math)[-10:]}')


print('\n' + '=' * 50)
print('第 8 课：文件操作 —— 读写文件')
print('=' * 50)

test_file = 'lesson-05-demo-file.txt'

# ========== 8.1 写入文件 ==========
print('\n--- 8.1 写入文件 (w模式) ---')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write('Hello Python!\n')
    f.write('这是第二行\n')
    f.write('Python makes coding easy.\n')
print('文件写入成功!')

# ========== 8.2 读取文件 ==========
print('\n--- 8.2 读取全部 (read) ---')
with open(test_file, 'r', encoding='utf-8') as f:
    content = f.read()
print(content)

print('--- 8.3 逐行读取 (readlines) ---')
with open(test_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f'第{i}行: {line.strip()}')

# ========== 8.4 追加写入 ==========
print('\n--- 8.4 追加写入 (a模式) ---')
with open(test_file, 'a', encoding='utf-8') as f:
    f.write('这是追加的一行\n')
print('追加完成!')

with open(test_file, 'r', encoding='utf-8') as f:
    print(f'最新内容: {f.readlines()}')

# 清理
os.remove(test_file)


print('\n\n=== 文件操作模式速查 ===')
print("'r' : 读取（文件必须存在）")
print("'w' : 写入（会覆盖已有内容）")
print("'a' : 追加（在末尾添加）")
print("'rb'/'wb' : 二进制模式（图片、视频等）")
print("with open(...) as f : 推荐写法，自动关闭文件")
