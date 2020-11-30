

class person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print('안녕 나는 ' + self.name + '야')

    def catch(self,pokemon_name):
        print(pokemon_name + ' 넌 내 꺼야')

class pokemon:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print('얍 나는' + self.name + '이야')

    def attack(self):
        print(pokemon_name + '내 공격을 받아라')

p1 = person('지우')
p2 = person('이슬')
p3 = person('웅이')

p1.introduce()
p1.catch('피카츄')

p2.introduce()
p2.catch('고라파덕')

p3.introduce()
p3.catch('마자용')