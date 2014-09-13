---
layout: post
title: Linked Lists
---


## The basic  
There are some common operations/techniques on linked lists that you have to know about. Many problems require you to use one or more of them to solve.  

Here the node for a linked list in Python is as follows.[^1]

{% highlight python %}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
{% endhighlight %}

### Remove a node
This one is very basic. What you need to do is point the next pointer of the prev node to the next node.  
Like this: `prev.next = prev.next.next`


### Reverse a linked list
To reverse a linked list, you can use three pointers like this:

{% highlight python %}
def reverse(root):
  """
  reverse a linked list with three pointers.
  root, new_root and next
  """
  new_root = None
  while root is not None:
    nextNode = root.next
    root.next = new_root
    new_root = root
    root = nextNode
  return new_root
{% endhighlight %}

### Fast pointer, slower pointer
By using two pointers, you can do a variety of things. For example, you can find the middle node in the list, detect cycle and find the last to `k` node. The `fast` pointer isn't necessarily faster, it might just move before the `slow` one.
#### Find the middle node
{% highlight python %}
def findMid(root):
  """find the middle node of the list
  """
  p = root
  q = root.next
  while q is not None:
    q = q.next
    if q is not None:
      q = q.next
      p = p.next
  
  #return q.next
  # if the linked list needed to be cut in half
  res = q.next
  q.next = None
  return res
{% endhighlight %}

### Merge two sorted linked list

This is a fairly common operation too.
{% highlight python %}
def mergeList(self, a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.val < b.val:
        head = a
    else:
        head = b
        b = a
        a = head
    while a.next is not None and b is not None:
        if a.next.val > b.val:
            tmp = a.next
            a.next = b
            b = tmp
        a = a.next
    if a.next is None:
        a.next = b
    return head
{% endhighlight %}

## Put into use

### Cycle detection


## Footnotes
[^1]: This is taken from [leetcode.com](https://oj.leetcode.com/)
