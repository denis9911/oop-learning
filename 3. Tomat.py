class Tomato:
    __states_list = ['absent', 'bloom', 'green', 'red']
    def __init__(self, _index):
        self.index= _index
        self._state = self.__states_list[0]

    def grow(self):
        if not self.is_ripe():
            index = self.__states_list.index(self._state)
            self._state = self.__states_list[index + 1]

    def is_ripe(self):
        return self._state == self.__states_list[-1]


class TomatoBush:
    def __init__(self, tomatos_num):
        self.tomatoes = [Tomato(i) for i in range(tomatos_num)]

    def growl_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        if self.all_are_ripe():
            self.tomatoes.clear()
            print('Урожай собран')
        else:
            print('Помидоры ещё не выросли!')


class Gardener:
    def __init__(self, name, tomato_bush):
        self.name = name
        self._tomato_bush = tomato_bush

    def work(self):
        self._tomato_bush.growl_all()
        print('Ваши помидорки подросли!')


    def harvest(self):
        if self._tomato_bush.all_are_ripe():
            self._tomato_bush.give_away_all()
        else:
            print('Не все помидоры на кусте ещё созрели')

    @staticmethod
    def knowledge_base():
        print('Пока садовник работает - помидоры на кусте растут, после их созревания можно собрать урожай')

Gardener.knowledge_base()
kust = TomatoBush(10)
stepan = Gardener('Stepan', kust)
stepan.work()
stepan.work()
stepan.harvest()
stepan.work()
stepan.harvest()




