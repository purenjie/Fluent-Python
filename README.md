# Fluent Python

### Chapter 1

#### Section 1

- namedtuple用以构建只有少数属性但是没有方法的对象

- `random.choice(seq)`

  Return a random element from the non-empty sequence *seq*. If *seq* is empty, raises [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError).

- `reversed(seq)`

  Return a reverse [iterator](https://docs.python.org/3/glossary.html#term-iterator). *seq* must be an object which has a [`__reversed__()`](https://docs.python.org/3/reference/datamodel.html#object.__reversed__) method or supports the sequence protocol (the [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__) method and the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) method with integer arguments starting at `0`).

通过数据模型和一些合成来实现这些功能。 通过实现 `__len__`和 `__getitem__` 这两个特殊方法， FrenchDeck 就跟一个 Python 自有的序列数据类型一样， 可以体现出 Python 的核心语言特性（ 例如迭代和切片） 。 同时这个类还可以用于标准库中诸如random.choice、 reversed 和 sorted 这些函数。 另外， 对合成的运用使得 `__len__` 和` __getitem__` 的具体实现可以代理给 self._cards这个 Python 列表（ 即 list 对象） 。

#### Section 2

 特殊方法的存在是为了被 Python 解释器调用的， 你自己并不需要调用它们。 也就是说没有 `my_object.__len__()` 这种写法，而应该使用 len(my_object)。 在执行 len(my_object) 的时候， 如果my_object 是一个自定义类的对象， 那么 Python 会自己去调用其中由你实现的` __len__` 方法。


