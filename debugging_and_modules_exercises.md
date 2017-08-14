1. A module is a Python file that stores functions, classes, or variables that can be imported in other Python files.

2. Three ways to import a module in Python are:

	```python
	import random
	import random as r
	from math import sqrt
	```

3. Importing allows us to have more organized code and easily reuse code across multiple files.

4. Three examples of using the random module are shuffling a deck, flipping a coin, and rolling dices.

5. ImportError is an error thrown when you try to import a module Python cannot locate or when you import something Python cannot find inside the module.

6. An OrderedDict is useful when order matters for key-value pairs, such as when we want the keys of the dictionary to be in alphabetical order.

7. A defaultdict is useful when you do not want a KeyError thrown when you try to access a key that doesn't exist. Defaultdict also allows multiple values for one key.

	```python
	if __name__ == '__main__':
    pass
    ```

8. The code inside the if statement will not run when that module is imported into another file, but will run when we the module is executed directly.


