import sys; sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 벌들이 쓸 구역을 정하기
    # 한 지점을 선택하면 슬랑이싱해서 해당 줄 다 가져와야함
    # 2. 해당 구역별로 벌의 최대 수획량을 뽑기
    # 한번에 큰 값을 가져오는게 좋다
    # 3. 뽑은 후 제곱하여 total에 합산하기
    # 제일 큰 값이 답
    print('#{} {}'.format(tc, arr))