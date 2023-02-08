# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

steak = 50000
vat = int(steak*0.15)
price = int(steak + vat)

print(f'스테이크 {steak:,} \n+ VAT    {vat:,} \n총계 ₩   {price:,}')
# f-string에 숫자 넣고 :, 입력 해주면 3자리마다 콤마 들어간다.
