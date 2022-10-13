
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def intel(self):
        print(self.cpu + ", " + self.ram)

cpu = input("Input cpu of your computer: ")
ram = input("Input ram of your computer: ")

comp1 = Computer(cpu, ram)
comp1.intel()





