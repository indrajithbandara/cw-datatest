#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#一、filter(function, sequence)
#对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple(取决于sequence的类型)返回：

def f(x): 
    return x % 2 != 0 and x % 3 != 0 

print filter(f, range(2, 25)) 
#[5, 7, 11, 13, 17, 19, 23]


def f1(x): 
    return x != 'a' 

print filter(f1, "abcdef") #bcdef 


#二、map(function, sequence)  
#对sequence中的item依次执行function(item)，见执行结果组成一个List返回：

def cube(x): 
    return x*x*x 
print map(cube, range(1, 11)) 
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

def cube1(x): 
    return x + x 
print map(cube1 , "abcde") 
#['aa', 'bb', 'cc', 'dd', 'ee']
 
#另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：
def add(x, y): 
    return x+y 
print map(add, range(8), range(8)) 
#[0, 2, 4, 6, 8, 10, 12, 14]

status_ids = map(lambda x:x.get('status__id'), snaps)

#三、reduce(function, sequence, starting_value)
#对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：
def add(x,y):
    return x + y 
print reduce(add, range(1, 11)) 
#注：1+2+3+4+5+6+7+8+9+10

reduce(add, range(1, 11), 20) 
#注：1+2+3+4+5+6+7+8+9+10+20


#四、lambda
#这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方： 
g = lambda x: x * 2 
print g(3) #6 

print (lambda x: x * 2)(3)  #6

#五、sorted
aa = [
   {'name':'zhangsan', 'price':20.01, 'date':'2015-01-09T01:00:00Z'},
   {'name':'lisi', 'price':10.01, 'date':'2013-01-09T01:00:00Z'},
   {'name':'wangwu', 'price':0.01, 'date':'2012-01-09T01:00:00Z'}
]  
sorted(aa, key=lambda s:s.amount) #对list进行排序
sorted(aa, key=lambda s:s.amount, reverse=True)

#aa = [<Symbol: Symbol object>, <Symbol: Symbol object>, <Symbol: Symbol object>] 
sorted(aa, key=lambda s:s["date"]) #对Symbol对象进行排序，date为Symbol属性
sorted(aa, key=lambda s:s["date"], reverse=True)

#六、for特殊用法
for i in range(4):
    print i

se=[x**2 for x in range(4)]
print se #[0, 1, 4, 9]

se=[x**2 for x in range(10) if not x%2]
print se #[0, 4, 16, 36, 64]