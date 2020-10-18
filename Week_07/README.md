学习笔记

# 字典树 Trie

## 基本性质

* 节点不存储任何单词
* 单词是从路径上获取的，从根节点到某一节点的路径上的单词连接起来，才是该节点对应的单词/字符串
* 每个节点的所有子节点路径代表的字符都不相同

## 节点可以存储额外信息

## python字典树的实现

```python
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self,word):
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end_of_word] = self.end_of_word
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in word:
                return False
            node = node[char]
        return self.end_of_word in node
    
    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```

# 并查集

```python
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```