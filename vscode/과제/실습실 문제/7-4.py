import math

def fee(lental, drive):
    lentalfee = (lental / 10 ) * 1200
    if lental == 50:
        insurance = 525 * 2
    else:
        insurance = 525 * (lental / 30)

    if drive > 100:
        drivefee = (drive - 100) * 85 + 100 * 170
    else:
        drivefee = drive * 170

    totalfee = lentalfee + insurance + drivefee
    if totalfee >= 100000:
        print(math.ceil(round(totalfee, -5) / 10000))
    else:
        print(math.ceil(totalfee))




fee(600, 50) #=> 91000
# 60 * 1200 + 50 * 170 + (600 / 30) * 525
fee(600, 110) #=> 10
# 60 * 1200 + (100 * 170 + 10 * 85) + (600 / 30) * 525
# 72000 + (17000 + 850) + 10500 = 100,350
# 10만원 넘어가면 반올림해서 만원 단위로 말하기