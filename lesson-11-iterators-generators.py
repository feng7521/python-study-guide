"""
============================================================
第 11 课：迭代器与生成器
============================================================
内容：iter()、next()、StopIteration、yield、生成器表达式
"""

print('=' * 50)
print('第 11 课：迭代器与生成器')
print('=' * 50)

# ========== 11.1 迭代器 ==========
print('\n--- 11.1 迭代器 ---')
nums = [1, 2, 3, 4, 5]
it = iter(nums)           # 创建迭代器

print('next(it):', next(it))   # 1
print('next(it):', next(it))   # 2
print('next(it):', next(it))   # 3
print('next(it):', next(it))   # 4
print('next(it):', next(it))   # 5

# 取完了再取会报错 StopIteration
try:
    print(next(it))
except StopIteration:
    print('迭代结束! StopIteration')

# ========== 11.2 生成器 yield ==========
print('\n--- 11.2 生成器 ---')

def fibonacci(n):
    """生成前 n 个斐波那契数（用 yield 而不是 return）"""
    a, b = 0, 1
    for _ in range(n):
        yield a            # yield = 返回但不结束函数
        a, b = b, a + b

fib = fibonacci(10)
print('前10个斐波那契数:')
for num in fib:
    print(num, end=' ')
print()

# 普通函数 vs 生成器
def make_list(n):
    """普通函数：一次性创建整个列表，占内存"""
    result = []
    for i in range(n):
        result.append(i * 2)
    return result

def make_generator(n):
    """生成器：按需产生，省内存"""
    for i in range(n):
        yield i * 2

print(f'make_list(5): {make_list(5)}')
print(f'make_generator(5) -> list: {list(make_generator(5))}')

# ========== 11.3 生成器表达式 ==========
print('\n--- 11.3 生成器表达式 (用 () 而不是 []) ---')
squares = (x**2 for x in range(5))
print('生成器表达式:', list(squares))

# 对比
list_comp  = [x**2 for x in range(5)]    # 列表推导，立即计算
gen_expr   = (x**2 for x in range(5))    # 生成器表达式，延迟计算
print(f'列表推导式:  {list_comp}  (类型: {type(list_comp).__name__})')
print(f'生成器表达式: {gen_expr} (类型: {type(gen_expr).__name__})')


print('\n\n=== 对比总结 ===')
print('iter(序列)  -> 创建迭代器，用 next() 逐个取值')
print('yield       -> 生成器函数，用到才产生，省内存')
print('() 表达式   -> 生成器表达式，类似列表推导但用 ()')
print('场景        -> 处理大数据/无限序列时优先用生成器')
