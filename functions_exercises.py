# Part I

def difference(a,b):
  return a-b

def product(a,b):
  return a*b

def print_day(num):
  if num < 1 or num > 7:
    return None
  day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  return day_list[num-1]

def last_element(list):
  if len(list) == 0:
    return None
  return list[-1]

def number_compare(num1, num2):
  if num1 > num2:
    return "First is greater"
  elif num2 > num1:
    return "Second is greater"
  return "Numbers are equal"

def single_letter_count(word, letter):
  return word.lower().count(letter.lower())

def multiple_letter_count(word):
  return {letter.lower(): word.lower().count(letter.lower()) for letter in word}

def list_manipulation(list, cmd, loc, val):
  if cmd == "remove" and loc == "end":
    return list.pop()
  elif cmd == "remove" and loc == "beginning":
    return list.pop(0)
  elif cmd == "add" and loc == "beginning":
    list.insert(0, val)
    return list
  elif cmd == "add" and loc == "end":
    list.append(val)
    return list

def is_palindrome(word):
  word = word.lower().replace(" ", "")
  return word == word[::-1]

def frequency(list, search_term):
  return list.count(search_term)

def flip_case(str, letter):
  return "".join([char.swapcase() if char.lower() == letter.lower() else char for char in str])

def multipy_even_numbers(list):
  product = 1
  for num in list:
    if num % 2 == 0:
      product *= num
  return product

def mode(l):
  count = {val: l.count(val) for val in l}
  max_value = max(count.values())
  correct_index = list(count.values()).index(max_value)
  return list(count.keys())[correct_index]

def capitalize(str):
  return str[0].upper() + str[1:]

def compact(list):
  return [val for val in list if val]

def partition(list, fn):
  return [[val for val in list if fn(val)], [val for val in list if not fn(val)]]
  
def intersection(list1, list2):
  return [val for val in list1 if val in list2]

def once(fn):
  def inner(*args):
    inner.count += 1
    if(inner.count == 1):
      return fn(*args)
  inner.count = 0
  return inner

# Part 2

def reversed_strings(str):
  return str[::-1]

def looking_for_a_benefactor(list, new_avg):
  import math
  last_donation = math.ceil(new_avg * (len(list)+1) - sum(list))
  if last_donation <= 0:
    raise Exception("There was an error, last donation is less than 0.")
  return last_donation

def sum_of_a_sequence(begin_num, end_num, step):
  l = [num for num in range(begin_num, end_num + 1)]
  return sum(l[::step])

def max_diff(lst):
  if len(lst) <= 1:
    return 0
  return max(lst) - min(lst)

def count_the_smiley_faces(l):
  lst = [val for val in l 
    if (len(val) == 2 and (val[0] == ":" or val[0] == ";") and (val[-1] == ")" or val[-1] =="D")) 
    or (len(val) == 3 and (val[0] == ":" or val[0] == ";") and (val[-1] == ")" or val[-1] == "D") and (val[1] == "~" or val[1] == "-"))]   
  return len(lst)

def sentence_count(paragraph):
  count = 0
  for val in paragraph:
    if val == "." or val == "!" or val == "?":
      count += 1
  return count

def tortoise_racing(v1, v2, g):
  if v1 >= v2:
    return None
  t = (g/(v2-v1))*3600
  h = int(t/3600)
  m = int((t/60)%60)
  s = int(t%60)
  return [h, m, s]

def calculate_string_rotation(first, second):
  for num in range(0, len(second)):
    if second[num:] + second[:num] == first:
      return num
  return -1
