学习笔记

> 动态规划和递归或者分治没有根本上的区别（关键看有无最优的子结构）
> 共性：找到重复子问题
> 差异性：最优子结构/中途可以淘汰次优解

#### 使用lru cache处理斐波那契数列问题

```python
# 直接使用装饰器调用lru cache
@lru_cache()
def fib(n):
    return n if n==0 or n==1 else fib(n-1)+fib(n-2)
```

#### 装饰器

使用装饰器可以定义函数中需要被重复利用的部分，如下述计算add函数和sub函数的运行时间

```python
import time
def add(a,b):
    start_time = time.time()
    res = a+b
    execute_time = time.time()-start_time
    print(execute_time)
    return res

def sub(a,b):
    start_time = time.time()
    res = a+b
    execute_time = time.time()-start_time
    print(execute_time)
    return res
```

可以通过装饰器将计算时间的部分定义

```python
import time

# 定义装饰器
def time_execute(f):
    def wrapper(*args,**kargs):
        start_time = time.time()
        res = f(*args,**kargs)
        execute_time = time.time()-start_time
        print(execute_time)
        return res
    return wrapper

@time_execute()
def add(a,b):
    return a+b

@time_execute()
def sub(a,b):
    return a-b

```

