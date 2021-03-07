import os

input_dir = "input"
output_dir = "output"

for input_filename in os.listdir("input"):
    with open(f"{input_dir}/f.txt", "r") as input_file:
        # Reading the first line and getting useful info
        output_filename = input_filename
        first_line = input_file.readline()
        simulation_time, num_of_intersections, num_of_streets, num_of_cars, extra_points = first_line.split(" ")

        # parsin strings into integers
        simulation_time = int(simulation_time)
        num_of_intersections = int(num_of_intersections)
        num_of_streets = int(num_of_streets)
        num_of_cars = int(num_of_cars)
        extra_points = int(extra_points)

        # Finding the corresponding streets for each intersection
        intersection_list_of_streeets = [[] for i in range(num_of_intersections)]
        for _ in range(num_of_streets):
            street_line = input_file.readline()
            intersection_id = int(street_line.split(" ")[1])
            intersection_list_of_streeets[intersection_id].append(street_line.split(" ")[2])


        # Creating the output file
        with open(f"{output_dir}/{output_filename}", "w") as output_file:
            output_file.write(str(num_of_intersections) + "\n")
            for i in range(num_of_intersections):
                output_file.write(str(i) + "\n")
                num_incoming_streets = len(intersection_list_of_streeets[i])
                output_file.write(str(num_incoming_streets) + "\n")
                for street in intersection_list_of_streeets[i]:
                    output_file.write(street + "\n")