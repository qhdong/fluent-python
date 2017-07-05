# -*- coding: utf-8 -*-
def tag(name, *content, cls=None, **attrs):
    if cls:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (key, val)
                           for key, val in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(tag('p', 'hello', 'world', cls='person', id=123))
    print(tag(name='img', cls='student', id='jake', size='100px'))
