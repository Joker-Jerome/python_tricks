from functools import lru_cache
import time


# Function that computes Fibonacci
# numbers without lru_cache
def fib_without_cache(n):
	if n < 2:
		return n
	return fib_without_cache(n-1) + fib_without_cache(n-2)
	
# Execution start time
begin = time.time()
fib_without_cache(30)

# Execution end time
end = time.time()

print("Time taken to execute the\
function without lru_cache is", end-begin)

# Function that computes Fibonacci
# numbers with lru_cache
@lru_cache(maxsize = 128)
def fib_with_cache(n):
	if n < 2:
		return n
	return fib_with_cache(n-1) + fib_with_cache(n-2)
	
begin = time.time()
fib_with_cache(30)
end = time.time()

print("Time taken to execute the \
function with lru_cache is", end-begin)


from functools import lru_cache

@lru_cache(maxsize = 100)
def count_vowels(sentence):
	sentence = sentence.casefold()
	return sum(sentence.count(vowel) for vowel in 'aeiou')
	
print(count_vowels("Welcome to Geeksforgeeks"))


