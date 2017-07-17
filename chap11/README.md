# interfaces & protocols

在 Python 中，interface 可以理解为一些公共方法的集合，`xx like object`, `xx interface`, `xx protocol` 可以理解为一个东西。

# duck typing

由于 duck typing 的存在， Python 可以非常灵活的使用和对待类型，这样做确实很方便，前提是你知道你在做什么。
类似的静态语言强类型的比如 Java 在这方面就要严格的多，当然也带来了安全性的提升。

有了 duck typing 之后，在代码中直接使用 `isinstance(obj, cls)`　并不是一件好事，但是如果配合　`ABC`　使用，那就说的过去了。

# virtual subclass

我们可以将一个类注册为　`ABC`　的　**虚拟子类**，这样做可以让解释器相信我们定义的类继承了　`ABC`　类，并不再做相应的检查，
如果我们撒谎没有实现相应的方法，那么有可能在运行时调用该方法是抛出异常。

需要注意的是，通过 `ABC.register(cls)`　注册的虚拟子类并没有真的继承父类的方法和属性，但是可以通过　`issubclass()` 和　`isinstance()`　的检查。

这一点可以通过　`cls.__mro__`　来验证。

# 语言的强类型与弱类型

* 如果一门语言很少做隐式类型转换，那它就是强类型，反之是弱类型，比如 `JavaScript, PHP`
* 如果类型检查发生在编译时期，那它是静态类型，否则就是动态类型

所以　Python 是一门　*强类型、动态*　编程语言。