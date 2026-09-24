"""
155. Min Stack
Difficulty: Medium
https://leetcode.com/problems/min-stack/

──────────────────────────────────────────────────

Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

Implement the MinStack class:

	• MinStack() initializes the stack object.

	• void push(int value) pushes the element value onto the stack.

	• void pop() removes the element on the top of the stack.

	• int top() gets the top element of the stack.

	• int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each
function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

	• -2^31 <= val <= 2^31 - 1

• Methods pop, top and getMin operations will always be called on
non-empty stacks.

	• At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

class MinStack:
    min_val: int
    stack: list[int]

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_val == None:
            self.min_val = value
        else:
            self.min_val = min(self.min_val, value)

    def pop(self) -> None:
        if len(self.stack) == 1:
            self.min_val = None
            self.stack.pop()
        else:
            self.stack.pop()            
            self.min_val = min(self.stack)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    ops = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    args = [[], [-2], [0], [-3], [], [], [], []]
    expected = [None, None, None, None, -3, None, 0, -2]

    obj = None
    for op, arg, exp in zip(ops, args, expected):
        if op == "MinStack":
            obj = MinStack()
            result = None
        else:
            result = getattr(obj, op)(*arg)
        status = "PASS" if result == exp else "FAIL"
        print(f"{status}: {op}{tuple(arg)} -> {result} (expected {exp})")
