class AbstractRobot():

    def __init__(self, file):
        pass

    def decode(self):
        pass


class Robot(AbstractRobot):

    def __init__(self, material):
        self.material = material

    def decode(self):
        if self.material in ['медь', 'аллюминий']:
            return 'монеты'
        if self.material in ['серебро', 'золото', 'бронза']:
            return 'медали'
        if self.material in ['дерево']:
            return 'значок'
        else:
            return 'не знаю что собрать'


class Build:

    def __init__(self, inp_name, data=AbstractRobot):
        self.inp = inp_name
        self.data = data

    def out(self):
        decoded = self.data.decode()
        return f'Собираю {decoded} [{self.inp}]'


class Conveyor:

    def __init__(self, online_con):
        self.online_con = online_con
        print(f"Рабочий конвейер {online_con}")

    def build_out(self, inp):
        build = Build(inp_name=inp, data=Robot(material=inp))
        print(f'{self.online_con}:', build.out())


if __name__ == '__main__':
    c = Conveyor('1')
    c.build_out('дерево')
    c.build_out('золото')
    c.build_out('стекло')
    c.build_out('медь')