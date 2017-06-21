# Text and Bytes

## Bytes

- Python3 中的 bytes 是只读的，而`bytearray` 是可读写的。
- 使用 bytes 和 bytearray 从 buffer-like 对象构建时会复制数据，而使用 `memoryview` 可以避免复制。
- UTF-16 等编码会将一个字符编码为多个字节，所以需要在文件头加上 BOM 表示字节顺序，而 UTF-8 不需要

注意，你无法通过 bytes 来 100% 推测它使用什么编码，不过可以根据人类语言的统计特性来做出推测，这方面已经有成熟的包 `chardet` 
完成这项工作了。在 `requests` 中也有使用。

在 open 的时候永远手动指定 `encoding` 避免因为系统环境不同造成的默认编码不同而引发 bug，
默认使用的编码是 `locale.getpreferredencoding()`