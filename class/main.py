class Hello:
    def hello_world(self):
        print("Hello World!")

a = Hello()
a.hello_world()

class star:
    def pyramid(self, size):
        for i in range(1,size+1):
            print("*" * i)

s = star()
s.pyramid(10)

class Member:
    def __init__(self, name):
        self.name = name
    
    def member_me(self):
        print(f"제 이름은 {self.name} 입니다.")

m = Member("구누")
m.member_me()

class MyInfo:
    def __init__(self, name, age ,home):
        self.name = name
        self.age = age
        self.home = home

    def member_me(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}살, 사는곳은 {self.home}입니다.")

m = MyInfo("리은교", 6974, "청와대")
m.member_me()

#로동으로인해 그뒤로는 못했읍니다