import decimal
decimal.getcontext().prec = 100

def fact(n):
	x = 1
	for i in range(1, n+1):
		x *= i
	return x

accuracy = 10

pi = decimal.Decimal(0)

for k in range(accuracy):
	pi += decimal.Decimal( decimal.Decimal((-1)**k) * decimal.Decimal(fact(6*k)) *  decimal.Decimal(13591409 + 545140134 * k) ) / decimal.Decimal( decimal.Decimal(fact(3*k)) * decimal.Decimal(fact(k)**3) * decimal.Decimal(640320**(3*k + 1.5)) )

pi = 12 * pi

print("{0:.19f}".format(1/pi))
