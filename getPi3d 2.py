import random
def get_pi(num):
    num_of_dots_in_sphere = 0
    num_of_dots_in_cube = 0

    for i in range(num):
    
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
        num_of_dots_in_cube += 1
        if ((x ** 2) + (y ** 2) + (z ** 2))  <= 1:
            num_of_dots_in_sphere += 1
        num_of_dots_in_cube += 1
        pi = float(((6 * num_of_dots_in_sphere) / num_of_dots_in_cube))
    return pi

while True:
    
    num = int(input("Please input an integer to calculate the value of pi: "))
    x = get_pi(num)

    print(x)
    print("\n")
