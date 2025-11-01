class Device:
    def turn_on(self):
        pass

class Lamp(Device):
    def turn_on(self):
        return "Лампа светит"

class Computer(Device):
    def turn_on(self):
        return "Компьютер запускается"

class TV(Device):
    def turn_on(self):
        return "Телевизор показывает"

devices = [Lamp(), Computer(), TV()]

for device in devices:
    print(device.turn_on())