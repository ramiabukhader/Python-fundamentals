import os, stat

# os.makedirs("./directory1/subdirectory1")
# os.makedirs("./directory1/subdirectory2")

# print(os.getcwd()) #we get the current working directories

#removing the directory

# path = os.getcwd()
# os.rmdir("./directory1/subdirectory1")

# os.chmod("./directory1/subdirectory2/test.txt", stat.S_IREAD) # giving a permision to the directory and read only by the owner
#  we can stat.S_IROTH mode to make it acceble by everyone, or IWROTE that can be written by only owner, or IXUSER by everyone
# print("File can be raed only by owner")

print(os.path.join('a', 'b', 'c')) # creating bath for directories


