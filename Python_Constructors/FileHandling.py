
# to open a file we use : with open(filename , 'r' for read, and 'w' for write and 'a' for appending mode, buffer) as file


# try:
#     with open('testfile', 'r') as myfile:
#         for line in myfile:
#             print(line)
# except FileExistsError:
#     # error handling code
#     print("Error!")
"""
try:
    with open('testfile', 'r') as myfile:
        readthelines = myfile.readlines()

except FileExistsError:
    # error handling code
    print("Error!")

for i in range(len(readthelines)):
    print("Line: " + str(i) + ": " + readthelines[i])
    """

# in this code we iterate all files
# import os

# root_dir = os.getcwd()
# for root, folders, files, in os.walk(root_dir):
#     for filename in files:
#         print(root, filename)


### Read all content of the files

with open('testfile') as in_file:
    content = in_file.read()

print(content)

in_file.close()

with open ('testfile', 'w') as filee:
    filee.write(" New lines 1")
    filee.write(" New lines 2")
    filee.write(" New lines 3")