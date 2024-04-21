#Write and Save Files in Python 김우준 2024133519

#Writing Files
from google.colab import drive
drive.mount('/content/gdrive')

Mounted at /content/gdrive

# Write line to file
with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

This is line A

# Write lines to file
with open('/content/gdrive/My Drive/Colab Notebooks/example10.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    writefile.write("This is line 10\n")

# Check whether write to file
with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Write a new line to text file
with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    
# Verify if the new line is in the text file
with open('/content/gdrive/My Drive/Colab Notebooks/example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

['This is line A\n', 'This is line B\n', 'This is line C\n']

# Write the strings in the list to text file
with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

[ ]
# Write the strings in the list to text file

with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
This is line A

This is line B

This is line C

# Verify if writing to file is successfully executed
with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'r') as testwritefile:
    print(testwritefile.read())

This is line A
This is line B
This is line C

# Append the line to the file
with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")

# Verify if the appending is successfully executed
with open('/content/gdrive/My Drive/Colab Notebooks/example3.txt', 'r') as testwritefile:
    print(testwritefile.read())

#Copy a file
# Copy file to another
with open('/content/gdrive/My Drive/Colab Notebooks/example11.txt','r') as readfile:
    with open('/content/gdrive/My Drive/Colab Notebooks/example12.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

# Verify if the copy is successfully executed
with open('/content/gdrive/My Drive/Colab Notebooks/example12.txt','r') as testwritefile:
    print(testwritefile.read())

This is line A
This is line B
This is line C
This is line D



