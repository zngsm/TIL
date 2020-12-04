import sys; sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. N 개 중 N // 2 개를 뽑기 <- 한쪽을 구하면 자동으로 나머지 조합은 결정된다.

    # 2. 해당 N // 2 개로 구성된 부분집합들 2개씩 뽑는 순열

    # 3. 순열대로 arr의 인덱스를 뽑아 total 합산하기

    # 4. 각각 합산한 값의 차이를 구해, 차이가 최소값이 되는 게 ans

    print('#{} {}'.format(tc, arr))