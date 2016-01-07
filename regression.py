import random

m = 0.0
bestM = 0.0
bestError = 1000000.0

x = [11.0, 8.0, 0.5, 7.5]
y = [4.0, 3.5, 3.2, 3.0]

for i in range(1, 10000):
	m = random.random() * 5.0
	error = 0.0

	#somehow calculate the error
print bestM