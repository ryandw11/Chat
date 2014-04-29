print ('Welcome to Ryandw11 chat')
print ('what is your user name?')
user = input()
print ('Welcome ' + user + ', to ryan chat!')
usern = '[' + user + ']'
e = 1
r = 0
while e > r:
    e = e + 1
    a = input()
    String = a
    if a == 'Stupid':
        print ('Error: "stupid" is not a vaild word')
    elif a == 'idiot':
        print ('Error: "idiot" is not a vaild word')
    elif String[0] == '/':
        if a == '/me':
            print ('<' + user + '>')
        elif a == '/help':
            print (' ----------------HELP---------------')
            print (' 1. /me     Make you say your name.')
            print (" 2. /help   Tell's you the commands")
        elif a == '/stop':
            print ('Shutting down program.')
            e = 0
            print (' program terminated')
        else:
            print ('Unknown command. Type /help for help.')
    else:
        print (usern + a)
