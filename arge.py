import sys


def sys_args():
    """list of command-line arguments passed to a Python script.
      The first element in the list is the name of the script itself."""

    print("This is the name of the program:", sys.argv[0])
    print("Number of elements including the name of the program:", len(sys.argv))
    print("Number of elements excluding the name of the program:", (len(sys.argv) - 1))
    print("Argument List:", sys.argv)

    print(type(sys.argv))


def uses_in_args():

    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:", end=" ")
    for i in range(1, n):
        print(sys.argv[i], end=" ")

    # Addition of numbers
    Sum = 0

    for i in range(1, n):
        Sum += int(sys.argv[i])

    print("\n\nResult:", Sum)


def stdin():
    
	"""
    input to terminal
	"""
	line = sys.stdin.readline()
	print("You entered:", line)


import sys


def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#A function that sets the maximum depth of the Python interpreter's call stack.
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())


def Maximum_integer():
    
    

    print("Maximum integer value:", sys.maxsize)


def search_path():
   
# sys.path.append("/path/to/module")

# import my_module


	print("Python module search path:")
	for path in sys.path:
		print(path)


def size_of():
    import sys

    my_list = [1,1]
    print("Size of my_list:", sys.getsizeof(my_list))


def modules_in_our_system():
        
	"""These are the modules that are automatically available in every Python environment,
       without the need for any external libraries or packages. 
	"""
    
	for name in sys.builtin_module_names:
		print(name)
                
	'''contains a list of all the currently loaded modules in the current Python environment, 
	including both built-in modules and modules that have been imported by the user.'''
	print(sys.modules.keys())



def main():
    # sys_args()
     #uses_in_args()
     #stdin()
     #print(factorial(54))
     #size_of()
     #Maximum_integer()
   #search_path()
   modules_in_our_system()
  


if __name__ == "__main__":
    main()
