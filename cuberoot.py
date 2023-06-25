# Guess and check

# cube = 8
# for guess in range(abs(cube) + 1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(cube, ' is not a perfect cube')
# else: 
#     if cube < 0:
#         guess = -guess
#     print('Cube root of ' + str(cube) + ' is ' + str(guess))

# Approximation

# cube = 28
# epsilon = 0.01 # the larger this number is the greater the innacuracy
# guess = 0.0
# increment = 0.0001 # the lower this number is the more iterations there will be
# num_guesses = 0

# while abs(guess**3 - cube) >= epsilon and guess <= cube: # basically saying while the difference between the guess cubed and the actual cube
#     guess += increment
#     num_guesses += 1
# print('num_guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#     print('Failed on cube root of ', cube)
# else:
#     print(guess, ' is close to the cube root of ', cube)

# Bisection

cube = .5
epsilon = 0.01
num_guesses = 0
low = 0
high = cube if cube > 1 else 1
guess = (high + low) / 2.0

while abs(guess**3 - abs(cube)) >= epsilon:
    if guess**3 < abs(cube): # cube root cannot be lower than the guess. the guessed cube root cubed is smaller than the target
        low = guess
    else: 
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, ' is close to the cube root of ', abs(cube))