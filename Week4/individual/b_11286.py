import heapq
import sys
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        try:
            print(heap[0][1])
            heapq.heappop(heap)
        except:
            print(0)
            continue
    else:
        heapq.heappush(heap,(abs(a),a))
