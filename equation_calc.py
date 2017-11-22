import re
import copy
# калькулятор выражений с перменными. умеет расставлять в правильном порядке, сокращать выражение (например, из 2a+3a сделает 5a)

def modified_len(p):
    # работает как обычная len(), но учитывает только первую цифру, если она есть
    res = 0
    tmp = re.findall(r"\D", p)
    res = len(tmp)
    if re.findall(r"\d", p) is not []:
        res += 1
    return res

class A:
    active = True
    numeral = None
    letters = None
    def __init__(self, s):
        sign = str(s[0])
        s = s[1:]
        numeral = ''.join(re.findall(r"\d",s))
        self.numeral = sign + numeral
        self.numeral = int(self.numeral)
        self.letters = ''.join(re.findall(r"\D",s))

def simplify(poly):
    result = []
    if poly[0]!="-":
        poly_tmp =  copy.deepcopy(poly)
        first_element = "+" + (re.split(r"[+-]", poly_tmp))[0]
        result.append(first_element)
    result += (re.findall(r"[+-]\w+",poly))
    # на этом этапе получаем список членов со знаками, к первому добавляем знак, если его не было
    #print (result)
    newres = []
    for i in sorted(result, key=lambda a: modified_len(a)):
        newres.append(i)
    #print (newres)

    # сортируем
    newlist = []
    for element in newres:
        tmp = sorted(element)
        tmp2 = ''.join(tmp)

        newlist.append(tmp2)
        x = sorted(newlist)
    #print (newlist)

    # делаем из списка список экземплеров класса для удобства
    list_of_A = []
    for x in newlist:
        a = A(x)
        list_of_A.append(a)

    # находим все элементы, которые можно просуммировать, помечаем их как неактивные, суммируем, записываем результат
    # в финальный список
    final_list = []
    for a in list_of_A:
        if a.active == 0:
            continue
        a.active = 0

        for x in list_of_A:
            if (a.letters == x.letters) and  (x.active):
                x.active =0
                #print(x.numeral, a.numeral)
                a.numeral += x.numeral
                #print(a.numeral)
        print (a.numeral)
        if a.numeral !=0:
            final_list.append(a)

    # готовим и выводим результат
    result = ""
    for x in final_list:
        if x.numeral>0:
            result+= "+"
        result +=str(x.numeral)
        result +=x.letters

    #result = result[:-1]
    if result[0] == "+":
        result = result[1:]
    print (result)
    return(result)

simplify("4x-4+5x-1xe+7777-5fdx")
