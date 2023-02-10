# 고지식한 알고리즘 (Brute Force)

P = 'is' # 찾을 패턴
t = 'This is a book~!' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
	i = 0 # t에서의 비교위치
	j = 0 # p에서의 비교위치
	while j < M and i < N: # 찾아야 하는 인덱스가 문장의 길이보다 커지면 안됨
		if t[i] != p[j]:     # 서로 다른 글자를 만나면
			i = i - j        # 비교를 시작한 위치로
			j = -1   # 아래의 더하는 과정 때문에 j는 항상 0으로 초기화 됨.
			# 더하는 과정은 if문 밖에 두어 무조건 실행되도록 한다.
			# 더하므로써 다음 인덱스를 검사하게 됨.
		i = i + 1 
		j = j + 1 
		if j == M : # 패턴을 찾은 경우
			return i - M # 검색 성공
		else: return -1 # 검색 실패		