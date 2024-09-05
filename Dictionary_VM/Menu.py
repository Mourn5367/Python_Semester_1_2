
class Menu:
    def __init__(self):
        self.ori = {"1. 사이다" : 1000, "2. 콜라" : 1500, "3. 쿠키" : 2000 , "4. 레몬에이드" : 2500}
        self.str = self.createStringDict() # {"사이다 : 1000...
        self.num = self.createNumberDict() # {"1: 1000...
        self.name = self.extractMenu() # { "","사이다"...
    def createStringDict(self):
        # 먼저 딕셔너리 생성
        dicString = {}

        # ori 메뉴는 키와 값으로 이루어진 딕셔너리다.
        # 이것을 언패킹 하기 위해서 key 변수에는 키를
        # valye 변수에는 값을 넣을것이다. 그런데 for를 이용한
        # 반복문으로 끝날때 까지 할 것이다.
        for key, value in self.ori.items():
            # "1. 사이다" 이렇게 되어있는 String 타입으로 되어있는 키를
            # split() 함수를 통해 .을 기준으로 나눌것이다.
            # 그러면 지금 상황에서 2등분 되는데 오른쪽 부분을 쓸 것이고
            # 그 값을 strip() 함수를 통해 공백을 지워 준 다음 str_Key 변수에
            # 저장 할 것이다.
            str_Key = key.split(".")[1].strip()
            # 이제 dicString 딕셔너리에 값을 지정해 주기 위해서
            # dicString[키] = 값 형태로 저장한 다음 반복문으로 넘어간다.
            dicString[str_Key] = value
        # 딕셔너리에 다 넣은 다음 반환하여 self.num 저장
        return dicString


    def createNumberDict(self):
        dicNumber = {}
        for key, value in self.ori.items():
            # 위의 createStringDict와 다른점은 int 형변환이다.
            # "1. 사이다"는 String 타입이기 때문에 스플릿을 통해
            # 분할한 다음 첫번째것을 고르더라도 "1" 이렇게 스트링타입으로 저장된다.
            # 그것을 막기 위해 int()를 이용해 형변환을 한 다음 딕셔너리에 저장한다.
            num_Key = int(key.split('.')[0])
            dicNumber[num_Key] = value
        return dicNumber

    def extractMenu(self):
        menuName = []
        menuName.append("")
        for key, _ in self.str.items():
            menuName.append(key)
        return menuName