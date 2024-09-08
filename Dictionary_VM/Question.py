class Question:
    def __init__(self):
        self.list = ["1. 추가 금액 넣기", "2. 메뉴 다시 고르기", "3. 그만 두기"]
        self.quesDict = self.CreateDict() # { 1 : "추가 금액 넣기"...
        #self.quesNoneNumDict = self.CreateNoneNumDict() # ["추가금액넣기"...
        self.quesReversDict = self.CreateReversDict() # ["추가금액넣기" : 1...
        # 주의점 이거 키 넣을때 입력값에 replace() 해줘야 함
    def CreateDict(self):
        QuestionDict = {}

        for item in self.list:
            dict_Key, dict_Value = int(item.split(".")[0]), item.split(".")[1].strip()
            QuestionDict[dict_Key] = dict_Value
        return QuestionDict

    # def CreateNoneNumDict(self):
    #     QuestionNoneNumList = {}
    #     # key와 Value 둘다 얻기 위해서는 딕셔너리.items()를 해줘야하고
    #     # key만 얻기 위해서는 딕셔너리만 써도된다.
    #     for key,value in self.quesDict.items():
    #         # strip 이건 양쪽 끝만 공백을 제거하고
    #         # replace 이건 전부다 제거 할 수도 있고 3번째 인수에는 횟수를 지정할 수도 있다.
    #         value = value.replace(" ", "")
    #         QuestionNoneNumList[value] = value
    #     return QuestionNoneNumList

    def CreateReversDict(self):
        QuestionReversDict = {}
        for key,value in self.quesDict.items():
            QuestionReversDict[value.replace(" ","")] = key
        return QuestionReversDict


