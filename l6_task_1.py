import time

class TrafficLight:
    __colors = ['Red', 'Yellow', 'Green']

    def running(self):
        for i in TrafficLight.__colors:
            if i == 'Red':
                print('Режим Красный')
                time.sleep(7)
            elif i == 'Yellow':
                print('Режим Желтый')
                time.sleep(2)
            elif i == 'Green':
                print('Режим Зеленый')
                time.sleep(5)

trafficlight = TrafficLight()
trafficlight.running()