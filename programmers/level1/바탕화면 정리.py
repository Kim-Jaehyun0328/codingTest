def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, 0, 0
    flag = False

    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            lux = i
            break

    for i in range(len(wallpaper) - 1, -1, -1):
        if "#" in wallpaper[i]:
            rdx = i + 1
            break

    for j in range(len(wallpaper[0])):
        for i in range(len(wallpaper)):
            if wallpaper[i][j] == "#":
                luy = j
                flag = True
                break
        if flag == True:
            flag = False
            break

    for j in range(len(wallpaper[0]) - 1, -1, -1):
        for i in range(len(wallpaper)):
            if wallpaper[i][j] == "#":
                rdy = j + 1
                flag = True
                break
        if flag == True:
            flag = False
            break


    return [lux, luy, rdx, rdy]
print(solution([".#...", "..#..", "...#."]))