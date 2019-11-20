fizzes = [x if x%3 else "fizz" for x in range(1,50)]
print(fizzes)
fizzes_less_buzzes  = [x if x%3 else "fizz" for x in range(1,50) if x%5]
print(fizzes_less_buzzes)

n=100
non_primes = {j for i in range(2,8) for j in range(i*2,n,i)}

primes = [x for x in range(2,n) if x not in non_primes ]
print(primes)

#some problems with list comprehension = time ==> to be resolved by generator

#[x for x in range(2,n) if x not in non_primes ] => List comprehension
#(x for x in range(2,n) if x not in non_primes ) => Generator

#itertools

import itertools
print(list(itertools.combinations(['a','b','c','d'],2)))
print(list(itertools.permutations(['a','b','c','d'],2))) # ( a,b ) and (b,a)

print(list(itertools.product("abc","123")))
print(list(itertools.product("abc","123")))

print(list(itertools.product([0,1],repeat=4)))



