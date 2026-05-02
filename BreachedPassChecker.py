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

url = 'https://api.pwnedpasswords.com/range/' + first5

response = requests.get(url)
    
if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again.") 
         
