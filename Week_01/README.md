

学习笔记

### 时间复杂度和空间复杂度

#### 表示法

Big O notation

表示程序的执行次数

#### 常见的 7 种时间复杂度

1. O(1) : Constant Complexity 常数复杂度

   常数复杂度统一表示位 O(1)

2. O(log n) : Logatithmic Complexity 对数复杂度

3. O(n) : Linear Complexity 线性时间复杂度

4. O(n^2) : N square Complexity 平方

5. O(n^3) : N cubic Complexity 立方

6. O(2^n) : Exponential Growth 指数

7. O(n!) : Factorial 阶乘

#### 主定理Master Theorem ——计算递归的时间复杂度

1. 二分查找（有序的一维数组）

O(log n)

2. 二叉树的遍历

O(n)

二叉树每个节点仅访问一次，所以时间复杂度取决于二叉树的总节点数

3. 二维有序矩阵 查找

O(n)

4. 归并排序（Merge sort)

O(nlog n)

#### 空间复杂度

1. 数组的长度
2. 递归的深度
3. 若递归中又开了数组，则两者中的最大值就是空间复杂度

### 数组、链表、跳表

#### 数组 Array

##### 泛型

对数组中元素的数据类型没有要求，指数组中可以包含任意数据类型的元素

##### 内存管理器

内存管理器给数组中的每个值定义一个地址，访问数组中的元素，则访问特定地址的数据，时间复杂度是O(1)

##### 时间复杂度

1. prepend（插入到第一位）：O(1)
2. append（插入到最后一位）：O(1)
3. lookup（查询）：O(1)
4. insert（插入到某一位）：O(n)
5. delete（删除）：O(n)

#### 链表 Linked list

链表中每个元素都是一个class ，称为node。

每个node包含value 和 next指针。value可以包含任意数据类型，next 指针指向下一位的元素，next 指针可以是双向的，这种称为双向链表。

第一个node称为head，最后一个node称为tail。

##### 时间复杂度

1. prepend（插入到第一位）：O(1)
2. append（插入到最后一位）：O(1)
3. lookup（查询）：O(n)
4. insert（插入到某一位）：O(1)
5. delete（删除）：O(1)

#### 跳表 Skip list

##### 使用跳表的条件

数组必须是有序的

##### 跳表的原理

在原本的链表上增加第一级索引，第一级索引指向next next 元素；再往上建立第二级索引，指向第一级索引的next next 元素...以此类推。

查询某个元素时，先从最大级的索引开始查询，若查询不到，则从范围的最小值开始往下查询下一级索引，直至找到目标元素

##### 跳表工程中的应用

LRU cache 缓存机制

Redis

##### 时间复杂度

lookup：O(log n)

##### 空间复杂度

O(n)

##### 跳表的增删

每次跳表的增删，都需要更新索引。

### 栈、队列、优先队列、双端队列

#### 栈 Stack

##### 关键点

* 先进后出 First In Last Out (FILO)
* 时间复杂度
  * 增加：O(1)
  * 删除：O(1)
  * 查询：O(n)，因为栈里的元素是无序的

##### python 中的实现

用 list 实现栈，栈的 top 元素 为 list[-1] ，base 元素为 list[0]

```python
class Stack:
    def __init__(self):
         self.items = []
 
     def isEmpty(self):
         # 判断是否为空
         return self.items == []
 
     def push(self, item):
         # 压入一个元素，无返回值
         self.items.append(item)
 
     def pop(self):
         # 弹出一个元素
         return self.items.pop()
 
     def peek(self):
         # 返回top元素，不改变原Stack
         return self.items[len(self.items) - 1]
 
     def size(self):
         # 返回Stack的大小
         return len(self.items)
```

 或者通过引用 `pythonds` 模块来实现

 ``` from pythonds.basic import Stack```

还有一种是队列中的堆栈，见下文

#### 队列 queue

##### 关键点

* 先进先出
* 时间复杂度
  * 增加：O(1)
  * 删除：O(1)
  * 查询：O(n)，因为队列里的元素是无序的

##### python 中的实现

```python
import queue

#创建基本队列
#queue.Queue(maxsize=0)创建一个队列对象（队列容量），若maxsize小于或者等于0，队列大小没有限制
Q=queue.Queue(10)
print(Q)
print(type(Q))

#1.基本方法
print(Q.queue)#查看队列中所有元素
print(Q.qsize())#返回队列的大小
print(Q.empty())#判断队空
print(Q.full())#判断队满

#2.获取队列，0--5
#Queue.put（item，block = True，timeout = None ）将对象放入队列，阻塞调用（block=False抛异常），无等待时间
for i in range(5):
    Q.put(i)
# Queue.put_nowait(item)相当于 put(item, False).


#3.读队列，0--5
#Queue.get(block=True, timeout=None)读出队列的一个元素，阻塞调用，无等待时间
while not Q.empty():
    print(Q.get())
# Queue.get_nowait()相当于get(False).取数据，如果没数据抛queue.Empty异常


#4.另两种涉及等待排队任务的方法
# Queue.task_done()在完成一项工作后，向任务已经完成的队列发送一个信号
# Queue.join()阻止直到队列中的所有项目都被获取并处理。即等到队列为空再执行别的操作
```

##### 优先队列 PriorityQueue

如果数据元素不具有可比性，则可将数据包装在忽略数据项的类中，仅比较优先级编号 

* 时间复杂度
  * 插入：O(1)
  * 取出：O(logn)
* 代码实现

```python
import queue

# queue.PriorityQueue() #优先级

q=queue.PriorityQueue(3) #优先级,优先级用数字表示,数字越小优先级越高
q.put((10,'a'))
q.put((-1,'b'))
q.put((100,'c'))
print(q.get())
print(q.get())
print(q.get())
```

##### 堆栈 LifoQueue

```python
import queue

# queue.LifoQueue() #后进先出->堆栈

q=queue.LifoQueue(3)
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
```

#### 双向队列 Deque

##### 时间复杂度

从头部或尾部插入，或移除都是O(1)

##### python 中的实现

通过引入 collections 模块中的 deque 类

##### 方法

| 方法             | 说明 |
| ---------------- | ---- |
| len(deque)       | 获取deque的长度 |
| element in deque | 判断元素是否存在deque中 |
| deque()          | 创建deque，可以从字符串或列表创建，可添加第二个参数（int）决定创建时只取后几个元素 |
| append()         | 在末尾插入单个元素 |
| appendleft()     | 在开头插入单个元素 |
| pop()            | 删除末尾第一个元素 |
| popleft()        | 删除开头第一个元素 |
| deque[index]     | 根据索引查找元素 |
| extend()         | 在末尾插入多个元素，字符串的话会被按字符拆分成多个元素，插入顺序按照原顺序， 后进的在最末尾 |
|extendleft()|在开头插入多个元素，字符串会被按字符拆分，后进的在最开头|
|clear()|清空deque|
|count(element)|统计deque中element 的个数|




