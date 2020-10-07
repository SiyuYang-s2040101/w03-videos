# First-fit heuristic for bin packing.
'''
The following is the example in the video
'''

items = [10, 10, 5, 5, 5]

# Set bin size
bin_size = 15

# Open the first bin
bins = [0]

# Loop over the items
for i in items:
    placed = False
    # Loop oven the open bins
    for j in range(len(bins)):
        # Check if there is space in bin
        if i <= bin_size - bins[j]:
            # Place the item and stop looking
            placed = True
            bins[j] = bins[j] + i
            break

    if not placed:
        # Open a new bin and place the item
        bins.append(i)

print(bins)
print(sum(bins) == sum(items))



# If we do not identify the items, just give them random numbers
import numpy as np

rng = np.random.default_rng()
# We want to have 20 items which are all within the range(2,31)
items = list(rng.integers(2, 31, size=20))
# Open a new bin
bins = [0]
bin_size = 50
print(items)

for i in items:
    placed = False
    for j in range(len(bins)):
        if i <= bin_size - bins[j]:
            placed = True
            bins[j] = bins[j] + i
            break
    
    if not placed:
        bins.append(i)

print(bins)
print(sum(bins) == sum(items))



'''
The following is the answer to the challenging question below the video
'''

# Create a list of integers randomly called items
import numpy as np
rng = np.random.default_rng()
items = list(rng.integers(2, 31, size=10))
print(items)
print(sum(items))

# Open a new empty bin in a bin set
bins = [[ ]]

# Define the bin_size
# And we need to make sure that the bin_size is large enough, at least larger than the maxium value of items
bin_size = 50

# Loop to place items in the bins
for i in items:
    placed = False
    for j in range(len(bins)):
        if i <= bin_size - sum(bins[j]):
            placed = True
            bins[j].append(i)
            break

    if not placed and i <= bin_size:
        bins.append([i])

print(bins)

# A function which is to test whether the sum of items equals the sum of integers in bins
def sum_of_bins():
    the_sum = 0
    for n in range(len(bins)):
        the_sum += sum(bins[n])
    return the_sum

# Remeber to add bracket behind the sum_of_bins, print(sum_of_bins) won't output anything
print(sum(items) == sum_of_bins())

'''
The answer to the question ends here.
The following line explain some bugs when I wrote the codes above
'''

# 1. The usage of sum():
# Test the function again because we have an issue in previous codes, need to debug
sum([3, 4, 10, 29, 13, 11, 11, 12, 27, 7])
sum(sum([3, 4, 10, 29]),sum([13, 11, 11, 12]),sum([27,7]))
# It is wrong to write code like the above ones
# If we want to calculate the sum of one list, we can write
bins = [[24, 20], [27, 12, 9], [7, 30], [20, 16], [24]]
sum(bins[0]) + sum(bins[1])...
# OR
bins = [1,2,3,4,5,6]
sum(bins)
sum([1,2,3,4,5,6])
# Not something like sum(1,2,3,4) or bins.sum()
# The use of sum(): https://www.programiz.com/python-programming/methods/built-in/sum


# 2. The differences between return xx and print(xx) at the end of a function
bins = [[24, 20], [27, 12, 9], [7, 30], [20, 16], [24]]

def sum_of_bins():
    the_sum = 0
    for n in range(5):
        the_sum += sum(bins[n])
    print(the_sum)
    print(type(the_sum))

print(type(sum_of_bins()))

# What is wrong with the function above
# Although the value seems to be the same, the datatype is not, that is why print(sum(items) == sum_of_bins()) is False
# When a function ends with print(xx), the type of this function let's say, sum_of_bins() is NonType
# That is type(sum_of_bins()) is NoneType
# When a function ends with return xx, the type of this function is the same as the_sum
# That is type(sum_of_bins()) == type(the_sum)
