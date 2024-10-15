# 반복되는 구문 해결하기

mysales = input("연봉을 입력하세요 : ")
name = input("이름을 입력하세요 : ")
checkTime = input("출근시간(HHMM) 형식으로 입력하세요. : ")
checkTimei = int(checkTime)
attstr = ""

if len(checkTime) < 4 :
    print("시간은 HHMM 형식으로 입력하셔야 합니다. 연봉을 책정할 수 없습니다.")
else :
    if checkTimei < 900 :
        mysales = str(float(mysales) * 1.3)
        attstr = "출근"        
    elif checkTimei <= 905 :
        mysales = str(float(mysales) * 1.1)
        attstr = "출근인정"
    elif checkTimei > 905 :
        mysales = str(float(mysales) * 0.85)
        attstr = "지각"
    else :
        print("잘못 입력하셨습니다.")
    
#인센티브 계산

print(name + "님 " + checkTime + "시에 "+attstr+"입니다. " + "그래서 당신의 연봉은 " + mysales + "원입니다.")