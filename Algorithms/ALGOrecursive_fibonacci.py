class Fibonacci():

    def __init__(self):
        pass

    def recursive(self, n):
        if n < 2:
            return n
        return self.recursive(n-1) + self.recursive(n-2)
        
    def iterative(self, n):
        i = 0
        a,b = 0,1
        while i < n: 
            a,b = b,a+b
            i += 1
        return a

    def dynamic(self,n):
        a,b = 1,1
        for _ in range(n):
            yield a
            a,b = b,a+b
        return result

if __name__ == "__main__":
    f = Fibonacci()
    print(f.recursive(6))
    print(f.iterative(6))

    result = []
    for x in f.dynamic(6):
        result.append(x)
    print(result)