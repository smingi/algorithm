# 5603. [Professional] 건초더미

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 건초 개수
    hay = [int(input()) for _ in range(n)]
    target = sum(hay)//len(hay) # 맞춰야 되는 평균값
    hay.sort(reverse=True) # 빼는 건초를 앞에 넣은 건초를 뒤에 넣기
    for i in range(len(hay)): # 평균을 0으로 맞추고 넣을 건초 위치를 찾음
        hay[i] -= target
        if hay[i] < 0 and hay[i-1] >= 0:
            m_idx = i # 넣는 건초 순서
    cnt = 0 # 이동횟수
    p_idx = 0 # 빼는 건초 순서
    while hay[-1] != 0 and p_idx < m_idx and m_idx < len(hay): # 빼거나 넣을 건초가 없을 때까지 반복
        temp = hay[p_idx] + hay[m_idx]
        if hay[p_idx] == 0:
            p_idx += 1
            continue
        if hay[m_idx] == 0:
            m_idx += 1
            continue
        if temp >= 0: # 뺄 건초가 넣을 건초보다 많을 때
            cnt += -hay[m_idx]
            hay[p_idx] = temp
            hay[m_idx] = 0
            m_idx += 1
        else:
            cnt += hay[p_idx]
            hay[p_idx] = 0
            p_idx += 1
            hay[m_idx] = temp
            
    print('#{} {}'.format(tc, cnt))
