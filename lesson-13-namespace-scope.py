"""
============================================================
第 13 课：命名空间与作用域
============================================================
内容：LEGB 规则、local/global/nonlocal
"""

print('=' * 50)
print('第 13 课：命名空间与作用域')
print('=' * 50)

# ========== LEGB 规则 ==========
print("""
Python 查找变量的顺序 (LEGB):
  L - Local:      函数内部
  E - Enclosing:  外层函数（嵌套函数中）
  G - Global:     模块级别（整个文件）
  B - Built-in:   内置（print、len 等）

当 Python 遇到一个变量名时，按这个顺序查找。
""")

# ========== 13.1 LEGB 示例 ==========
x = 'global 变量'          # G: 全局

def outer():
    y = 'outer 变量'       # E: 对于 inner 来说的外部
    print('outer 内部可以看到:', x)

    def inner():
        z = 'inner 变量'   # L: 局部
        print('inner 内部可以看到:', x, y, z)

    inner()
    # print(z)   # 报错！不能访问内层的局部变量

outer()

# ========== 13.2 global 关键字 ==========
print('\n--- global: 在函数内修改全局变量 ---')
count = 100

def change_count():
    global count          # 声明要修改全局变量
    count = 200

print(f'修改前: {count}')
change_count()
print(f'修改后: {count}')

# 不加 global 会怎样？
name = 'global'

def try_change():
    name = 'local'       # 这创建了一个局部变量，不影响全局
    print(f'  函数内 name = {name}')

try_change()
print(f'函数外 name 还是 = {name}')   # 还是 global

# ========== 13.3 nonlocal 关键字 ==========
print('\n--- nonlocal: 修改外层函数的变量 ---')

def outer_func():
    value = '外层'
    def inner_func():
        nonlocal value     # 声明要修改外层函数的变量
        value = '被内层修改了'
    print(f'调用前: {value}')
    inner_func()
    print(f'调用后: {value}')

outer_func()

# ========== 13.4 实战示例 ==========
print('\n--- 闭包 (closure) 示例 ---')

def make_counter():
    count = 0                    # enclosing scope
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter()
c2 = make_counter()
print(f'c1: {c1()}, {c1()}, {c1()}')   # 1, 2, 3
print(f'c2: {c2()}, {c2()}')            # 1, 2 (独立计数)


print('\n\n=== LEGB 速查 ===')
print('L: Local      -> 函数内部变量')
print('E: Enclosing  -> 嵌套函数的外层变量')
print('G: Global     -> 文件顶层变量')
print('B: Built-in   -> Python 自带的 (print, len...)')
print()
print('global    关键字 -> 在函数内修改全局变量')
print('nonlocal  关键字 -> 在嵌套函数内修改外层变量')
