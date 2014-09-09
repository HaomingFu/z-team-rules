import heapq

def heapsort(l):
    #heapq.heapify(l)
    h = []
    for v in l:
        heapq.heappush(h, v)
    return [heapq.heappop(h) for i in range(len(h))]

def test():
    print(heapsort([1, 4, 8, 5, 7, 2, 3]))

test()
