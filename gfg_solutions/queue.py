class Queue:

    def __init__(self) -> None:
        self.arr = []

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0

    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.arr[-1]

if __name__ == "__main__":
    my_ob = Queue()
    my_ob.push(1)
    my_ob.push(2)
    my_ob.pop()
    print(my_ob.peek())
    


