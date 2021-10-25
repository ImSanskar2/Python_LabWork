class pk:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name ="+ self.name)
        print("age =" , self.age)
obj1=pk("sanskar",19)
obj1.show()

class MyClass:
  x = 9
p1 = MyClass()
print(p1.x)

class Queue:
  queue = list()
  def addtoq(self, dataval):
      if dataval not in self.queue:
          self.queue.insert(0, dataval)
          return True
      return False

  def size(self):
    return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("One")
TheQueue.addtoq("Two")
print(TheQueue.size())

class Stack:
  def _init_(self):
    self.stack = []
  def add(self, dataval):
    if dataval not in self.stack:
      self.stack.append(dataval)
      return True
    else:
      return False
  def peek(self):
    return self.stack[-1]
AStack = Stack()
AStack.add("One")
AStack.add("Two")
AStack.peek()
print(AStack.peek())
AStack.add("Three")
print(AStack.peek())
