'''
要求：返回一个 IP 数组，并且按 IP 最后一位排序返回
string = "192.0.0.1？！289.0.0.1！0.0.0.0！192.163.10.28？192.0.0.1”
此题我有一个疑问，IP最后一位只的是4段ip中的最后一位，还是字符串最后一位？
暂时理解成字符串最后一位吧，可能我的第一种理解不正确
'''
line = "192.0.0.1?!289.0.0.1!0.0.0.0!20.163.10.28?192.0.0.9"
import re
import operator
res = re.split(r'[?!]+', line)
# 方法一使用lambda
# res.sort(key=lambda x:x[-1])
# 方法2 使用operator.itemgetter
res.sort(key=operator.itemgetter(-1))

## 注意字符串和数字排序的区别, 注意这里排序的是按照字符串最后一位排序
# sort和sorted都可以这么使用
# 如果是按照ip地址四段中的最后一段排序，那么代码如下：
# res.sort(key= lambda x:int(x.split('.')[-1]))

print(res)