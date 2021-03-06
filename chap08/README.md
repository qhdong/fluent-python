# Object Reference

## Python 中的 `==` 和 `is` 

`is` 比较的是两个对象的地址，也就是它们的 `id(obj)` 的结果，看他们是否是一个地址，而 `==` 比较的是对象的内容，
默认的实现是比较地址，跟 `is` 一样，然而大部分实现都会重载，而且 `==` 事实上是 `__eq__` 的一个语法糖。

所以在比较一些单例时可以用 `is` 会比较快，比如 `if obj is None`

## shallow copy & deep copy

Python 集合类默认的拷贝方式是浅拷贝，比如 `l1 = [1, 2]; l2 = list(l1)`

通过 `copy.copy` 和 `copy.deepcopy` 可以支持浅拷贝和深拷贝，其中深拷贝会处理好 **循环引用** 的问题，
另外可以通过自定义 `__copy__()` 和 `__deepcopy__()` 来控制拷贝过程。

## 函数参数传递方式

在 Python 中只有唯一的一种传递参数值的方式，那就是 `call by sharing`，也就是传递引用，在函数内可以改变可变类型的参数值，
但无法替换它，也就是　`id` 无法改变。

```python
def f(a, b):
    a += b
    return a

>>> a, b = 1, 2
>>> f(a, b)
3
>>> a, b
(1, 2)
>>> a, b = [1], [2]
>>> f(a, b)
[1, 2]
>>> a, b
([1, 2], [2])
>>> a, b = (1,), (2,)
>>> f(a, b)
(1, 2)
>>> a, b
>>> ((1,), (2,))
```

## Python　对象删除和垃圾回收

在 Python 中没有删除对象的概念，而是在没有引用可以访问到对象的时候，被 GC 垃圾回收了。

Python 中的垃圾回收算法是　**引用计数**，当一个对象引用计数值为 0 的时候，就会被调用　`__del__` 方法，然后销毁对象。

一般来说，会使用 `weakref.WeakValueDictionary`　等弱引用的集合类，而不是底层应用。

## Python 对象模型

Python 中的每一个对象都有　id, type, value，其中只有　`value`　可以随时间变化，而变量名只不过是一个指向对象的指针而已。