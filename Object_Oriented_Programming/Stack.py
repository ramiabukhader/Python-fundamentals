#Last In First Out, opposite to Queue
# the most use of the stack is parsing parentheses
# Simple parsing task is to check wether a string of parentheses are matching

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def fullStack(self):
        return self.items

stack = Stack()

# print("Current Stack: " , stack.fullStack())

# print("Stack Empty?" , stack.isEmpty())

# print("push integer 1")
# stack.push(1)
# print("Current Stack: " , stack.fullStack())
# print("Stack Empty?" , stack.isEmpty())

# stack.push(3)
# stack.push(4)
# print("Current Stack", stack.fullStack())

# print("Popped Item", stack.pop())
# print("Element at the top of the stack: ", stack.peek())
# print("Current Stack: " , stack.fullStack())



def checkParenthis(str):
    stack = Stack()
    pushChars, popChars = "<({[" , ">)}]"
    for c in str:
        if c in pushChars:
            stack.push(c)

        elif c in popChars:
            if stack.isEmpty():
                return False
            else:
                stackTop = stack.pop() # pop out first elemetn of the stack but last element from list
                balancingbrackets = pushChars[popChars.index(c)]
                if stackTop != balancingbrackets:
                    return False
                else:
                    return True
        else:
            return False
        
    return not stack.isEmpty()

print(checkParenthis("()("))