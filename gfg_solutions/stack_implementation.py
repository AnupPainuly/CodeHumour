class Stack():
    
    def __init__(self):
        self.arr = []

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        if not self.isEmpty():
            self.arr.pop()
        else:
            print("stack is empty")

    def isEmpty(self):
        return len(self.arr) == 0

    def peek(self):
        if not self.isEmpty():
            return self.arr[-1]
        else:
            print("stack is empty")

if __name__ == "__main__":
    my_stack_ob = Stack()
    my_stack_ob.push(1)
    my_stack_ob.push(2)
    my_stack_ob.pop()
    print(my_stack_ob.peek())





