"""


4x4격자에서 복제 연습

격자 안에 물고기M 마리 , 각자 이동방향 가짐

상어도 격자에들어가있음

둘 이상 물고기 or 상어가 같은 칸 안에 있을 수도


마법 연습
1. 상어가 복제 마법 -> 5번에서 나타남
2. 모든 물코기가 한 칸 이동 : 상어, 물고기냄새, 벗어나는 칸으론 불가 / 이동할 수 있을 떄까지 반시계 45도 회전
이동할 수 있는칸 없으면 이동 x

3. 상어는 3칸 이동
이동하는 중에 물고기 있으면, 물고기느 제외됨, 물고기 제외되면 물고기냄새 생김
제외되는 물고기 가장 많은 방법으로 이동

4. 두번 전 연습으로 생긴 물고기냄새가 사라짐
물고기냄새 2 로 해놓고 매 연습마다 -1로 하면될듯

5. 물고기 복제 => 1번 상태 물고기 그대로 다시 생기는 듯



"""

M, S = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(M)]  # fx, fx 위치와, d 방향

s_x, s_y = map(int, input().split())  # 상어 위치

# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물고기 냄새 표시
smell = [[0] * 4 for _ in range(4)]


def move_fish(fish):
    global smell
    for ins in fish:


def move_shark(s_x, s_y, fish):


# 상어가 연습
for _ in range(S):

    # 복제를 위해 초기 상태 저장
    copy = fish

    # 물고기 이동
    moved_fish = move_fish(fish)

    # 상어 이동
    s_x, s_y, fish = move_shark(s_x, s_y, fish)

    # 물고기 냄새 없애기
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:
                smell[i][j] -= 1

    # 물고기 복제
    for ins in copy:
        fish.append(ins)

# 정답 출력
print(len(fish))





