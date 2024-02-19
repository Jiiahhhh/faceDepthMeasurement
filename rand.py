import numpy as np

# Set random seed
np.random.seed(42)

# Generate 1000 random values in the range 25-30
random_values = np.random.randint(20, 31, 1000)

# Print the random values
for value in random_values:
    print(value)

# Save the random integer values to a text file
np.savetxt('random_values.txt', random_values, fmt='%d')
