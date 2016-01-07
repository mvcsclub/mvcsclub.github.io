import random

m = 50
bestM = 0.0
bestError = 1000000.0

x = [11.0, 8.0, 0.5, 7.5]
y = [4.0, 3.5, 3.2, 3.0]

for i in range(1, 100):
	error, error2 = (0, 0)
	print m

	for j in range(1, len(x)):
		error += (m*x[j] - y[j])*(m*x[j] - y[j]);
		error2 += ( (m + 0.0001)*x[j] - y[j])*( (m + 0.0001)*x[j] - y[j]);

	deriv = (error2 - error)/ 0.0001;
	#this tells you what direction the error changes as m increases

	if error < bestError:
		bestError = error
		bestM = m

	m -= deriv*0.001;
	#we want to go in the opposite direction
print bestM