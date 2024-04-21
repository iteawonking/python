#Reading Files Python 김우준 2024133519

#or use GDrive mounting method

from google.colab import drive
drive.mount('/content/gdrive')


# Read the Example1.txt
example1 = "/content/gdrive/My Drive/Colab Notebooks/example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

/content/gdrive/My Drive/Colab Notebooks/example1.txt

# Print the mode of file, either 'r' or 'w'
file1.mode

r

# Read the file

FileContent = file1.read()
FileContent

This is line 1\nThis is line 2\nThis is line 3\n(empty)\nThis is line 4\n\n


# Print the file with '\n' as a new line
print(FileContent)

This is line 1
This is line 2
This is line 3
(empty)
This is line 4

# Type of file content

type(FileContent)

str

# Close file after finish
file1.close()

# A Better Way to Open a File
# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

[ ]
# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
This is line 1
This is line 2
This is line 3
(empty)
This is line 4

# Verify if the file is closed
file1.closed

True

# See the content of file
print(FileContent)

This is line 1
This is line 2
This is line 3
(empty)
This is line 4

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

This

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

This is line 1

This is line 2

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

This is line 1
This is line 2

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())
    print("second line: " + file1.readline())
    print("third line: " + file1.readline())

first line: This is line 1

second line: This is line 2

third line: This is line 3

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;

Iteration 0 :  This is line 1

Iteration 1 :  This is line 2

Iteration 2 :  This is line 3

Iteration 3 :  (empty)

Iteration 4 :  This is line 4

Iteration 5 :

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
FileasList[0]

This is line 1\n

# Print the second line
FileasList[1]

This is line 2\n

# Print the third line
FileasList[2]

This is line 3\n

# Print the forth line
FileasList[3]

(empty)\n

# Print the fifth line
FileasList[4]

This is line 4\n
