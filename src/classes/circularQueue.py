from queue import Empty


class CircularQueue:
    capacity = 10;

    def __init__(self):
        self.data = [None] * self.capacity;
        self.size = 0;
        self.first = -1;
        self.last = -1;

    def __len__(self):
        return self.size;

    def is_empty(self):
        return self.size == 0;

    def first(self):
        if self.is_empty():
            raise Empty("Empty queue");
        return self.data[self.first];

    def enqueue(self, value):
        if self.size < 10:
            if self.size == 0:
                self.first = 0;
                self.last = 0;
            else:
                self.last += 1;
                self.last = self.last % 10;

            self.data[self.last] = value;
            self.size += 1;

        else:
            print("The queue is full.");

    def dequeue(self):
        if self.size > 0:
            self.data.pop(self.first)
            self.size -= 1;
            self.last -= 1;
            self.data.append(None);

        else:
            print("The queue is empty;");
