
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

#a testin function
def main():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.peek())
    print(q.pop())
    print(q.pop())

    d = Queue()
    print(d.peek())
    print(d.pop())

if __name__ == "__main__":
    main()

    