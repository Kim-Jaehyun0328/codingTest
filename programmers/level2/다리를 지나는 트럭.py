from collections import deque

def solution(bridge_length, weight, truck_weights):
    length = len(truck_weights)
    answer = 0
    truck_weights = deque(truck_weights)
    done = []
    ing = deque()
    time = deque()
    while True:
        if len(done) == length:
            break
        if time and time[0] == bridge_length:
            time.popleft()
            done_truck = ing.popleft()
            done.append(done_truck)

        if len(ing) < bridge_length and truck_weights and sum(ing) + truck_weights[0] <= weight:
            temp = truck_weights.popleft()
            ing.append(temp)
            time.append(0)

        for i in range(len(time)):
            time[i] += 1

        answer += 1
    return answer

print(solution(2,10,[7,4,5,6]))
