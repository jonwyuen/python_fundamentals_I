1.

  ```python
  [print(val) for val in [1,2,3,4]]
  ```

2.

  ```python
  [print(val*20) for val in [1,2,3,4]]
  ```

3.

  ```python
  [val[0] for val in ["Elie", "Tim", "Matt"]]
  ```

4.

  ```python
  [val for val in [1,2,3,4,5,6] if val % 2 == 0]
  ```

5.

  ```python
  [val for val in [1,2,3,4] if val in [3,4,5,6]]
  ```

6.

  ```python
  [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
  ```

7.

  ```python
  "".join([letter for letter in "first" if letter in "third"])
  ```

8.

  ```python
  [val for val in range(1,101) if val % 12 == 0]
  ```

9.
  
  ```python
  [letter for letter in "amazing" if letter not in ["a", "e", "i", "o", "u"]]
  ```

10.

  ```python
  [[num for num in range(0,3)] for val in range(0,3)]
  ```

11.

  ```python
  [[num for num in range(0,10)] for val in range(0,10)]
  ```
