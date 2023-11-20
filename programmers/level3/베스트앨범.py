def solution(genres, plays):
    answer = []
    hash_ = {}
    for i in range(len(genres)):
        hash_[genres[i]] = []

    for i in range(len(plays)):
        hash_[genres[i]].append(plays[i])

    genres_num = len(hash_)

    while hash_:
        max_play = -1e9
        max_genre = ""
        for key, value in hash_.items():
            sum_play = sum(value)
            if sum_play > max_play:
                max_play = sum_play
                max_genre = key
        hash_[max_genre].sort(reverse=True)
        if len(hash_[max_genre]) > 1:
            if hash_[max_genre][0] == hash_[max_genre][1]:
                idx = []
                for i in range(len(plays)):
                    if plays[i] == hash_[max_genre][0]:
                        idx.append(i)
                    if len(idx) == 2:
                        break
                answer.append(idx[0])
                answer.append(idx[1])
            else:
                answer.append(plays.index(hash_[max_genre][0]))
                answer.append(plays.index(hash_[max_genre][1]))
        else:
            answer.append(plays.index(hash_[max_genre][0]))
        hash_.pop(max_genre)

    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
