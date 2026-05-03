# Linked List Notes

## 链表基础

### 概念

链表是由一系列节点组成的线性数据结构，每个节点包含**数据域**和**指针域**。与数组不同，链表在内存中不连续存储，因此随机访问代价高，但头部插入/删除代价低。

### 类型

| 类型                | 特点                             |
| ------------------- | -------------------------------- |
| 单向链表 (Singly)   | 每个节点只有 `next` 指针         |
| 双向链表 (Doubly)   | 每个节点有 `prev` 和 `next` 指针 |
| 循环链表 (Circular) | 尾节点的 `next` 指向头节点       |

LeetCode 中绝大多数题目使用**单向链表**。

### Python 实现

LeetCode 标准节点定义：

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 常用操作

#### 遍历

```python
curr = head
while curr:
    print(curr.val)
    curr = curr.next
```

#### 虚拟头节点 (Dummy Head)

在头部插入或删除时，用 dummy 节点可以统一处理，避免单独判断 `head` 是否为空：

```python
dummy = ListNode(0)
dummy.next = head
# 操作结束后
return dummy.next
```

#### 在指定节点之后插入

```python
new_node.next = prev.next
prev.next = new_node
```

#### 删除指定节点（需知道前驱节点）

```python
prev.next = prev.next.next
```

#### 在尾部追加

```python
curr = head
while curr.next:
    curr = curr.next
curr.next = new_node
```

### 复杂度对比

| 操作          | 数组      | 链表                   |
| ------------- | --------- | ---------------------- |
| 随机访问      | O(1)      | O(n)                   |
| 头部插入/删除 | O(n)      | O(1)                   |
| 尾部追加      | O(1) 均摊 | O(n)                   |
| 中间插入/删除 | O(n)      | O(1)（需已知前驱节点） |

---

## 链表常用技巧总结

### 快慢指针

快慢指针通常用于链表中的"定位"问题。`slow` 每次走一步，`fast` 每次走两步。

常见用途：

- 找链表中点（876）
- 判断链表是否有环（141）
- 找环的入口（142）

核心思想：利用**速度差**，当 `fast` 到达链表末尾时，`slow` 恰好在中间位置。

> **注意：找中点时的奇偶行为**
>
> 以下初始化方式，当链表长度为偶数时，`slow` 停在**前半段最后一个节点**（常用于回文链表）：
>
> ```python
> slow, fast = head, head
> while fast.next and fast.next.next:
>     slow = slow.next
>     fast = fast.next.next
> # slow 在前半段末尾
> ```
>
> 若改为 `while fast and fast.next`，则偶数长度时 `slow` 停在**后半段第一个节点**。

---

### 前后双指针（固定间距）

与快慢指针不同，前后双指针的两个指针**速度相同**，但保持固定的间距 k。

常见用途：

- 寻找倒数第 k 个节点（19）
- 删除倒数第 k 个节点

核心思路：让 `fast` 先走 k 步，然后 `slow` 和 `fast` 同步前进，当 `fast` 到达末尾时，`slow` 正好在倒数第 k 个位置。

```python
fast = head
for _ in range(k):
    fast = fast.next

slow = head
while fast:
    slow = slow.next
    fast = fast.next
# slow 即为倒数第 k 个节点
```

---

### 头插法

头插法通常用于链表中的"反转"问题。每次取出当前节点，把它插到新链表的头部。

常见用途：

- 反转整个链表
- 反转链表的一部分
- K 个一组反转链表

核心代码：

```python
nxt = curr.next
curr.next = dummy.next
dummy.next = curr
curr = nxt
```

---

### 回文链表中的组合使用

判断回文链表时，可以把这两个技巧结合起来：

1. 用快慢指针找到链表中点（slow 停在前半段末尾）
2. 从 `slow.next` 开始反转后半段
3. 比较前半段和反转后的后半段（以后半段指针为空作为终止条件）

> **注意**：如需保持原链表结构，比较完后应将后半段再次反转还原。LeetCode 上大多数题目不要求还原，但面试时最好主动提及。

---

### 总结

| 技巧       | 核心机制               | 负责           | 典型题目      |
| ---------- | ---------------------- | -------------- | ------------- |
| 快慢指针   | 速度差（1步 vs 2步）   | 找中点、判断环 | 141, 142, 876 |
| 前后双指针 | 固定间距 k，同速前进   | 找倒数第 k 个  | 19            |
| 头插法     | 节点依次插到新链表头部 | 反转结构       | 206, 25, 234  |
