"""Meeting one notes."""
from __future__ import annotations  # don't worry about this

from collections import deque


class Node:
    name: str
    children: list[Node]


def breadth_first_search(head: Node) -> list[str]:
    """
    Create a list of node names in breadth-first search.

    Uses a deque as a queue.
    """
    array = []
    queue = deque([head])
    while queue:
        node = queue.popleft()
        for child in node.children:
            queue.append(child)
        array.append(node.name)
    return array


def depth_first_search(head: Node) -> list[str]:
    """
    Create a list of node names in depth-first search.

    Uses a stack, no recursion.
    """
    array = []
    stack = [head]
    while stack:
        node = stack.pop()
        for child in node.children:
            stack.append(child)
        array.append(node.name)
    return array
