import random
import sys
from threading import Thread
from time import time, sleep

class Afficheur(Thread):
    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        i = 0
        while i < 5:
            for lettre in self.mot:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 100
                time.sleep(attente)
            i += 1

thread_1 = Afficheur("1")
thread_2 = Afficheur("0")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()