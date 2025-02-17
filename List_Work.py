# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

Science = ['stars', 'pap', 'mom']
#print(len(List))

def match_ends():
    count = 0
    for word in Science:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count
print(match_ends())

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

Markers = ["Maroon", "Red", "Blue", "Martina", "Muerto"]
Markers_M = ["Maroon", "Martina", "Muerto"]
Markers_Rest = ["Red", "Blue"]
Markers_M.sort()
Markers_Rest.sort()
print(Markers_M)
print(Markers_Rest)
Markers_M.extend(Markers_Rest)
print(Markers_M)

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
Tuple = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Tuple.sort(key=lambda x: x[-1])
print(Tuple)
