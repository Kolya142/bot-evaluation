import os
import time


class log:
    def __init__(self):
        self.logs = ""
    def send(self, data, type_):
        d = f'{type_}, {time.time()}: {data}'
        self.logs += f'{d}\n'
        print(d)
    def save(self):
        open("log.txt","w").write(self.logs)
l = log()
def log_(data, type_):
    l.send(data, type_)
def main(main_):
    try:
        main_()
    except Exception as e:
        log_(f"{e}", "Error")
        l.save()
        p = ''
        for i in str(e):
            if i == " ":
                p += "+"
            else:
                p += i
        os.system('start https://www.google.com/search?q=' + str(p))
        raise e