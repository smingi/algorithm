# 백준 2527_직사각형

for _ in range(4):
    sx, sy, sp, sq, lx, ly, lp, lq = map(int, input().split())

    if sp < lx or lp < sx or lq < sy or sq < ly:
        print("d")

    elif (sp == lx and sy == lq) or (sp == lx and sq == ly) or (sx == lp and sy == lq) or (sx == lp and sq == ly):
        print("c")

    elif (sp == lx) or (sx == lp) or (sy == lq) or (sq == ly):
        print("b")

    else:
        print("a")
