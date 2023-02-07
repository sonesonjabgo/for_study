import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N): # i는 arr의 각 자리를 위함
        if i % 2: # arr의 인덱스가 홀수이면 최솟값이 들어가야 함
            # arr[i]가 남은 수 중에 최솟값이 되야함.
            minidx = i
            for j in range(i+1, N): # 정렬이 된 인덱스는 고려하지 않기 위함
                if arr[j] < arr[minidx]:
                    minidx = j
            arr[i], arr[minidx] = arr[minidx], arr[i]
        else:
            maxidx = i
            for j in range(i+1, N):
                if arr[j] > arr[maxidx]:
                    maxidx = j
            arr[i], arr[maxidx] = arr[maxidx], arr[i]
    rst = ' '.join(map(str, arr[:10]))
    print(f'#{t} {rst}')