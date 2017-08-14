1.

  ```python
  {k:v for (k,v) in [("name", "Elie"), ("job", "Instructor")]}
  ```

2.

  ```python
  l = ["CA", "NJ", "RI"]
  l2 = ["California", "New Jersey", "Rhode Island"]

  dict(zip(l,l2))
  {l[i]: l2[i] for i in range(0,3)}
  ```

3.

  ```python
  {letter: 0 for letter in ["a", "e", "i", "o", "u"]}
  ```

4.
  
  ```python
  {num: chr(num+64) for num in range(1,27)}
  ```