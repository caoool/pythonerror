import threading

state = [""] * 5
mutex = threading.Lock()
condition = [threading.Condition()] * 5

class philosopher(threading.Thread):
	def __init__(self, name, i):
		threading.Thread.__init__(self)
		self.name = name
		self.i = i
		
	def run(self):
		while True:
			mutex.acquire()
			state[self.i] = "HUNGRY"
			test(i)
			if state[self.i] != "EAT":
				condition[self.i].wait()
			mutex.release()
			print (self.name + ' is eating!')
			mutex.acquire()
			state[self.i] = "THINKING"
			test((self.i+1)%5)
			test((self.i+5-1)%5)
			mutex.release()
			print (self.name + ' is thinking!')
			
	def test(j):
		if state[(j+5-1)%5] != "EAT" and state[j] != "HUNGRY" and state[(j+1)%5] != "EAT":
			state[j] = "EAT"
			condition[i].notify()
			
names = ['P1', 'P2', 'P3', 'P4', 'P5']
philosophers = [philosopher]*5
for i in range(5):
	philosophers[i] = philosopher(names[i], i)
for p in philosophers:
	print (p)
	p.start()

	
