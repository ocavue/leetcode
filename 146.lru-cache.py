"""
submits:
  - date: 2020-04-12
    cheating: false
"""

#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (30.10%)
# Likes:    4900
# Dislikes: 217
# Total Accepted:    461.5K
# Total Submissions: 1.5M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' + '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the LEAST RECENTLY
# USED ITEM before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#
#
#

# @lc code=start
from queue import Queue
from typing import Union
import heapq


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return "<Node {}:{} prev={} next={}>".format(
            self.key, self.value, self.prev, self.next
        )


class DoubleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def remove(self, node: Node):
        # One interesting property about double linked list is that the node can remove itself without other reference.
        if node.prev:
            node.prev.next = node.next
        else:
            self.start = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev

        self.length -= 1

    def append(self, node: Node):
        """append a node at the end of linked list"""
        if self.length == 0:
            node.prev = node.next = None
            self.start = self.end = node
        else:
            self.end.next = node
            node.next = None
            node.prev = self.end
            self.end = node
        self.length += 1


class LRUCache:
    def __init__(self, capacity: int):
        self.node_map = {}
        self.linked_list = DoubleLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.linked_list.remove(node)
            self.linked_list.append(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) > -1:
            self.node_map[key].value = value
        else:
            node = Node(key, value)
            self.linked_list.append(node)
            self.node_map[key] = node
            if self.linked_list.length > self.capacity:
                to_remove_node = self.linked_list.start
                self.linked_list.remove(to_remove_node)
                del self.node_map[to_remove_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == "__main__":
    # fmt: off

    cache = LRUCache(2)

    assert cache.put(1, 1) == None
    assert cache.linked_list.length == 1
    assert cache.put(2, 2) == None
    assert cache.linked_list.length == 2
    assert cache.get(1)    == 1         # returns 1
    assert cache.put(3, 3) == None      # evicts key 2
    assert cache.linked_list.length == 2
    assert cache.get(2)    == -1        # returns -1 (not found)
    assert cache.put(4, 4) == None      # evicts key 1
    assert cache.get(1)    == -1        # returns -1 (not found)
    assert cache.get(3)    == 3         # returns 3
    assert cache.get(4)    == 4         # returns 4
    # fmt: on

    for action, value in zip(
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]],
    ):
        print('runing', action, *value)
        if action == "LRUCache":
            cache = LRUCache(*value)
        elif action == "get":
            cache.get(*value)
        elif action == "put":
            cache.put(*value)
        else:
            raise Exception("unknow action")
