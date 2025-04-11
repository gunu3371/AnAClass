# for i in range(3):
#     print(i)

# for i in range(2, 11,2):
#     print(i)

height = 12
for i in range(height):
    for z in range(height):
        print("* ", end="")
    print()

height = 12
for i in range(height):
    if False:
        pass
    print("* "*i)


height = 12
i = 0
while i < height:
    print("* ", end="")
    i += 1
print()