# Python 3 从零开始学习指南

> 基于《菜鸟教程 Python3 教程》整理，适合零基础新手

---

## 学习路线图（四个阶段）

### 第一阶段：打基础（预计 1-2 周）

| 序号 | 章节 | 核心内容 | 学习目标 |
|------|------|----------|----------|
| 1 | Python3 简介 | 什么是Python、Python特点、应用领域 | 知道Python能做什么 |
| 2 | Python3 环境搭建 | 下载安装Python、配置PATH、验证安装 | 能在自己电脑上运行Python |
| 3 | Python3 解释器 | 交互模式、脚本模式、命令行参数 | 会用两种方式运行Python代码 |
| 4 | Python3 基础语法 | 编码、标识符、保留字、缩进、多行语句 | 能写出正确的Python代码 |
| 5 | Python3 注释 | 单行注释 `#`、多行注释 `'''` 或 `"""` | 学会给代码加说明 |
| 6 | Python3 运算符 | 算术、比较、赋值、逻辑、位、成员、身份 | 会用各种运算符号 |
| 7 | Python3 编程第一步 | 斐波那契数列实例 | 写出第一个完整程序 |

### 第二阶段：数据类型与结构（预计 2-3 周）

| 序号 | 章节 | 核心内容 | 学习目标 |
|------|------|----------|----------|
| 8 | Python3 数字 | int、float、complex、数学函数、随机数 | 处理数字运算 |
| 9 | Python3 字符串 | 创建、截取、格式化、转义、常用方法 | 处理文本信息 |
| 10 | Python3 列表 | 创建、访问、修改、删除、嵌套、常用方法 | 存储一组有序数据 |
| 11 | Python3 元组 | 创建、访问、不可变性、与列表的区别 | 存储不可修改的数据 |
| 12 | Python3 字典 | 键值对、增删改查、遍历 | 用"名字"查找数据 |
| 13 | Python3 集合 | 创建、去重、交集并集差集 | 数学集合运算 |

### 第三阶段：程序控制与函数（预计 2-3 周）

| 序号 | 章节 | 核心内容 | 学习目标 |
|------|------|----------|----------|
| 14 | Python3 条件控制 | if、elif、else、match case | 让程序会"判断" |
| 15 | Python3 循环语句 | while、for、break、continue、pass、else | 让程序会"重复" |
| 16 | Python3 迭代器与生成器 | iter、next、yield | 理解更高级的遍历 |
| 17 | Python3 函数 | 定义、参数、返回值、匿名函数、变量作用域 | 封装可复用的代码块 |
| 18 | Python3 数据结构 | 列表推导式、del、序列操作技巧 | 更高效的数据操作 |
| 19 | Python3 模块 | import、from...import、__name__、包 | 组织和使用代码文件 |
| 20 | Python3 输入和输出 | print、input、格式化输出、文件读写 | 程序与人交互 |
| 21 | Python3 错误和异常 | try/except、raise、finally、自定义异常 | 让程序更健壮 |

### 第四阶段：进阶内容（预计 2-4 周）

| 序号 | 章节 | 核心内容 |
|------|------|----------|
| 22 | Python3 面向对象 | 类、对象、继承、多态、封装 |
| 23 | Python3 命名空间/作用域 | global、nonlocal、LEGB规则 |
| 24 | Python3 标准库概览 | os、sys、math、datetime等 |
| 25 | Python3 正则表达式 | re模块、模式匹配 |
| 26 | Python3 多线程 | threading模块 |
| 27 | Python3 日期和时间 | time、datetime、calendar |
| 28 | Python3 JSON | JSON解析与生成 |
| 29 | Python3 网络编程 | socket编程 |
| 30 | Python3 MySQL | 数据库操作 |

---

---

## 课程文件（可直接运行）

| 文件 | 对应课程 |
|------|----------|
| `lesson-01-basics.py` | 第1课：print()、变量、运算符、缩进、注释 |
| `lesson-02-data-types.py` | 第2-3课：数字、字符串、列表、元组、字典、集合 |
| `lesson-03-control-flow.py` | 第4-5课：条件判断、for/while 循环、break/continue |
| `lesson-04-functions.py` | 第6课：函数、参数、lambda、map/filter |
| `lesson-05-modules-files.py` | 第7-8课：模块导入、文件读写 |
| `lesson-06-exceptions.py` | 第9课：try/except、异常处理、自定义异常 |
| `lesson-07-oop.py` | 第10课：类、对象、继承、多态、封装 |
| `lesson-11-iterators-generators.py` | 第11课：iter()、next()、yield、生成器 |
| `lesson-12-advanced-data-structures.py` | 第12课：列表推导式、栈、队列、遍历技巧 |
| `lesson-13-namespace-scope.py` | 第13课：LEGB 规则、global、nonlocal |
| `lesson-14-stdlib.py` | 第14课：os、sys、glob、time、math、random |
| `lesson-15-json-datetime.py` | 第15课：JSON 数据解析、日期时间操作 |
| `lesson-16-regex.py` | 第16课：正则表达式、search、findall、sub |

> 用 `python lesson-01-basics.py` 即可运行任意课程文件

---

## 给新手的学习建议

1. **动手！动手！动手！** —— 只看不写永远学不会。每个例子都要亲手敲一遍。
2. **每天坚持** —— 每天学30分钟比周末一口气学6小时效果好得多。
3. **遇到错误是好事** —— 每个报错信息都在教你东西，仔细读它。
4. **先理解概念，不追求细节** —— 第一遍不要纠结每个函数的所有参数，理解"是什么、用来干什么"就够。
5. **做笔记** —— 用自己的话记录学到的知识点。
6. **不要跳步骤** —— 前面章节是后面的基础。
