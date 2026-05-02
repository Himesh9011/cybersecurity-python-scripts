import getpass #module (getpass), used to make the input pass hidden
import hashlib # for hashing for (k-anonimity)
import requests #for getting response and sending requests
"""
password = input("Enter your password : " ) #Input Function
print(password); 
"""


user_pass = getpass.getpass("Enter your Pass : ") # Hidden Pass
print("Got Your Pass Word!"); 

encoded_pass = user_pass.encode('utf-8') # encoding the pass for hashing (it will turn the strings into the number for hashing process)

hash_text = hashlib.sha1(encoded_pass) # it will print messy computer readable texts 

full_hash = hash_text.hexdigest().upper() # it will print computer to human readable texts, hexdecimal() turns into clean 40 chars text,  
                                          # and upper() will change the texts into capital letters (helps in fetching data)

first5, tail = full_hash[:5], full_hash[5:] # Slicing (k-anonymity)

url = 'https://api.pwnedpasswords.com/range/' + first5 # api url

response = requests.get(url)
    
if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again.") # response and error tracking 
         
hash_match = response.text

lines = hash_match.splitlines() # splitlines helps in putting the api response individually rather than as /n

for line in lines:
        h, count = line.split(':') # unpacking and colon separator
        if h == tail:              # matching
                 print(f"Match found! Your password was leaked {count} times.")
                 break 
else:
    # This 'else' runs only if the loop finishes without hitting 'break'
    print("Safe! No matching hash found.")
