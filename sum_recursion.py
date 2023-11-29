'''a function that takes a list of integers and a single integer as arguments. The single integer will represent an index point.'''

def sum_recursion(list, index):
    # base case to stop when index has reached 0
   if index <= 0:     
      return list[index]
    # as long as index  is not o, keeping moving to the index before current
   else:
    index_mover = sum_recursion(list, index - 1) # this edits the relationship of index to list defined above on base case- moes the index to -1 from relation to list used in base case
    return list[index] + index_mover

# Testing the recursive function
input_index = 4
list = [1, 4, 5, 3, 12, 16]
print(f"The sum of list intergers up to index {input_index} is: {sum_recursion(list,input_index)}")