---
layout: post
title: Linked Lists
---


## The basic  
There are some common operations/techniques on linked lists that you have to know about. Many problems require you to use one or more of them to solve.  

Here the node for a linked list in Python is as follows.[^1]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
```


### Reverse a linked list
To reverse a linked list, you can use three pointers like this:

```python
def reverse(root):
  """
  reverse a linked list with three pointers.
  root, new_root and next
  """
  new_root = None
  while root:
    nextNode = root.next
    root.next = new_root
    new_root = root
    root = nextNode
  return new_root
```

### Fast pointer, slower pointer
By using two pointers, you can do a variety of things. For example, you can find the middle node in the list, detect cycle and find the last to `k` node.



[^1] This is taken from [leetcode.com](https://oj.leetcode.com/)
