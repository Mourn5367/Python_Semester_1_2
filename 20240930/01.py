from traceback import print_tb

if __name__ == '__main__':

    # num = [0,1,2,3]
    # english =['zero','one','two']
    # english += english
    # # print(english)
    # s = 'asd qwe zxc'
    # print(list(s))
    # sdict = {n:e for n,e in (zip(num,english))}
    # # print(sdict)
    # # print(zip(num,english))

    # matrix = [[3,4,5],[1,2,8],[9,7,6]]
    # matrix2 = [3,4,5,1,2,8,9,7,6]
    # print(matrix[0])
    # for i,item in enumerate(matrix2):
    #     print(i,item)

    # new_set = {e**2 for e in range(5,10)}
    # print(new_set)
    # qset = {5,3,6,2,1}
    # print(qset)
    #
    # new_sett = {e for e in 'mississippi'}
    # print(new_sett)

    vowels = ['a', 'e', 'i', 'o', 'u']
    rems = [' ', ',', '.', "'",'\n']
    sentence = '''We don't meet people by accident.
    They're meant to cross out path for a reason.'''


    tranSentence =sentence.lower().replace(' ','').replace('.','').replace("'",'').replace(',','').replace('\n','')
    print(tranSentence)
    result = {j for j in tranSentence if j not in vowels}
    print(result)