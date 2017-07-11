# Python 中的 protected 和　private 对象属性

在 Python 中，没有语法方面的支持，只有大家约定俗成的规矩，`_protected_var` 和　`__private_var`，
对于前者，在　Python 解释器看来没有任何区别，而后者会将其命名替换为　`_Classname__private_var`　存储在 
`__dict__`　中。

有一个例外，那就是　`from module import *`　的时候，该模块中 `_obj`　不会被导入，也就是说有下划线的模块不会被导入，
当然也可以手动导入，　`from module import _var`

Python 中的私有属性提供的是　safety 而不是　security，也就是说防止你无意的访问不该访问的东西，而不是彻底阻止你访问。
这点不同于 Java　的访问属性，它是强制性的，然而后者也可以通过　reflection 来访问。

# 使用　__slots__　节省存储空间

Python 默认会在每个对象的　`__dict__`　字典中存储属性，然而由于哈希表的存储特性，导致如果你有很多个对象的时候，内存开销将会很大。

为了解决内存开销问题，Python 支持在类中定义　`__slots__`　属性，在其中指明属性，所有实例的属性将会存储在　`tuple
`　中，速度和存储开销都会更好。

当然因为属性存储在 `tuple`　中，所以对象不能再定义新的属性，这是一个副作用，所以最好不要为了限制用户的使用而用 `__slots__`

`__slots__`　并不会被继承，只跟当前类中的定义有关。



