# 백준 1316 그룹 단어 체커

t = int(input())
cnt = 0 # 개수 세기
for _ in range(t):
    word = input()
    word_lst = [] # 중복 단어 체크 리스트
    idx = 0 # 인덱스
    t_word = word[idx] # 임시 단어 (반복중인 단어)
    
    while idx < len(word):
        if word[idx] in word_lst and word[idx] != t_word: # 조건에 안맞으면 중지
            break
        t_word = word[idx] # 반복중인 단어 변경
        
        if word[idx] not in word_lst: # 중복 단어 리스트에 없으면 추가
            word_lst.append(word[idx])
        idx += 1 # 인덱스 이동

    if idx == len(word): # 끝까지 확인 했으면 개수 세기
        cnt += 1

print(cnt)
