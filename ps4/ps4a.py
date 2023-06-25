# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  
    '''
    if len(sequence) == 1:
        return [sequence]

    permutations = []
    first_char = sequence[:1]
    remaining_chars = sequence[1:]
    remaining_permutations = get_permutations(remaining_chars)

    for item in remaining_permutations:
        for index in range(len(item) + 1):
            permutation = item[:index] + first_char + item[index:]
            permutations.append(permutation)
            
    return permutations



if __name__ == '__main__':
   #EXAMPLE
   example_input_1 = 'abc'
   print('Input:', example_input_1)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input_1))

   example_input_2 = 'vba'
   print('Input:', example_input_2)
   print('Actual Output:', get_permutations(example_input_2))


    


