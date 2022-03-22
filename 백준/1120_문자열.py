# 1120 문자열

def countD(A, B):  # 두 문자열의 다른 문자 개수를 구하는 함수
    cnt = 0  # 차이가 나는 문자 개수
    for i in range(len(B)):
        if A[i] == B[i]:
            continue
        else:  # 문자가 다르면 개수 +1
            cnt += 1
    return cnt


A, B = input().split()

if len(A) == len(B):  # 같으면 바로 함수 돌리기
    result = countD(A, B)
else:  # 다르면
    result = len(B)
    dif = len(B) - len(A)
    for i in range(dif+1):  # 앞과 뒤에서 넣을 수 있는 조합 다 돌려서 최솟값 찾기
        tmp = B[:i]+A+B[len(A)+i:]  # 만들어진 부분집합
        tmp_cnt = countD(tmp, B)
        if result > tmp_cnt:
            result = tmp_cnt

print(result)