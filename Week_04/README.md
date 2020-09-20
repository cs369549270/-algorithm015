学习笔记 / 学习总结

### 深度优先搜索

#### 示例代码

* 递归写法

```python
def dfs(node,visited):
    if node in visited:
        return
    visited.add(node)
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node,visited)
```

* 非递归写法

```python
def dfs(self,tree):
    if tree.root is None:
        return []
    visited,stack = [],[tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
```

### 广度优先

#### 示例代码

```python
def bfs(graph,start,end):
    visited = set()
    queue = []
    queue.append([start])
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```

### 贪心算法
在每一步选择中都采取在当前状态下的最优解，从而导致全局最优解的算法

* 适用范围
求最优解，解决一些要求结果不特别精确的问题

* 区别与动态规划

贪心：在当下做出局部最优判断，无法回退
动态规划：保存以前的结果，可以进行回退

### 二分查找
前提条件：
1. 单调性：递增或递减
2. 存在上下界
3. 能够通过索引访问

#### 代码模版

```python
left,right = 0,len(array)-1
while left <= right:
    mid = (left+right)/2
    if array[mid] == target:
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```