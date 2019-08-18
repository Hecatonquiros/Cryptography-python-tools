
#Number of letters = 26

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number_letters = len(alphabet)
string_in = raw_input("Enter message to cipher: ")
string_out = ""
n = len(string_in)

shift = input("Enter the shift number: ")


#Shifting the letters of the message 

for i in range(n):
    letter = string_in[i]
    location = alphabet.find(letter)
    new_location = location + shift
    string_out += alphabet[new_location % number_letters]   #Module to allow every shift number


print("This is the message cipher: " + string_out)
