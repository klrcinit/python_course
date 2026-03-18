# Define an int variable with the name first_variable and assign it the value -5. Output the value of the variable. The output should look like this: "first_variable = ?", where you should replace ? with the value of the first_variable variable.
#
# Then, define a second int variable second_variable and assign it the value 3.
#
# Finally, print the result of dividing first_variable by second_variable to the console. The output should look like this: "first_variable / second_variable = ?" where you should replace ? with the value of the division first_variable / second_variable.
#
# Tipp: You must realize a cast from float to int in the prints.

first_variable = -5;

print("first_variable = " + str(first_variable));

second_variable = 3;

result = first_variable / second_variable;

print("first_variable / second_variable = " + str(int(result)));