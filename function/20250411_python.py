def makeFishShapeBun(infill):
    if infill == "슈크림":
        ret = f"{infill}맛 붕어빵 완성"
    elif infill == "팥":
        ret = f"{infill}맛 붕어빵 완성(팥은 좀;;)"
    elif infill == "주체사상":
        ret = f"{infill}맛 붕어빵 완성입네다 혁명적이구만 동무"
    elif infill == "자본주의":
        ret = f"{infill}? 넌 총살이다 반동분자놈아"
    else:
        ret = f"반동분자놈 뭘넣은거야"
    return ret

print(makeFishShapeBun("슈크림"))



x = 10

def example():
    x = 20
    print(x)

example()
print(x)



def for10(string):
    for i in range(10):
        print(string)

for10("Hello World")



def sort(li):
    sort = [li.pop(0)]
    for i in li:
        z = 0
        while True:
            if i <= sort[z]:
                sort.insert(z,i)
                print(z,i)
                del(i)
                break
            elif z == len(sort) - 1:
                sort.append(i)
                del(i)
                break
            z += 1
    return sort


print(sort([2124421,543553,11,22,33,1,5,1414431345,12312312,444,2112,3333]))