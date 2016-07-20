#Storing number of entries in the phonebook in t
t=int(raw_input())
#splitting input and saving it as a dictionary
name_number=[raw_input().split() for i in range(t)]
phonebook={k:v for k,v in name_number}

while 1:
    try:
        userInput=raw_input()
        if(userInput in phonebook):
            print '%s=%s'%(userInput,phonebook[userInput])
        else:
            print 'Not found'
    # when there is no input received and end of file is reached
    except(EOFError):
        break
