def solution(bridge_length: int, weight: int, truck_weight: [int]) -> int:
    bridge: [int] = [0]
    time = bridge_length
    deltalast = 0

    if not(1 <= bridge_length <= 10000 or 1 <= weight <= 10000 or 1 <= len(truck_weight) <= 10000 or 1 <= min(truck_weight) <= weight):
        raise Exception("Invalid input")

    while len(truck_weight) > 0 or len(bridge) > 0:
        if  len(truck_weight) > 0 and sum(bridge) + truck_weight[0] <= weight:
            bridge.append(truck_weight.pop(0))
            time += deltalast
            deltalast = 0
        elif len(truck_weight) > 0 and sum(bridge) + truck_weight[0] > weight:
                deltalast += 1
        if len(bridge) > 0:
            bridge.pop(0)

        time += 1

    return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))