string = input('Enter any Name\t')

###print (string[0].upper());
def Convert () :
    name = ""
    for i in range(0,len(string)) :
        if (ord(string[i]) >= 65 and ord(string[i]) <= 91 ) : name += string[i].lower();
        elif (ord(string[i]) >= 97 and ord(string[i]) <= 123 ) : name += string[i].upper();
    print (name);
    return ;

Convert ();