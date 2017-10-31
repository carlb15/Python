from threading import Thread, local
import time

class MessageThread(Thread):
    def __init__(self, message, sleep):
        self.message = message
        self.sleep = sleep
        Thread.__init__(self)                # remember to run Thread init!

    def run(self):                           # automatically run by 'start'
        i = 0
        while i < 50:
            i += 1
            print(i, self.message)

            time.sleep(self.sleep)

t1 = MessageThread("thread - 1", 1)
t2 = MessageThread("thread - 2", 2)

t1.start()
t2.start()