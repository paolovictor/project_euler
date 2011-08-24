import math

class MyXRange(object):
    def __init__(self, a1, a2=None, step=1):
        if step == 0:
            raise ValueError("arg 3 must not be 0")
        if a2 is None:
            a1, a2 = 0, a1
        if (a2 - a1) % step != 0:
            a2 += step - (a2 - a1) % step
        if cmp(a1, a2) != cmp(0, step):
            a2 = a1
        self.start, self.stop, self.step = a1, a2, step

    def __iter__(self):
        n = self.start
        while cmp(n, self.stop) == cmp(0, self.step):
            yield n
            n += self.step

    def __repr__(self):
        return "MyXRange(%d,%d,%d)" % (self.start, self.stop, self.step)

    # NB: len(self) will convert this to an int, and may fail
    def __len__(self):
        return (self.stop - self.start)//(self.step)

    def __getitem__(self, key):
        if key < 0:
            key = self.__len__() + key
            if key < 0:
                raise IndexError("list index out of range")
            return self[key]
        n = self.start + self.step*key
        if cmp(n, self.stop) != cmp(0, self.step):
            raise IndexError("list index out of range")
        return n

    def __reversed__(self):
        return MyXRange(self.stop-self.step, self.start-self.step, -self.step)

    def __contains__(self, val):
        if val == self.start: return cmp(0, self.step) == cmp(self.start, self.stop)
        if cmp(self.start, val) != cmp(0, self.step): return False
        if cmp(val, self.stop) != cmp(0, self.step): return False
        return (val - self.start) % self.step == 0

def is_prime(n):
    for i in xrange(2, (int)(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def fill_prime_table(n, max_i, table):
    table[1] = True
    for i in MyXRange(2, n):
        print i
        if i in table:
            continue

        table[i] = is_prime(i)
        
        for k in MyXRange(table[i] and (i + i) or i, max_i, i):
            table[k] = False



primes = []

n = 600851475143
#n = 13195
i = 2
while i <= n:
    if i % 1000000 == 0:
        print "[", i, "]"

    if n % i == 0 and is_prime(i):
        primes.append(i)

        n = n / i
        i = 1
        print n
    i += 1
    
print max(primes)
print primes
