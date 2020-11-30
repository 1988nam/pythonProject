class Car():
    """
    Car Class
    Author : Nam
    Date : 2020.11.30
    Description : Class, Static, Instance Method
    """
# instance self 가 뭔지 ? class method cls 는 뭔지 ? 다시 한 번 Check 필요

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    # self 가 들어가 있으면 Instance Method 로 우선 이해
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {} , price :{}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {} , price :{}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('please 1 or more')
            return
        cls.price_per_raise = per
        return print('succeed!')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK this car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보 (인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격정보 (인상 후) 클래스 메소드 미 사용
Car.price_per_raise = 1.4

print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격정보 (인상 후) 클래스 메소드 사용

Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())

print()

# 인스턴스 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))