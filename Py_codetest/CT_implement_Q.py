# 07 럭키 스트레이트

print("입력하세요")
n = input()
n_lengh = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(n_lengh//2):
    summary += int(n[i])
    
# 오른쪽 부분의 자릿수 합 더하기:
for i in range(n_lengh//2, n_lengh):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else :
    print("READY")







