# Finding the Largeest or Smallest N Items

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3,nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# print(cheap)
# print(expensive)

heap=list(nums)
print(heap)

heapq.heapify(heap) 
# heap[0] is always the smallest
print(heap)

heapq.heappop(heap)
# reordering; the smallest goes to heap[0] with O(logN)
print(heap)

heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)


