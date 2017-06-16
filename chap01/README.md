# Python Magic Method

Python 中的魔术方法对于编写 Pythonic 的代码非常有用，比如 `__len__, __str__, __getitem__` 等，
如果你希望自己的类也能享受 Python 解释器提供的便利性操作，可以自己在类中定义这些方法，之后使用内置函数 `len` 等调用时会自动调用你的代码。

对于内置类型而言，`len()` 等操作会非常快，因为它直接读取 `PyVarObject` 结构体中保存的长度信息，所以很高效。

还有一些常用的 Magic Method，在这里列一下：

category | method
-------- | ------
String representation | `__repr__` `__str__` `__bytes__`
Convensition Number | `__abs__` `__bool__` `__hash__`
Collections | `__len__` `__getitem__` `__setitem__` `__delitem__`
Iteration | `__iter__` `__next__`
Callable | `__call__`
Context Manager | `__enter__` `__exit__`
Instance creation | `__new__` `__init__` `__del__`
Attribute management | `__getattr__` `__getattribute__` `__setattr__`
Attribute descriptor | `__get__` `__set__` `__delete__`

## 优先实现 `__repr__`

在 print 时如果发现没有实现 `__str__` 会自动选择 `__repr__`，另外在格式化的时候优先使用 `print('%r')
`，这样的话如果是字符串会显示引号，方便排除 Bug
