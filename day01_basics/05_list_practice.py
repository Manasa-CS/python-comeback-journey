if __name__ == "__main__":
    num_list = [18, 25, 3, 57, 63, 42, 5]
    print("Original list:", num_list)

    # Accessing elements    
    print("First element:", num_list[0])
    print("Last element:", num_list[-1])

    # Appending an element
    num_list.append(49)
    print("List after appending 49:", num_list)

    # Inserting an element at a specific position
    num_list.insert(2, 33)
    print("List after inserting 33 at index 2:", num_list)

    # Removing an element
    num_list.remove(42)
    print("List after removing 42:", num_list)

    # Reversing the list
    num_list.reverse()
    print("List after reversing:", num_list)

    # Sorting the list
    sorted_list = sorted(num_list)
    print("Sorted list using sorted():", sorted_list)
    print("Original list after sorted():", num_list)  # Original list remains unchanged
    num_list.sort()
    print("List after sorting using sort():", num_list)

    #reverse sorting the list
    sorted_list = sorted(num_list, reverse=True)
    print("Sorted list using sorted():", sorted_list)
    print("Original list after reverse sorting:", num_list)  # Original list remains unchanged
    num_list.sort(reverse=True)
    print("List after reverse sorting using sort():", num_list)