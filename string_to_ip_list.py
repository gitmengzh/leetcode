'''
要求：返回一个 IP 数组，并且按 IP 最后一位排序返回
string = "192.0.0.1？！289.0.0.1！0.0.0.0！192.163.10.28？192.0.0.1”
'''
line = "192.0.0.1?!289.0.0.1!0.0.0.0!20.163.10.28?192.0.0.9"
import re
import operator
res = re.split(r'[?!]+', line)
# L.sort(key=operator.itemgetter())


# res.sort(key=operator.itemgetter())
res.sort(key=lambda x:x.split('.')[-1])
# res.sort(key=lambda x:x[-1])
# print(res)
# a  = '192.163.10.28'
s = []
a = ['192.0.0.1', '211.0.0.29', '0.0.0.291', '192.163.10.8', '192.0.0.1']

for i in a:
    j = lambda a:a.split('.')[-1]
    s.append(j(i))
# b = lambda x:a[-2].split('.')[-1]
# a.sort(key=lambda x:int(x.split('.')[-1]))
print(sorted(s,key=lambda x:x[-1]))
['192.0.0.1', '289.0.0.1', '0.0.0.0', '192.163.10.28', '192.0.0.1']
['0.0.0.0', '192.0.0.1', '289.0.0.1', '192.0.0.1', '192.163.10.28']
['1', '29', '291', '28', '1']
['192.0.0.1', '192.0.0.1', '192.163.10.28', '0.0.0.291', '211.0.0.9']
## 注意字符串和数字排序的区别