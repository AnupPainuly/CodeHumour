class VendingMachine:

    def __init__(self):
        self.items, self.unit = map(int, input().split(" "))

    def buy(self, item, curr):
        return curr - item*self.unit

ob = VendingMachine()
trans = int(input())
count = 0
while count < trans:
    item, curr = map(int, input().split(" "))
    foo = ob.buy(item, curr)
    print(foo)
    count += 1
