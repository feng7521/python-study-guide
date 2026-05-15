"""
============================================================
第 15 课：JSON 数据处理 + 日期时间
============================================================
内容：json.dumps/loads、datetime、timedelta、strftime
"""
import json
from datetime import datetime, date, timedelta, time

print('=' * 50)
print('第 15 课：JSON 数据处理 + 日期时间')
print('=' * 50)

# ========== 15.1 JSON: Python -> JSON 字符串 ==========
print('\n--- JSON: dict 转 JSON 字符串 (dumps) ---')
data = {
    'name': 'Alice',
    'age': 25,
    'skills': ['Python', 'SQL', 'Excel'],
    'married': False,
    'score': None
}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# 没有 indent 的紧凑格式
print(f'紧凑: {json.dumps(data, ensure_ascii=False)}')

# ========== 15.2 JSON: JSON 字符串 -> Python ==========
print('\n--- JSON: JSON 字符串转 dict (loads) ---')
json_text = '{"name": "Bob", "age": 30, "city": "Shanghai"}'
parsed = json.loads(json_text)
print(f'解析结果: {parsed}')
print(f'类型: {type(parsed).__name__}')
print(f'姓名: {parsed["name"]}, 年龄: {parsed["age"]}')

# ========== 15.3 JSON 文件读写 ==========
print('\n--- JSON 文件读写 ---')

test_file = 'lesson-15-demo.json'
with open(test_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'写入文件: {test_file}')

with open(test_file, 'r', encoding='utf-8') as f:
    loaded = json.load(f)
print(f'从文件读取: {loaded["name"]}')
import os
os.remove(test_file)

# ========== 15.4 datetime ==========
print('\n--- datetime: 日期时间 ---')

now = datetime.now()
print(f'现在: {now}')
print(f'  年={now.year}, 月={now.month}, 日={now.day}')
print(f'  时={now.hour}, 分={now.minute}, 秒={now.second}, 微秒={now.microsecond}')

# 创建指定时间
dt = datetime(2026, 1, 1, 12, 30, 0)
print(f'指定时间: {dt}')

# ========== 15.5 timedelta: 时间运算 ==========
print('\n--- timedelta: 时间运算 ---')

today = date.today()
print(f'今天: {today}')
print(f'一周后: {today + timedelta(days=7)}')
print(f'三周前: {today - timedelta(weeks=3)}')
print(f'100天后: {today + timedelta(days=100)}')

birthday = date(2000, 1, 1)
age_days = (today - birthday).days
print(f'从 {birthday} 到今天共 {age_days} 天')
print(f'约 {age_days // 365} 年')

# ========== 15.6 strftime/strptime: 格式化 ==========
print('\n--- strftime: 格式化输出 ---')

now = datetime.now()
print(f'ISO格式:    {now.isoformat()}')
print(f'自定义:     {now.strftime("%Y年%m月%d日 %H:%M:%S")}')
print(f'英文:       {now.strftime("%A, %B %d, %Y")}')
print(f'简短:       {now.strftime("%y/%m/%d")}')

# strptime: 字符串解析为时间
date_str = '2026-05-15 16:30:00'
parsed_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
print(f'strptime解析: {parsed_date}')


print('\n\n=== JSON & DateTime 速查 ===')
print('json.dumps(obj)      -> Python对象转JSON字符串')
print('json.loads(str)      -> JSON字符串转Python对象')
print('json.dump(obj, f)    -> 写入JSON文件')
print('json.load(f)         -> 读取JSON文件')
print()
print('datetime.now()       -> 当前日期时间')
print('date.today()         -> 今天日期')
print('timedelta(days=7)    -> 时间间隔')
print('strftime("%Y-%m-%d") -> 格式化输出')
print('strptime(str, fmt)   -> 字符串解析为时间')
