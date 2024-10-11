from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-cnt, val) for val, cnt in Counter(s).items()]
        res = []
        heapq.heapify(heap)

        while heap:
            cnt, char = heapq.heappop(heap)
            if not res or char != res[-1]:
                res.append(char)
                if cnt + 1 != 0:
                    heapq.heappush(heap, (cnt+1, char))
            else:
                if not heap:
                    return ''
                next_cnt, next_char = heapq.heappop(heap)
                res.append(next_char)
                if next_cnt + 1 != 0:
                    heapq.heappush(heap, (next_cnt+1, next_char))
                heapq.heappush(heap, (cnt, char))
        return ''.join(res)