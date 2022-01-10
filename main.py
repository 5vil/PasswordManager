mass_pass = input('What is the master password - ')

if mass_pass == 'Kailasam123':
    print('Access Granted')
else:
    print('Nice Try')
    exit()
    

def add():
    acct = input('Enter the Accout type - ')
    acc = input('Enter the Username - ')
    pwd = input('Enter the password - ')

    with open('pass.txt', 'a') as f:
        f.write(acct +  "|" + acc  + "|" + pwd + '\n')

    print('Saved Succesfully')

def read():
    with open('pass.txt', 'r') as f:
        lines = f.readlines()
        print(lines)

while True:
    mode = input('Which mode would you like to enter in (add, view, q to quit) - ')

    if mode == 'add':
        add()

    if mode == 'view':
        read()
    
    if mode == 'q':
        break
    
#Done