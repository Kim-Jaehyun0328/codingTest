# def solution(book_time):
#     last = []
#     book_time.sort()

#     for book in book_time:
#         start_hour, start_minute = book[0].split(":")
#         end_hour, end_minute = book[1].split(":")

#         start = int(start_hour) * 60 + int(start_minute)
#         end = int(end_hour) * 60 + int(end_minute)

#         if last and min(last) <= start:
#             last[last.index(min(last))] = end + 10
#         else:
#             last.append(end + 10) #10분 뒤 가능하니까


#     return len(last)
from heapq import heappop, heappush


def solution(book_time):
    answer = 1

    # "HH:MM" → HH * 60 + MM
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()

    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap, e + 10)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e + 10)

    print(heap)

    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	))