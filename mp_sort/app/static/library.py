from org.transcrypt.stubs.browser import *
import random

# Commit 1: Global Variable Array 
array = []

def gen_random_int(number, seed):
	# Commit 2: gen_random_int 3 lines --->
	global array
	random.seed(seed)
	array = [random.randint(0, 9) for _ in range(number)]
	pass

def generate():
	number = 10
	seed = 200

	# Commit 3: 
	# call gen_random_int() with the given number and seed
	gen_random_int(number, seed)

	# Commit 4: 
	# store it to the variable array
	array_str = ', '.join(map(str, array)) + '.'

	# pass - CAN BE REMOVED
	# array = None
	# # convert the items into one single string 
	# # the number should be separated by a comma
	# # and a full stop should end the string.
	# pass
	# array_str = None

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

# Commit 5: Insertion_Sort(arr) implementation
def insertion_sort(arr):
    # Insertion sort implementation 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sortnumber1():

	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

	You need to do the following:'''

	# Commit 6: get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
	generated_numbers_str = document.getElementById("generate").innerHTML
	
	# Commit 7: create a list of integers from the string of numbers
	generated_numbers_str = generated_numbers_str.replace('.', '')  # Remove period
	array = [int(num.strip()) for num in generated_numbers_str.split(',')]

	# Commit 8: call your sort function, either bubble sort or insertion sort
	sorted_array = insertion_sort(array)

	# Commit 9: create a string of the sorted numbers and store it in array_str
	array_str = ', '.join(map(str, sorted_array)) + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():

	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# Commit 10: Split the string into a list of integers
	array = [int(num.strip()) for num in value.split(',')]

	# Commit 11: Sort the list using insertion sort
	sorted_array = insertion_sort(array)

	# Commit 12: Store the final string to the variable array_str
	array_str = ', '.join(map(str, sorted_array)) + '.'

	document.getElementById("sorted").innerHTML = array_str