class Human:
    default_name = 'John'
    default_age = 18
    def __init__(self,__money = 0, __house = 0,name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = __money
        self.__house = __house

    def info(self):
        print('Name: {}, Age: {}, Money: {}, house: {}'.format(self.name, self.age, self.__money, self.__house))

    def default_info(self):
        return self.default_name, self.default_age

    def __make_deal(self, house):
        total_cost = house.final_price()
        if total_cost > self.__money:
            print('Недостаточно средств для выполнения операции!')
        else:
            self.__money -= total_cost
            self.__house += 1
            print(f'Поздравляю, вы купили дом прощадью {house._area}м2\nНа балансе осталось {self.__money}')

    def earn_money(self, money):
        self.__money += money
        print(f'Вы заработали {money}!')

    def buy_house(self, house):
        self.__make_deal(house)


class House:
    def __init__(self, _area,_price):
        self._area = _area
        self._price = _price

    def final_price(self, discount=0):
        return self._price - self._price /100 * discount


class SmallHouse(House):
    def __init__(self, _price, _area=40):
        super().__init__(_area, _price)
        self._area = 40



nikola = Human(name='Nikola', age=40)
dom = SmallHouse(_price=100)

nikola.earn_money(500)
nikola.buy_house(dom)
nikola.info()