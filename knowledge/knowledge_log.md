1. for ... else ... 循环
```python
for i in s:     # 遍历循环s
    if i == 'a':    # 如果 s 中包含a元素，那么返回True
        return True
else:               # 如果遍历完，没有，那么返回False
    return false
```
2. str,list切片
> s[::-1]      反转字符串或者列表
```python
l=[1,2,3,4,5]
print(l[::-1])      # 输出结果  [5, 4, 3, 2, 1]
s='123245'
print(s[::-1])      # 输出结果'542321'
```
>s[:0:-1]   从index为1的位置开始反转
```python
l=[1,2,3,4,5]
print(l[:0:-1])      # 输出结果  [5,4, 3, 2]
s='123245'
print(s[:0:-1])      # 输出结果'54232'
```
