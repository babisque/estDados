from queue import Empty

class CircularQueue:
    capacity = 10;
    data = [None] * capacity;

    def __init__(self):
        self.size = 0;
        self.first = -1;
        self.last = -1;

    def __len__(self):
        return self.size;

    def is_empty(self):
        return self.size == 0;

    def firstQ(self):
        if self.is_empty():
            raise Empty("Fila vazia.");
        return self.data[self.first];

    def dequeue(self):
        if self.size > 0:
            self.data.pop(self.first);
            self.size -= 1;
            self.last -= 1;
            self.data.append(None);

        else:
            print("A fila está vazia.");
            return None;

    def enqueue(self, e):
        if self.size < 10:
            if self.size == 0:
                self.first = 0;
                self.last = 0;
            else:
                self.last += 1;
                self.last = self.last % 10;

            self.data[self.last] = e;
            self.size += 1;

        else:
            print("A fila está cheia.");