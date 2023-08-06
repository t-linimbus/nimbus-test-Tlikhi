import random

def generate_random_integer():
    return random.randint(1, 9)

while True:
    # Call the function and store the random integer in variable A
    A = generate_random_integer()

    # Call the function again to generate another random integer and store it in variable B
    B = generate_random_integer()

    # Multiply A and B together to get C
    C = A * B

    # Print the values of A and C
    print("Random integer A:", A)
    print("Result of A * B (C):", C)

    # Check if C is equal to 4
    if C == 4:
        print("Success!")
        print("A:", A)
        print("B:", B)
        break

    print()  # Add a blank line for better readability

print("Reached C = 4")