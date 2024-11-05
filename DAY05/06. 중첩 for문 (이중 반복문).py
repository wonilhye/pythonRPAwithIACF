matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # 행별로 줄 바꿈
# 출력:
# 1 2 3
# 4 5 6
# 7 8 9
