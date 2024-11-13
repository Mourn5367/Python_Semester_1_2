
# def CtoF(C):
#     return [c*1.8+32 for c in C]
# C = [25.4, 33.2, 66.7]
# F = CtoF(C)
#
# print(f'섭씨 : {C} [C]')
# print(f'화씨 : {F} [F]')
#
# def fun():
#     a = 10
#     b = 5
#     print(f"함수 출력문: {a},{b}")

# def printVal(a,b,c):
#     s = f' a is {a}, b is {b}, and c is {c}'
#     print(s)

# a = 100
# fun()
# print(a)

#printVal(a =10,11,12)
#printVal(10, 25, c = 33 )

# def printVal(*a):
#     print(type(a))
#     for v in a:
#         print(v)
# printVal()

def bmiprint(w: float, h: float):
    if h > 3:
        h = h / 100
    bmi =  w / pow(h, 2)
    if bmi >= 30.0:
        print(f"bmi = {bmi:.3f} 고도비만")
    elif bmi >= 25.0:
        print(f"bmi = {bmi:.3f}비만")
    elif bmi >= 18.5:
        print(f"bmi = {bmi:.3f}표준")
    else:
        print(f"bmi = {bmi:.3f} 마른 체형")

weight, height = map(float,(input("체중과 키(cm)를 입력해 주세요(체중과 키 구분은 공백으로 합니다.)")).split(" "))
bmiprint(weight, height)