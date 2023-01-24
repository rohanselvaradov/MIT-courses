# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #Create empty list to contain the possible permutations
    permutations = []
    #If length of sequence is one:
    if len(sequence) == 1:
        #If permutations are empty:
        return list(sequence)
    #Otherwise:
    else:
        #Store permutations for the string excluding first letter
        sub_permutation = get_permutations(sequence[1:])
        for perm in sub_permutation:
            for i in range(len(perm) + 1):
                permutations.append(perm[:i] + sequence[0] + perm[i:])
        return permutations
            
    

if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'rat'
    print('Input:', example_input)
    print('Expected Output:', ['rat', 'rta', 'tra', 'tar', 'art', 'atr'])
    print('Actual Output:', get_permutations(example_input))

    example_input = '&*'
    print('Input:', example_input)
    print('Expected Output:', ['&*', '*&'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = '1'
    print('Input:', example_input)
    print('Expected Output:', ['1'])
    print('Actual Output:', get_permutations(example_input))


    pass #delete this line and replace with your code here

