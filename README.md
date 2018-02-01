# Fluent Python

### Chapter 1  Python数据模型

特殊方法名能让你自己的对象实现和支持以下的语言构架， 并与之交互：

- 迭代
- 集合类
- 属性访问
- 运算符重载
- 函数和方法的调用
- 对象的创建和销毁
- 字符串表示形式和格式化
- 管理上下文（ 即 with 块）

特殊方法的存在是为了被 Python 解释器调用的， 你自己并不需要调用它们。通过内置的函数（ 例如 len、 iter、 str， 等等） 来使用特殊方法是最好的选择。 这些内置函数不仅会调用特殊方法， 通常还提供额外的好处， 而且对于内置的类来说， 它们的速度更快。

通过实现特殊方法， 自定义数据类型可以表现得跟内置类型一样， 从而让我们写出更具表达力的代码——或者说， 更具 Python 风格的代码。

len 之所以不是一个普通方法

1. 是为了让 Python 自带的数据结构可以走后门，速度更快。
2. 可以把 len 用于自定义数据类型。

bool(x) 的背后是调用`x.__bool__()` 的结果； 如果不存在`__bool__` 方法， 那么 bool(x) 会尝试调用 `x.__len__()`。 若返回 0， 则 bool 会返回 False； 否则返回True。

### Chapter 2  序列构成的数组

Python 从 ABC 那里继承了用统一的风格去处理序列数据这一特点。不管是哪种数据结构， 字符串、 列表、 字节序列、 数组、 XML元素，抑或是数据库查询结果， 它们都共用一套丰富的操作： 迭代、 切片、 排序， 还有拼接。

#### 内置序列

- 存放类型
  - 容器序列

    list、 tuple 和 collections.deque 这些序列能存放不同类型的数据

  -  扁平序列

     str、 bytes、 bytearray、 memoryview 和 array.array， 这类序列只能容纳一种类型。

> 容器序列存放的是它们所包含的任意类型的对象的引用， 而扁平序列里存放的是值而不是引用。 换句话说， 扁平序列其实是一段连续的内存空间。 扁平序列体积更小、 速度更快而且用起来更简单， 但是它只能保存一些原子性的数据，比如数字、 字符和字节。 容器序列则比较灵活， 但是当容器序列遇到可变对象时，容易产生意外情况，需确保代码正确。

- 能否被修改

  - 可变序列

  list、 bytearray、 array.array、 collections.deque 和memoryview

  - 不可变序列

  tuple、 str 和 bytes

#### 列表推导（ list comprehension） 

列表推导可以帮助我们把一个序列或是其他可迭代类型中的元素过滤或是加工， 然后再新建一个列表。

Python3表达式内部的变量和赋值只在局部起作用， 表达式的上下文里的同名变量还可以被正常引用， 局部变量并不会影响到它们。

```python
>>> x = 'ABC'
>>> dummy = [ord(x) for x in x]
>>> x 
'ABC'
>>> dummy 
[65, 66, 67]
```

列表推导中两个 for 循环时，两者的关系为嵌套关系，执行关系为先内层后外层

```python
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']

>>> tshirts = [(color, size) for color in colors for size in sizes] 
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
('white', 'M'), ('white', 'L')]

>>> tshirts = [(color, size) for size in sizes for color in colors]
>>> tshirts
[('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
('black', 'L'), ('white', 'L')]
```

列表推导的作用只有一个： 生成列表。

#### 生成器表达式（ generator expression）

如果想生成其他类型的序列， 生成器表达式就派上了用场。

**虽然也可以用列表推导来初始化元组、 数组或其他序列类型， 但是生成器表达式是更好的选择。 这是因为生成器表达式背后遵守了迭代器协议， 可以逐个地产出元素， 而不是先建立一个完整的列表， 然后再把这个列表传递到某个构造函数里。 可以节省内存。**

使用生成器逐个产出元素

```python
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): 
... print(tshirt)
...
black S
black M
black L
white S
white M
white L
```

#### 元组（tuple）

1. **没有字段名的记录**

元组其实是对数据的记录，元组中的每个元素都存放了记录中一个字段的数据， 外加这个字段的位置。 正是这个位置信息给数据赋予了意义。

**元组拆包**

for 循环可以分别提取元组里的元素， 也叫作拆包（ unpacking）

```python
# 平行赋值
>>> lax_coordinates = (33.9425, -118.408056)
>>> latitude, longitude = lax_coordinates 

# 不使用中间变量交换两个变量的值
>>> b, a = a, b

# 用 * 运算符把可迭代对象拆开作为函数的参数
>>> t = (20, 8)
>>> divmod(*t)
>>> quotient, remainder = divmod(*t)

# 让一个函数可以用元组的形式返回多个值
>>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
```

> _ 占位符可表示我们不感兴趣的数据
>
> \* 也可以忽略我们不感兴趣的数据

接受表达式的元组可以是嵌套式的， 例如 (a, b, (c, d))。 只要这个接受元组的嵌套结构符合表达式本身的嵌套结构， Python 就可以作出正确的对应。

```python
>>> grades = [('LiMing', 'male', ('grade', 'A')),
...           ('LiuYang', 'female', ('grade', 'B')),
...           ('ZhangNing', 'male', ('grade', 'c'))]
>>> for name, gender, (grade, Alpha) in grades:
...     print('%s:%s' % (name, gender))
...     print('%s:%s' % (grade, Alpha))
... 
LiMing:male
grade:A
LiuYang:female
grade:B
ZhangNing:male
grade:c
```

2. **不可变列表**

除了跟增减元素相关的方法之外， 元组支持列表的其他所有方法。

#### 具名元组（namedtuple）

collections.namedtuple 是一个工厂函数， 它可以用来构建一个带字段名的元组和一个有名字的类——这个带名字的类对调试程序有很大帮助。

创建一个具名元组需要**两个参数**， 一个是类名， 另一个是类的各个字段的名字。 后者可以是由数个字符串组成的可迭代对象， 或者是由空格分隔开的字段名组成的字符串。

```python
>>> from collections import namedtuple

# 由数个字符串组成的可迭代对象
>>> City = namedtuple('City', 'name country population coordinates') 
# 由空格分隔开的字段名组成的字符串
>>> City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) 
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
139.691667))
```

除了从普通元组那里继承来的属性之外， 具名元组还有一些自己专有的属性。

```python
>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates')

# _fields 返回一个包含这个类所有字段名称的元组
>>> City._fields
('name', 'country', 'population', 'coordinates')
>>> delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))

# _make() 接收一个可迭代对象生成类的实例 
>>> delhi = City._make(delhi_data)
>>> delhi
City(name='Delhi NCR', country='IN', population=21.935, coordinates=(28.613889, 77.208889))

# _asdict() 以collections.OrderedDict 的形式返回
>>> delhi._asdict()
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', (28.613889, 77.208889))])
```

#### 切片

可以用 s[a：b：c] 的形式对 s 在 a 和 b之间以 c 为间隔取值。 c 的值还可以为负， 负值意味着反向取值。

s1 = s[::-1]可对序列取反

如果把切片放在赋值语句的左边， 或把它作为 del 操作的对象， 我们就可以对序列进行嫁接、 切除或就地修改操作。

```python
>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[2:5] = [20, 30]
>>> l
[0, 1, 20, 30, 5, 6, 7, 8, 9]
>>> del l[5:7]
>>> l
[0, 1, 20, 30, 5, 8, 9]
# 复制对象是切片时，右边必须为可迭代序列
>>> l[2:5] = [100]
```



**序列  +、\* 和增量赋值**

如果在 a * n 这个语句中， 序列 a 里的元素是对其他可变对象的引用的话，生成新序列的 n 个引用都指向同一个对象。修改原始对象内容 n 个引用同时改变。可用`[a for i in range(n)]`创建

增量赋值

- 可变序列：就地修改原对象的值，引用指向的内存地址不变
- 不可变序列：在背后生成新的序列（创建一个新的指向不同内存地址的同名引用）

 += 背后的特殊方法是 \_\_iadd\_\_ 。但是如果一个类没有实现这个方法的话， Python 会退一步调用 \_\_add\_\_。\*=同理 

#### 序列排序

list.sort 方法会就地排序列表，返回值是 None

如果一个函数或者方法对对象进行的是就地改动， 那它就应该返回 None， 好让调用者知道传入的参数发生了变动， 而且并未产生新的对象。

内置函数 sorted 会新建一个列表作为返回值。可以接受任何形式的可迭代对象作为参数， 甚至包括不可变序列或生成器。 而不管 sorted 接受的是怎样的参数， 它最后都会返回一个列表。

list.sort 方法和 sorted 函数， 都有两个可选的关键字参数：

- reverse：True or False
- key：一个只有一个参数的函数， 这个函数会被用在序列里的每一个元素上， 所产生的结果将是排序算法依赖的对比关键字。key=str.lower  key=len 

**用bisect来管理已排序的序列**

`import bisect`

bisect(haystack, needle) 把 needle 插入这个位置之后， haystack 还能保持升序

bisect_left(haystack, needle) 插到相同元素前面

bisect.bisect 的作用则是快速查找，可以用来建立一个用数字作为索引的查询表格

```python
>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
... i = bisect.bisect(breakpoints, score)
... return grades[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

**用bisect.insort插入新元素**

bisect.insort(seq, item) 把变量 item 插入到序列 seq 中， 并能保持 seq的升序顺序

#### 数组

`from array import array`

如果需要一个只包含数字的列表， 那么 array.array 比 list 更高效

另外一个快速序列化数字类型的方法是使用[pickle](https://docs.python.org/3/library/pickle.html)模块。pickle.dump 可以处理几乎所有的内置数字类型， 包含复数、 嵌套集合， 甚至用户自定义的类。

array.tofile 和 array.fromfile 方法将列表存入文件或取出

数组排序需用 sorted 函数新建数组

`a = array.array(a.typecode, sorted(a))`

**NumPy 和 SciPy**处理大规模数值型数据

#### 双向队列和其他形式队列

`from collections import deque`

 双向队列是一个线程安全、 可以快速从两端添加或者删除元素的数据类型。便于存放“最近用到的几个元素”

