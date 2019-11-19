# 3.7以降のフォーマット済み文字リラテルによる書き方
a, b = 'abc', 'def'

# 1
print(f'{a} {b}')

print('#', '-'*9, sep = '')

#2
print('{}{}'.format(a, b))
