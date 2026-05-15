"""
============================================================
第 16 课：正则表达式 —— 文本搜索利器
============================================================
内容：re.search、re.findall、re.sub、re.split、正则符号速查
"""
import re

print('=' * 50)
print('第 16 课：正则表达式')
print('=' * 50)

text = 'Contact us: alice@example.com or bob123@company.cn. Phone: 138-1234-5678'

# ========== 16.1 search: 找第一个匹配 ==========
print('\n--- search: 找第一个匹配 ---')
match = re.search(r'\w+@\w+\.\w+', text)
print(f'文本: {text}')
print(f'search 找到: {match.group() if match else "没找到"}')

# ========== 16.2 findall: 找所有匹配 ==========
print('\n--- findall: 找所有匹配 ---')
emails = re.findall(r'[\w.]+@[\w.]+', text)
print(f'所有邮箱: {emails}')

# 找所有数字
all_digits = re.findall(r'\d+', text)
print(f'所有数字: {all_digits}')

# ========== 16.3 分组匹配 ==========
print('\n--- 分组匹配 () ---')
phone_pattern = r'(\d{3})-(\d{4})-(\d{4})'
match = re.search(phone_pattern, text)
if match:
    print(f'完整手机号: {match.group()}')
    print(f'区号: {match.group(1)}')
    print(f'中间: {match.group(2)}')
    print(f'末尾: {match.group(3)}')

# ========== 16.4 sub: 替换 ==========
print('\n--- sub: 替换 ---')

# 邮箱脱敏
masked = re.sub(r'(\w+)@', '***@', text)
print(f'邮箱脱敏: {masked}')

# ========== 16.5 split: 分割字符串 ==========
print('\n--- split: 用正则分割 ---')
csv_line = 'apple,  banana , orange , grape'
fields = re.split(r'\s*,\s*', csv_line)
print(f'原始: "{csv_line}"')
print(f'分割: {fields}')

# ========== 16.6 实战示例 ==========
print('\n--- 实战: 验证常见格式 ---')

def is_valid_email(s):
    pattern = r'^[\w.+-]+@[\w-]+\.[\w.]+$'
    return bool(re.match(pattern, s))

def is_valid_phone(s):
    pattern = r'^\d{3}-\d{4}-\d{4}$'
    return bool(re.match(pattern, s))

print(f'is_valid_email("test@example.com"): {is_valid_email("test@example.com")}')
print(f'is_valid_email("not-an-email"): {is_valid_email("not-an-email")}')
print(f'is_valid_phone("138-1234-5678"): {is_valid_phone("138-1234-5678")}')
print(f'is_valid_phone("12345"): {is_valid_phone("12345")}')


print('\n\n=== 常用正则符号速查 ===')
symbols = [
    (r'\d',     '数字 [0-9]'),
    (r'\w',     '字母/数字/下划线'),
    (r'\s',     '空白字符(空格/Tab/换行)'),
    (r'.',      '任意字符(除换行)'),
    (r'*',      '0次或多次'),
    (r'+',      '1次或多次'),
    (r'?',      '0次或1次'),
    (r'{n,m}',  'n到m次'),
    (r'^',      '字符串开头'),
    (r'$',      '字符串结尾'),
    (r'[abc]',  'a或b或c'),
    (r'[^abc]', '不是a/b/c'),
    (r'(...)',  '分组捕获'),
    (r'|',      '或 (a|b)'),
]
for sym, desc in symbols:
    print(f'  {sym:10s} {desc}')
