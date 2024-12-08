import numpy as np

diesides = int(input("Enter no.of sides 6/12 :"))
die = range(1, diesides)

numroll = int(input("Enter no.of times u wanna roll :"))

result = np.random.choice(die, size = numroll, replace = True)
print(result)