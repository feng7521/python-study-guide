"""
============================================================
第 10 课：面向对象编程 (OOP) 入门
============================================================
内容：类、对象、__init__、继承、多态、封装
"""

print('=' * 50)
print('第 10 课：面向对象编程 (OOP)')
print('=' * 50)

# ========== 10.1 类和对象 ==========
# 类 = 模板/蓝图    对象 = 根据模板创建的具体实例

print('\n--- 10.1 定义类 & 创建对象 ---')

class Dog:
    """Dog类"""
    species = 'Canis familiaris'    # 类属性（所有实例共享）

    def __init__(self, name, age):
        """__init__ 是构造函数，创建对象时自动调用"""
        self.name = name            # 实例属性（每个实例不同）
        self.age = age

    def bark(self):
        """实例方法"""
        return f'{self.name}: Woof! Woof!'

    def info(self):
        return f'{self.name}, {self.age} years old'

# 创建对象（实例化）
dog1 = Dog('Max', 3)
dog2 = Dog('Luna', 1)

print(dog1.info())
print(dog1.bark())
print(dog2.info())
print(f'物种(类属性): {dog1.species}')

# ========== 10.2 继承 ==========
print('\n--- 10.2 继承 ---')

class GuideDog(Dog):                # GuideDog 继承自 Dog
    """导盲犬类，继承自Dog"""

    def __init__(self, name, age, training_level):
        super().__init__(name, age) # 调用父类的 __init__
        self.training_level = training_level

    def guide(self):
        """导盲犬特有的方法"""
        return f'{self.name} is guiding... (level {self.training_level})'

    def bark(self):
        """重写(override)父类方法"""
        return f'{self.name}: Soft bark...'

gd = GuideDog('Buddy', 2, 'A')
print(gd.info())                    # 继承自 Dog 的方法
print(gd.bark())                    # 调自己重写的版本
print(gd.guide())                   # 调自己新增的方法
print(f'是Dog的子类? {issubclass(GuideDog, Dog)}')
print(f'是Dog的实例? {isinstance(gd, Dog)}')
print(f'是GuideDog的实例? {isinstance(gd, GuideDog)}')

# ========== 10.3 多态 ==========
print('\n--- 10.3 多态 ---')

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name}: Meow~'

class Duck:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name}: Quack!'

# 多态：不同类的对象可以用同样的方式调用
animals = [Dog('Max', 3), Cat('Kitty'), Duck('Donald')]
for animal in animals:
    print(animal.speak())   # 每个动物用自己的方式 speak

# ========== 10.4 封装（私有属性）==========
print('\n--- 10.4 封装 ---')

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance    # __ 开头的属性是私有的

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'存入 {amount}, 余额: {self.__balance}'
        return '金额必须大于0'

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f'取出 {amount}, 余额: {self.__balance}'
        return '余额不足或金额无效'

    def get_balance(self):
        return self.__balance

account = BankAccount('Alice', 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f'当前余额: {account.get_balance()}')
# print(account.__balance)  # 报错！不能直接访问私有属性


print('\n\n=== OOP 三个核心概念 ===')
print('封装: 把数据和方法打包在一起，隐藏内部细节')
print('继承: 子类继承父类的属性和方法，减少重复代码')
print('多态: 不同类可以实现同名方法，调用方式统一')
