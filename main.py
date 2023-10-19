import random
import csv
from time import sleep
from datetime import datetime


while True:
    number = random.randint(0, 100)
    now = datetime.now()
    with open("lab1.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter="\t")
        file_writer.writerow([now.strftime("%H:%M:%S"), "Температура воды", number])
        sleep(60)