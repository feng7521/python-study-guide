"""
============================================================
第 9 课：异常处理 —— 让程序不怕出错
============================================================
内容：try/except、else、finally、raise、自定义异常
"""

print('=' * 50)
print('第 9 课：异常处理')
print('=' * 50)

# ========== 9.1 基本 try/except ==========
print('\n--- 9.1 基本 try/except ---')
try:
    result = 10 / 0          # 这会出错！
except ZeroDivisionError:
    print('错误: 不能除以零!')

# ========== 9.2 捕获多种异常 ==========
print('\n--- 9.2 多种异常 ---')
test_cases = [
    '10 / 0',       # ZeroDivisionError
    'int("abc")'    # ValueError
]

for case in test_cases:
    try:
        if 'abc' in case:
            int('abc')
        else:
            _ = 10 / 0
    except ZeroDivisionError:
        print(f'[{case}] -> 除零错误')
    except ValueError:
        print(f'[{case}] -> 值错误: 无法将 abc 转为数字')
    except Exception as e:
        print(f'[{case}] -> 其他错误: {e}')

# ========== 9.3 try/except/else/finally ==========
print('\n--- 9.3 完整结构 ---')

def safe_divide(a, b):
    """安全除法，处理各种情况"""
    try:
        result = a / b
    except ZeroDivisionError:
        print('错误: 除数不能为零')
        return None
    except TypeError:
        print('错误: 参数类型不对')
        return None
    else:
        print('计算成功!')
        return result
    finally:
        print(f'尝试计算: {a} / {b}')

print(safe_divide(10, 2))
print()
print(safe_divide(10, 0))

# ========== 9.4 抛出异常 raise ==========
print('\n--- 9.4 raise 抛出异常 ---')

def check_age(age):
    if age < 0:
        raise ValueError('年龄不能为负数!')
    if age > 150:
        raise ValueError('年龄不合理!')
    return f'年龄 {age} 有效'

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f'验证失败: {e}')

# ========== 9.5 自定义异常 ==========
print('\n--- 9.5 自定义异常 ---')

class ScoreError(Exception):
    """自定义分数异常"""
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise ScoreError(f'分数 {score} 不在 0~100 范围内')
    return f'分数 {score} 有效'

try:
    print(validate_score(95))
    print(validate_score(150))
except ScoreError as e:
    print(f'验证失败: {e}')


print('\n\n=== try/except 结构说明 ===')
print('try     -> 尝试执行可能出错的代码')
print('except  -> 出错时的处理方案')
print('else    -> 没出错才执行（可选）')
print('finally -> 无论是否出错都执行（可选）')
print('raise   -> 主动抛出异常')
