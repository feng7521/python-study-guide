"""
============================================================
第 14 课：标准库概览 —— Python 自带的百宝箱
============================================================
内容：os、sys、glob、time、math、random
"""
import os
import sys
import glob
import time
import math
import random

print('=' * 50)
print('第 14 课：标准库概览')
print('=' * 50)

# ========== 14.1 os 模块 ==========
print('\n--- os: 操作系统接口 ---')
print(f'当前目录: {os.getcwd()}')
print(f'平台: {os.name}')                      # nt=Windows, posix=Linux/Mac
print(f'目录列表: {os.listdir(".")[:5]}')

# 路径操作
path = os.path.join('folder', 'subfolder', 'file.txt')
print(f'拼接路径: {path}')
print(f'目录部分: {os.path.dirname(path)}')
print(f'文件名: {os.path.basename(path)}')
print(f'文件存在? {os.path.exists("README.md")}')

# ========== 14.2 sys 模块 ==========
print('\n--- sys: 系统参数 ---')
print(f'Python版本: {sys.version.split()[0]}')
print(f'平台: {sys.platform}')
print(f'最大递归: {sys.getrecursionlimit()}')

# ========== 14.3 glob 模块 ==========
print('\n--- glob: 文件搜索 ---')
py_files = glob.glob('lesson-*.py')
print(f'找到 {len(py_files)} 个 lesson 文件:')
for f in py_files:
    print(f'  {f}')

# ========== 14.4 time 模块 ==========
print('\n--- time: 时间操作 ---')
print(f'现在时间戳: {time.time():.0f}')
print(f'格式化: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')

# 计时器
start = time.perf_counter()
total = sum(range(1000000))
elapsed = time.perf_counter() - start
print(f'累加100万个数耗时: {elapsed:.4f} 秒')

# ========== 14.5 math 模块 ==========
print('\n--- math: 数学函数 ---')
print(f'pi = {math.pi}')
print(f'e  = {math.e}')
print(f'sqrt(2) = {math.sqrt(2):.4f}')
print(f'log(100) = {math.log(100):.4f}')
print(f'sin(pi/2) = {math.sin(math.pi/2)}')
print(f'ceil(3.14) = {math.ceil(3.14)}')
print(f'floor(3.14) = {math.floor(3.14)}')

# ========== 14.6 random 模块 ==========
print('\n--- random: 随机数 ---')
random.seed(42)   # 固定种子，让结果可复现
print(f'randint(1, 100):  {random.randint(1, 100)}')
print(f'random() 0~1:     {random.random():.4f}')
print(f'choice:           {random.choice(["red", "green", "blue"])}')

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f'shuffle后:        {items}')


print('\n\n=== 常用标准库速查 ===')
print('os       -> 文件/目录操作、环境变量')
print('sys      -> Python 解释器相关')
print('glob     -> 文件通配符搜索')
print('time     -> 时间戳、计时、sleep')
print('math     -> 数学函数和常量')
print('random   -> 随机数生成')
print('datetime -> 日期时间（见第15课）')
print('json     -> JSON 解析（见第15课）')
print('re       -> 正则表达式（见第16课）')
