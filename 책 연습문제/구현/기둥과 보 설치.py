def possible(answer):
    for x, y, frame in answer:
        if frame == 0:  # 기둥의 존재 조건
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        elif frame == 1:  # 보의 존재 조건
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame

        if b == 0:  # 삭제일 경우
            answer.remove([x, y, a])
            if not possible(answer):  # 삭제가 가능한 경우
                answer.append([x, y, a])
        elif b == 1:  # 설치일 경우
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])

    return sorted(answer)