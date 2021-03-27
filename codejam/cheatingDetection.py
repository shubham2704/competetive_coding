import numpy as np


def process_input(inputs):
    output = []

    for input in inputs:
        input = [[int(item) for item in line] for line in input]

        array = np.array(input)

        student = array.sum(axis=1)
        print(len(student))
        

        questions = array.sum(axis=0)
        print(len(questions))

    return output


if __name__ == "__main__":
    n = int(input())
    p = int(input())
    inputs = []
    for _ in range(n):
        input_matrix = []
        for _ in range(100):
            str = input()
            input_matrix.append(str)
        inputs.append(input_matrix)

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1