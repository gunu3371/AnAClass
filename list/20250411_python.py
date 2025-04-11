a = "noodle"
b = True
c = 10
d = 10.2

mix = [a, b, c, d]

print(mix)

a = ['Math', 'Science', 'History']
b = ['P.E', 'Music', 'Art']

subject = a + b

aa = a*2

print(subject)
print(aa)

print(subject[-1])
print(subject[-6])
print(subject[1:3])
print(subject[5:1:-1])
print(subject[::3])
print(subject[::-1])

k = []

for i in range(11):
    k.append(i)

print(k[1::3])

subway = ["프로도", "튜브", "어피치"]
print(subway)

print(subway.index("튜브"))

subway.append("라이언")
print(subway)

subway.insert(3, "춘식이") # 리은교
print(subway)

subway.append("춘식이") # 김구누
print(subway)

print(subway.count("춘식이"))

li = [21,44,113,645,211,5,6,9,7,4,6974]

li.sort()

print(li)

li.reverse()

print(li)

print("\n\n\n")



s1 = set([1,2,3,4,5,5,5,5,5,5,6974,6974,11111,1,1,1,1,1,1,1,1,1,1,1,1])
print(s1)

s2 = set("ana")
print(s2)

A = {1,2,3,4,5,6,7}
B = {4,5,6,7,8,9,10}

print(A & B)

print(A | B)

print(A - B)

print(B - A)

print(A ^ B)

A.add(100)
print(A)

A.update([100, 200, 300])
print(A)

A.remove(100)
print(A)

A.discard(200)
print(A)

# A.remove(1000)
# print(A)

A.discard(1000)
print(A)

A.clear()
print(A)

print("\n\n\n")



age = input("나이 내놔: ")
print(f"니놈 나이는 {age}다.")

text = "Python"
print(len(text))

x = 3.14
print(type(x))

num_str = "6900"
num = int(num_str)
print(num + 74)

f = float("69.00")
print(f + 0.74)

s = str(69)
print(s + "74")

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

print(max(numbers))

print(min(numbers))

unsorted_list = [5,3,8,1]

sorted_list = sorted(unsorted_list)

print(sorted_list)

print(unsorted_list)