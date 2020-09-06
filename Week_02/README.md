学习笔记

# 哈希表

python中哈希表的引用主要是set 和dict

## python中的set 集合

* set 中的元素是无序的，所以无法通过索引获取
* set一旦创建，set中的元素将无法改变，但可以添加和删除

### 代码实现

```python
set = {"a","b","c"}
```

### 方法

| 方法                                   | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| for x in set                           | 遍历set中的元素                                              |
| x in set                               | 检查 x 是否存在set中                                         |
| set.add(x)                             | 往set中添加元素 x，add方法只能添加一个元素                   |
| set.update(list)                       | 往set中添加list中的元素，list中有多少个元素，就会添加多少个元素 |
| len(set)                               | 获取set 的长度                                               |
| set.remove(x)                          | 从set中删除元素 x，如果x不存在set中，remove会抛出异常        |
| set.discard(x)                         | 从set中删除元素 x，如果x不存在set中，discard不会有任何反应   |
| set.pop()                              | 删除set中的最后一个元素，但是由于set是无序的，所以无法知道会删除哪个元素，pop方法会返回删除的元素 |
| set.clear()                            | 清空set                                                      |
| del set                                | 删除set，set将不存在                                         |
| set1.union(set2)                       | 合并两个set，返回一个新的set                                 |
| set1.update(set2)                      | 将set2中的元素添加到set1中                                   |
| set(tuple)                             | set()方法可以从元组创建set                                   |
| set.copy()                             | 复制set，并返回                                              |
| set1.difference(set2)                  | 返回一个新的set，包含set1中不存在于set2中的元素              |
| set1.difference_update(set2)           | 从set1 中 将存在于set2中的元素删除，没有返回值               |
| set1.intersection(set2)                | 返回一个新的set，包含set1和set2中相同的元素                  |
| set1.intersection_update(set2)         | 从set1中将不存在于set2中的元素删除                           |
| set1.isdisjoint(set2)                  | 如果set1和set2中没有相同的元素，则返回True，否则返回False    |
| set1.issubset(set2)                    | 如果set1中的元素都存在于set2中，则返回True，否则返回False    |
| set1.issuperset(set2)                  | 如果set2中的元素都存在于set1中，则返回True，否则返回False    |
| set1.symmetric_difference(set2)        | 返回一个新的set，包含存在于set1中，但不存在于set2中的元素    |
| set1.symmetric_difference_update(set2) | 不返回，从set1中删除存在于set2中的元素，并往set1中添加set2中不存在于set1中的元素 |

## python中的dict 字典

* dict中的key是不允许重复的
* dict中的key是不可修改的，支持字符串，数字，元组，但是不支持列表

### 代码实现

```python
dict = {"a":1,"b":2}
```

### 方法

| 方法                              | 说明                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| dict[key]                         | 访问dict中key对应的value                                     |
| dict[key]=                        | 修改dict中key对应的value                                     |
| del dict[[key]]                   | 删除dict 中 key = key的元素                                  |
| dict.clear()                      | 清空dict                                                     |
| del dict                          | 删除dict，dict将不存在                                       |
| cmp(dict1,dict2)                  | 比较两个dict，如果元素完全相同，则返回 0，如果dict1 大于 dict2，则返回 1，否则 返回 -1 |
| len(dict)                         | 获取dict的长度                                               |
| dict.copy()                       | 复制dict，并返回                                             |
| dict.fromkeys(seq,value)          | 从seq序列中的元素作为key新建dict，value为key对应的值，没有value，则为None |
| dict.get(key,default=None)        | 查找dict中key对应的value，若key不存在，则返回default值       |
| dict.haskey(key)<br>key in dict   | 判断key在dict中是否存在，返回boolean                         |
| dict.items()                      | 以列表形式返回(key,value)的元组数组                          |
| dict.keys()                       | 以列表形式返回dict 的key                                     |
| dict.setdefault(key,default=None) | 查找dict中key对应的value，若key不存在，返回default值，并在dict中新增元素key：default |
| dict1.update(dict2)               | 将dict2中的元素，添加到dict1中                               |
| dict.values()                     | 以列表形式返回dict中的value                                  |
| dict.pop(key,default)             | 根据key删除dict中对应的元素，并返回被删除的value，若没有指定key，返回default值 |
| dict.popitem()                    | 删除dict最后一个元素，并以字典形式返回这个元素               |



# 二叉树

## 树节点的定义

python代码

```python
class TreeNode:
  def __int__(self,val):
    self.val = val
    self.left,self.right = None,None
```

## 树的遍历

### 前序遍历

根-左-右

```python
def preorder(self,root):
  if root:
    self.traverse_path.append(root.val)
    self.preorder(root.left)
    self.preorder(root.right)
```



### 中序遍历

左-根-右

```python
def inorder(self,root):
  if root:
    self.inorder(root.left)
    self.traverse_path.append(root.val)
    self.inorder(root.right)
```



### 后序遍历

左-右-根

```python
def postorder(self,root):
  if root:
    self.postorder(root.left)
    self.postorder(root.right)
    self.traverse_path.append(root.val)
```



## 二叉搜索树 Binary 

也叫二叉排序树，有序二叉树 

### 删除节点

1. 若要删除的节点没有子节点，则直接删除
2. 若要删除的节点有子节点，则将大于该节点的最近子节点提上来替换该节点的位置

# 堆 Heap

可以迅速找到一堆数中的最大值或者最小值的数据结构

大顶堆，大根堆：根节点最大的堆

小顶堆，小根堆：根节点最小的堆

## 堆的分类和时间复杂度

| Operation                                                    | find-min     | delete-min                                                   | insert                                                       | decrease-key                                                 | meld                                                         |
| :----------------------------------------------------------- | :----------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Binary](https://en.wikipedia.org/wiki/Binary_heap)[[8\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-CLRS-9) | *Θ*(1)       | *Θ*(log *n*)                                                 | *O*(log *n*)                                                 | *O*(log *n*)                                                 | *Θ*(*n*)                                                     |
| [Leftist](https://en.wikipedia.org/wiki/Leftist_tree)        | *Θ*(1)       | *Θ*(log *n*)                                                 | *Θ*(log *n*)                                                 | *O*(log *n*)                                                 | *Θ*(log *n*)                                                 |
| [Binomial](https://en.wikipedia.org/wiki/Binomial_heap)[[8\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-CLRS-9)[[9\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-10) | *Θ*(1)       | *Θ*(log *n*)                                                 | *Θ*(1)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(log *n*)                                                 | *O*(log *n*)[[c\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-meld-12) |
| [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_heap)[[8\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-CLRS-9)[[10\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-Fredman_And_Tarjan-13) | *Θ*(1)       | *O*(log *n*)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(1)                                                       | *Θ*(1)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(1)                                                       |
| [Pairing](https://en.wikipedia.org/wiki/Pairing_heap)[[11\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-Iacono-14) | *Θ*(1)       | *O*(log *n*)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(1)                                                       | *o*(log *n*)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11)[[d\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-pairingdecreasekey-17) | *Θ*(1)                                                       |
| [Brodal](https://en.wikipedia.org/wiki/Brodal_queue)[[14\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-18)[[e\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-brodal-20) | *Θ*(1)       | *O*(log *n*)                                                 | *Θ*(1)                                                       | *Θ*(1)                                                       | *Θ*(1)                                                       |
| [Rank-pairing](https://en.wikipedia.org/w/index.php?title=Rank-pairing_heap&action=edit&redlink=1)[[16\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-21) | *Θ*(1)       | *O*(log *n*)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(1)                                                       | *Θ*(1)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(1)                                                       |
| [Strict Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_heap)[[17\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-22) | *Θ*(1)       | *O*(log *n*)                                                 | *Θ*(1)                                                       | *Θ*(1)                                                       | *Θ*(1)                                                       |
| [2-3 heap](https://en.wikipedia.org/wiki/2-3_heap)[[18\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-23) | *O*(log *n*) | *O*(log *n*)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *O*(log *n*)[[b\]](https://en.wikipedia.org/wiki/Heap_(data_structure)#cite_note-amortized-11) | *Θ*(1)                                                       | *?*                                                          |

## 二叉堆的实现方式

以完全二叉树实现

### 二叉堆（大顶）

1. 完全二叉树
2. 根节点大于它的所有子节点

#### 实现形式

一维数组

最大值索引为 0

根节点索引为 i 时，左儿子的索引为 2i+1，右节点2i+2

子节点索引为 i 时，根节点的索引为 floor((i-1)/2)

#### 查询最大值

最大值即为最顶根节点，所以O(1)可实现

#### 添加元素

1. 将元素添加到堆末尾
2. 从堆末尾往上调整二叉堆：与根节点比较，若大于根节点，则与根节点交换，直到小于根节点位置
3. O(logn)实现

删除最大值

1. 删除最大值
2. 将堆末尾的值放到顶上最大值处
3. 从堆顶向下调整二叉堆：两个子节点比较，与更大的子节点交换，直到堆末尾
4. O(logn)实现

#### python的heapq库

import heapq

| 方法（以下方法均需以heapq.开头） | 说明                            |
| -------------------------------- | ------------------------------- |
| headpush(heap,x)                 | 往小顶堆heap中添加元素 x        |
| heappop(heap)                    | 从heap中弹出最小值并返回        |
| heapify(list)                    | 让列表具备小顶堆的特征          |
| heapreplace(heap,x)              | 从heap中弹出最小值，并添加元素x |
| nlargest(n,list)                 | 列表形式返回 list中的n个最大值  |
| nsmallest(n,list)                | 列表形式返回 list中的n个最小值  |



# 图 graph

有点，有边就是图

数学表示：Graph(V,E)

* V - vertex 点，具备了 2 个属性：
  * 度：即点连接的边数量，如果边的方向是指向这个点的，称为入度；若边是从这个点出去的，称为出度
  * 点与点之间：连通与否
* E - edge 边，具备了 2 个属性：
  * 有向和无向
  * 权重：可以理解为边的长度，或边的损耗（经过这个边需要消耗剁手）

## 图的实现

* 邻接矩阵
  1. 行索引和列索引都表示点的下标
  2. 矩阵中的值表示行的点走向列的点之间的边：
     1. 权重属性：
        1. 有权重的边，则为权重
        2. 没有权重的边，则为 1
        3. 没有连接的边，则为 0
     2. 方向属性：
        1. 若边是无向的，则(0,1)(1,0)都是 1
        2. 若边是有向的，如 0 -> 1，则(0,1)是 1，(1,0)是 0
* 邻接表
  1. 最左边的数字表示点
  2. 每一行为与第一个点相连接的点

## 图的算法

### DFS - 递归写法

```python
visited = set() #树的DFS可以不加这一行，但是图一定要加，因为树的节点不会重复，但是图可能会

def dfs(node,visited):
  if node in visited: #terminator
    return
  visited.add(node)
  for next_node in node.children():
    if not next_node in visited:
      dfs(next_node,visited)
```

### BFS

```python
def bfs(graph,start,end):
  queue = []
  queue.append([start])
  visited = set()
  while queue:
    node = queue.pop()
    visited.add(node)
    process(node)
    nodes=generate_related_nodes(node)
    queue.push(nodes)
```

