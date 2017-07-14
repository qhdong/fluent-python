## Python 中的接口

在 Python 中并没有像 Java 的 `interface` 那样明确表示接口的关键词，但是接口的概念仍然存在，
一般称之为 `Protocol`，也就是在文档中约定的，而不是在代码里限制，一般遵循某个协议就是指包含一些指定的方法实现，
比如 `sequence protocol` 就是指实现了 `__len__` 和 `__getitem__` 这两个方法。

## Python 中 slice 的原理

当我们使用 `a[1:2]` 的时候，到底发生了什么呢？可以通过一段简单的代码来演示一下

```python
class MySlice:
    def __getitem__(self, item):
        return item


>>> s = MySlice()
>>> s[1:-1, 2]
(slice(1, -1, None), slice(2, None, -1))
```

可以看出，其实这里的切片就是一个语法糖，Python 会帮你转换为 `slice` 内置对象。

