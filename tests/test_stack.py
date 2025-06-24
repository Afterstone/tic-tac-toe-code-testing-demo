import pytest

# TDD example for a Stack class

class Stack[T]:
    def __init__(self):
        ...

    def push(self, item: T):
        ...

    def pop(self) -> T:
        ...

    def peek(self) -> T:
        ...

    def is_empty(self) -> bool:
        ...

    def size(self) -> int:
        ...
