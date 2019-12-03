from sys import argv

script, filename = argv # file name read to variable

txt = open(filename) # open file

print(f"Here's your file {filename}:")
print(txt.read()) # print file content

print("Type the filename again:")
file_again = input("> ") #input file name

txt_again = open(file_again) #open file again

print(txt_again.read()) # read file content
