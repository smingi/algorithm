# 백준 2869_달팽이는 올라가고 싶다


A, B, V = map(int, input().split())  # A: 낮(올라가는 높이) B: 밤(내려가는 높이) V: 총 높이

day = (V-B) // (A-B)

if (V-B) % (A-B):
    day += 1

print(day)
