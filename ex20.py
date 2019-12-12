from sys import argv

script, input_file = argv

def print_all(f): #function prints all file content
    print(f.read())

def rewind(f): #function to seek to beginning of the file
    f.seek(0)

def print_a_line(line_count, f): # function to print specified line of the file
    print(line_count, f.readline())

current_file = open(input_file) 

print("First let's print the whole file:\n") # print whole file 

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



