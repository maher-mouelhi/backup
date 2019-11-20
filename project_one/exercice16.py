import random
import string
s = "abcdefg123456789"
s2 = string.ascii_letters+ string.punctuation+string.digits+string.ascii_uppercase
long = 10
a = ''.join(random.sample(s2,long))
print(a)