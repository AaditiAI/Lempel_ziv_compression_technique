#Aaditi, 2021
import os
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Prompt the user for the file path
file_path =r'C:\Users\vivek\Downloads\lempel text file.txt'

# Read the content of the text file
file_content = read_text_file(file_path)

if file_content is not None:
    print("Content of the text file:")
    print(file_content)
    print(' ')


def extract_unique_substrings(file_content ):
    unique_substrings = {}
    n = len(file_content )
    #Dictionary for unique substring
    unique_substrings[file_content [0]] = '1'
    i = 1
    k = ""
    current_code = 2
    while i < n:
        k = k + file_content [i]
        if k not in unique_substrings:
            unique_substrings[k] = str(current_code)
            current_code += 1
            k = ""
        i += 1

    return unique_substrings

unique_substrings = extract_unique_substrings(file_content )

print("Unique substrings and their assigned numbers:")
for substring, code in unique_substrings.items():
    print(f"{substring}: {code}")
unique_characters = set(file_content)#set is used to extract unique characters
sorted_characters = sorted(unique_characters)


#Dictionary for unique characters
char_to_num = {}
current_code = 0
for char in sorted_characters:
    char_to_num[char] = str(current_code)
    current_code += 1
print('')
print("Unique characters and their assigned numbers:")
for char, num in char_to_num.items():
       print(f"{char}: {num}")
print(' ')

def copy_unique_substrings_to_array(unique_substrings):
    array = []
    for substring, code in unique_substrings.items():
        array.append([substring, code])
    return array
array1 = copy_unique_substrings_to_array(unique_substrings)
array2 = copy_unique_substrings_to_array(char_to_num)

print('Dictionary 1 converted into array1 consisting of unique substring',array1)
print('')
print('Dictionary 2 converted into array2 consisting of unique characters',array2)
print('')

list1 = []
for i in range(len(array1)):
        if len(array1[i][0]) == 1:
         # Use the code from 'array2'
          
          y=array1[i][0]
          z=char_to_num.get(y)
          list1.append(z)
        else:
          m = array1[i][0]
          n = m[:-1]
          x = m[-1]
          q = char_to_num.get(x) # Use the code from 'array2'
          r = unique_substrings.get(n)
          list1.append(r + q)
print("Assigning unique character to last bit from array 2 and giving position value to the remaining ones from array 1 ")
print(list1)
print('')
#converting it into binary 
list2=[]
for i in range(len(list1)):
    if(len(list1[i]))==1:
        list2.append(list1[i])
    else:
     k=list1[i]
     j=int(k[:-1])
     d=k[-1]
     h=str(bin(j))
     list2.append(h[2:]+d)
print("Keeping the last bit as it is taken from List1 and converting position value to binary")
print(list2)
print('')

#finding max length
max_length_string = max(list2, key=len)
max_length = len(max_length_string)

#padding zeroes
print("Padded substrings")
finalcode=[]
final_code = [s.zfill(max_length) for s in list2]
print(final_code)

#using ord to find the ascii values
print("\nASCII code of the input string:")
for char in file_content :
    ascii_code = ord(char)
    print(f"{char}: {ascii_code}", end=' ')
print('\n ')

# Print the binary representation of the input string
print("\nBinary representation of Ascii form:")
binary_string = ' '.join(format(ord(char), '08b') for char in file_content )
print(binary_string)
print('\n')

#For printing total number of characters
# Split the multiline string into individual lines
lines = file_content.split('\n')

# Calculate the length of each line excluding the trailing space
line_lengths = [len(line.rstrip()) for line in lines]

# Calculate the sum of lengths of all lines
total_length = sum(line_lengths)

# Print the result
print(f"Total character count across all lines: {total_length} characters")
lempelziv=max_length*(total_length)
ascii_code=8*(total_length)
print("Number of unique substrings =",len(array1))
print('Compression Ratio is :',(lempelziv/ascii_code))




