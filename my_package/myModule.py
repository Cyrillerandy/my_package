def top_n(items, n):
    '''Returns the top n items in an array, in desc order

    Args:
        items (array) : list or array like object
        n (int) : number of items to return

    Returns:
        (array) : returns an array of the first n items in desc order

    Egs:
        >>> top_n([8, 7, 3, 2, 4], 3)
        [8, 7, 4]
    '''
    for i in range(n): # Keep looping until the sort is done
        for j in range(len(items)-1-i):
            if items[j] > items[j + 1]: # Check for the bigger value
                items[j], items[j + 1] = items[j + 1], items[j] # Swap the two if first is larger

    # Extract the last 3
    top_n = top_n[-n:]

    # in desc order
    return top_n[::-1]

