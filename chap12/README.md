# 继承

尽量不要直接继承　`list, dict`　等内置类，因为内置类通常会忽略用户重载的方法，可以从　`collections.UserDict` 继承。
出现这个问题的原因主要是 `CPython` 实现这些内置类的特定方式。

