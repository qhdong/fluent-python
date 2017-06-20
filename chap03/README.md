# Map 类型

可以使用 `types.MappingProxyType` 来做字段的只读映射

# Set 

使用列表生成式产生 set 要比使用 constructor 快，因为解释器会使用特殊的 BUILD_SET 指令。

set 的内容必须为 `hashable`，而 set 本身并不是 hashable 的，所以如果需要生成嵌套的 set，
需要使用 `fronzenset`