def isPrime(x, tillx):
  divided = 0
  for i in tillx:
    if (x % i) == 0:
      divided = 1

  if divided == 0:
    tillx.append(x)

tillx = []
for i in range(2, 100):
  isPrime(i, tillx)

print(tillx)
