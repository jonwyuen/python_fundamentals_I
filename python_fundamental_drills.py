def find_needle(haystack):
  return "found the needle at position {}".format(haystack.index("needle"))

def to_jaden_case(string):
	return " ".join(letter.capitalize() for letter in string.split())

def position(alphabet):
	return "Position of alphabet: {}".format(ord(alphabet)-96)

def even_or_odd(number):
	return "Odd" if number % 2 else "Even"

def greet(name):
	if name == "Johnny":
		return "Hello, my love!"
	return "Hello, {}!".format(name)

def positive_sum(arr):
	return sum([val for val in arr if val > 0])

def count_by(x, n):
	return [val * x for val in range(1,n+1)]

def remove_every_other(my_list):
	return my_list[::2]

def powers_of_two(n):
	return [2**val for val in range(0,n+1)]

def always(n=0):
	def inner():
		return n
	return inner

def bonus_time(salary, bonus):
	return "${}".format(salary*10) if bonus else "${}".format(salary)

def createDict(keys, values):
	while len(keys) > len(values):
		values.append(None)
	return dict(zip(keys, values))

def descending_order(num):
	return int("".join(sorted(str(num), reverse=True)))


def in_array(a1, a2):
	return sorted({a1val for a1val in a1 if any(a1val in a2val for a2val in a2)})

def bumps(road):
	return "Car Dead" if road.count("n") > 15 else "Woohoo!"

def get_middle(s):
	if len(s) % 2 != 0:
		return s[len(s)/2] 
	return s[len(s)/2 - 1] + s[len(s)/2]

def high_and_low(numbers):
	n = [int(val) for val in numbers.split()]
	return "{} {}".format(max(n), min(n))

def square_digits(num):
	return int("".join([str(int(val)**2) for val in str(num)]))

def is_isogram(string):
	return len(string) == len(set(string.lower()))

def longest(s1, s2):
	return "".join(sorted(set(s1 + s2)))

def flatten(lst):
	l = []
	for val in lst:
		l.extend(val) if type(val) is list else l.append(val)
	return l

def get_count(words=None):
  d = {'vowels':0, 'consonants':0}
  d['vowels'] = len([v for v in words.lower() if v in 'aeiou'])
  d['consonants'] = len([c for c in words.lower() if c not in 'aeiou' and c.isalpha()])
  return d

def make_lazy(fn, *args):
	def inner():
		return fn(*args)
	return inner
    


































