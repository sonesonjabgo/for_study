# fn_d(91) 
# 출력 예시 
# 101
# # 9+1+91

# num + 1 + 0 + 1
# [1,0,1] 이 필요함
def fn_d(n):
    rlt = n + sum(map(int,str(n)))
    print(rlt)
    return(rlt)

fn_d(91)