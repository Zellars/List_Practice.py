#Problem 1: Create a list of the first 10 positive integers. Write a function to:
#Append the number 11 to the list.
#Remove the number 5 from the list.
#Print the list in reverse order.

#Problem 2: Given a list of numbers, write a function to:
#Find and print the maximum and minimum numbers in the list.
#Calculate and print the average of the numbers in the list.

#Problem 1 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #orignal list
print(my_list)
my_list.append(11) #added 11
print(my_list)
my_list.remove(5) #removed 5
print(my_list)
my_list.reverse() #reversed list
print(my_list)

#Problem 2
def find_max_min(my_list):
    max_num = max(my_list)
    min_num = min(my_list)
    return max_num, min_num

# Call the function 
max_val, min_val = find_max_min(my_list)

# Print the results
print(f"Maximum: {max_val}")  # Output: Maximum: 5
print(f"Minimum: {min_val}")  # Output: Minimum: 1

def calculate_average(my_list):
    if len(my_list) == 0:  # Check if the list is empty
        return 0  # Return 0 or some indication if the list is empty
    average = sum(my_list) / len(my_list)
    return average  # Return the average


average = calculate_average(my_list)  # Call the function and store the result
print(f"The average is: {average}")  # Output: The average is: 3.0


