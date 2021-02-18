class ZigZag:

    def __init__(self,l1,l2):
        self.que=[l1,l2]

    def next(self):
        v=self.que.pop(0)
        r=v.pop(0)
        if v:
            self.que.append(v)
        return r

    def has_next(self):
        if self.que:
            return True
        return False

z=ZigZag([1,3,5,7,9],[2,4,6,8,10])


while z.has_next():
    print(z.next(),end=" ")