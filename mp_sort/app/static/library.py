from org.transcrypt.stubs.browser import *
# Commit 0: import Flask 
from flask import Flask, render_template
import random

# Commit 1: Global Variable Array 
array = []

def gen_random_int(number, seed):
	# Commit 2: gen_random_int 3 lines --->
	global array
	random.seed(seed)
	array = [random.randint(0, 9) for _ in range(number)]

def generate():
	number = 10
	seed = 200
	gen_random_int(number, seed)
	array_str = ', '.join(map(str, array)) + '.'

	# Generate Output	
	document.getElementById("generate").innerHTML = array_str

# Commit 3: Insertion_Sort(arr) implementation
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

	generated_numbers_str = document.getElementById("Generate 10 numbers").innerHTML
	generated_numbers_str = generated_numbers_str.replace('.', '')  # Remove period
	array = [int(num.strip()) for num in generated_numbers_str.split(',')]

	# Commit 4: call your sort function, either bubble sort or insertion sort
	sorted_array = insertion_sort(array)

	# Commit 5: create a string of the sorted numbers and store it in array_str
	array_str = ', '.join(map(str, sorted_array)) + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():

	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.
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

	# Commit 6: Sort the list using insertion sort
	sorted_array = insertion_sort(array)

	# Commit 7: Store the final string to the variable array_str
	array_str = ', '.join(map(str, sorted_array)) + '.'

	document.getElementById("sorted").innerHTML = array_str