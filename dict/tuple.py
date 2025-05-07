tp = ("사과", "바나나", "딸기")
yeayea = ("사관", "포도", "망고")

new = tp + yeayea

apple, banana, strawberry = tp
print(apple) # 사과
print(banana) # 바나나
print(strawberry) # 딸기

def two(a, b, c):
    return (a*b, b*c)

ab ,bc = two(2, 4, 5)
print(ab)
print(bc)

try:
    tp[0] = "qkqh"
except:
    print("오류났다 반동아")

tuple = ("a", "b", "c")

try:
    tuple[0] = "g" #TypeError
    a = 2 / 0 # ZeroDivisionError
except TypeError as e:
    print(f"오류 내용: {e}")
except ZeroDivisionError:
    print("오류2")
finally:
    print("오류 고쳤다 반동아")