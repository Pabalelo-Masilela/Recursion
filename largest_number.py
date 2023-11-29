def find_largest(list, index=0):
    # Base case: If the index is equal to the length of the list minus 1, return the last element
    if index == len(list) - 1:
        return list[index]
    
    # Recursive case:
    # Find the largest number in the rest of the list starting from the next index
    index_move = find_largest(list, index + 1) # deits the base case rdescription of index realtion to list
    
    # Compare the largest number in the rest with the current element
    if list[index] > index_move:
        return list[index]
    else:
        return index_move
   

# Example test case:
if __name__ == "__main__":
    my_list = [12, 5, 27, 8, 19, 33]
    
    largest = find_largest(my_list)
    print(f"The largest number in the list is: {largest}")
