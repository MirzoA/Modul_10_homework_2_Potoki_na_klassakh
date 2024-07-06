from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args,**kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        print(f'Sir {self.name}, на нас напали!',flush=True)
        count = 0
        ataka = 100

        if ataka > self.skill:
            for i in range(ataka - self.skill, -1, -self.skill):
                count += 1
                print(f'Sir {self.name}, сражается {count} день, осталось {i} воинов.',flush=True)
                time.sleep(1)
            else:
                print(f'Sir {self.name}, одержал победу спустя {count} дней!',flush=True)

knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print(f'Битва закончилась!')