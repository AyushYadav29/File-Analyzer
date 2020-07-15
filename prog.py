#sem end IT project
#group number:
#group members:Himanshu,Ayush,Dhruv

file=open("firstyear_project.txt",'w')
N=input("enter the number of lines you want to write:")#there is no need to add a full stop
for i in range(0,N):
    line=raw_input("enter the lines:")
    file.write(line+'\n')
file.close()
def menu():#gives you the main code.
    print("enter the option of your choise:")
    print("1)number of lines:")
    print("2)number of wordes:")
    print("3)number of charactors:")
    print("4)number of spaces:")
    print("5)number of vovels:")
    print("6)number of consonents:")
    print("7)find accourence of a word:")
    print("8)search and replace:")
    print("9)add lines to the file:")
    print("10)copy into a new file:")
    print("11)exit")
def sub_menu():#all done using seek()
    print("1)add at the end of the file:")
    print("2)add at the begining of file:")
    print("3)add something anywhere:")
    print("4)exit")
def number_of_lines():#1 used to find the number of lines
    num_lines = 0
    with open("firstyear_project.txt", 'r') as file:
        for line in file:
            num_lines += 1
    print"Number of lines:",num_lines
    file.close()
def number_of_wordes():#2 will count how manny words are there in the file or pirticular line it eill split the line in to a list of words and traversal in it.
    file=open("firstyear_project.txt",'r')
    word=0
    for line in file:
        wordlist=line.split()
        word=word+len(wordlist)
    print(word)
    file.close()
def number_of_charactors():#3 it further splits the words and gives the number of leters in a line also number of charactors in a wordlines = 0
    file=open("firstyear_project.txt",'r')
    characters = 0
    for line in file:#does count space and \n also
        wordslist = line.split()
        #print len(line)
        characters = characters + len(line)
    print(characters)
    file.close()
def number_of_spaces():#4 this loook for the spaces( )in a line in incriments i by one
    space=0
    file=open("firstyear_project.txt",'r')
    line=file.read()
    #print line
    for i in line:
        if i.isspace():#does count \n also
            space+=1
    print"spaces=", space
    file.close()
def number_of_vovels():#5 this will look for caps and small ['a','A','e','E','i','I','o','O','u','U']
    file=open("firstyear_project.txt",'r')
    vowels=('a','e','i','o','u','A','E','I','O','U')
    count=0
    line=file.read()
    for i in line:
        if i in vowels:
            count+=1
    print "number of vowels:", count
    file.close()
def number_of_consonants():#6 this will look for consonents
    print "number of consonants:", count
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    line=file.read()#does count space and \n also
    for i in line:
        if i not in vowels:
            count+=1
    print "number of consonants:", count
    file.close()
def accourence_of_a_word():#7 takes a word from the user and looks for the word when it finds it incriments count by 1 and at the end it displays the count.
    file=open("firstyear_project.txt",'r')
    word=0
    x=raw_input("input the word you want to find the occurense of:")
    for line in file:#does count space and \n also
        print line
        wordlist=line.split()

        for j in wordlist:
            if j==x:
                word+=1
    print "no of times word repeted is:",word
    file.close()
def search_and_replace():#8 this will replace the word every where
    w=raw_input("enter the word you want to replace:")
    W=raw_input("enter the word that it needs to be replaced with:")
    with open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt", 'r+') as file:
        #file.readline()
        lines=file.readlines()
        print(lines)
        for line in lines:
            print(line.replace(w,W))
        file.readlines()
        #file.close()
#def add_lines_to_the_file():
def the_begining():#will let you add staitments at rhe begining
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'a')
    x=raw_input("enter the thing to be added:")
    file.write(x+'\n')
    file.close()
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'r')
    Z=file.read()
    print Z
    file.close()
def the_ending():#will let you add staitments at the end
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'a')
    file.seek(2)
    X=raw_input("the the staitment to be added:")
    file.write(X+'\n')
    file.close()
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'r')
    Y=file.read()
    print Y
    file.close()
def write_anything_anywhere():#you can write anything anywhere
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'a')
    a=input("which position do you want to write from?")
    file.seek(a,0)
    z=raw_input("plz enter the text to be edited:")
    file.write(z)
    file.close()
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'r')
    X=file.read()
    print X
    file.close()
def copy_into_a_new_file():
    file=open("C:\\Users\\Dhruv\\Desktop\\1st year IT\\firstyear_project.txt",'r')
    f=open("copy_to_file.txt",'a')
    # Try Except Statement
    print "now coping to a new file........."
    for line in file.readlines():
        f.write(line)
    f.close()
    file.close()
    f=open("copy_to_file.txt",'r')
    F=f.read()
    print F
    f.close()

menu()
loop=1
choise=0
while loop==1:
    choise=input("enter the operation you want to choiseS:")
    if choise==1:
        print "this will display the number of lines"
        number_of_lines()

    if choise==2:
        print "this will display the number of words"
        number_of_wordes()

    if choise==3:
        print "this will display the number of chacters"
        number_of_charactors()

    if choise==4:
        print"this will display the number of spaces"
        number_of_spaces()

    if choise==5:
        print"this will display the number of vovels"
        number_of_vovels()

    if choise==6:
        print"this will display the number of consonants"
        number_of_consonants()

    if choise==7:
        print"this displays the accourence of a given word"
        accourence_of_a_word()

    if choise==8:
        print"this will search and replace"
        search_and_replace()

    if choise==9:
        print"add lines to the file:"
        sub_menu()
        Loop=0

        while Loop==0:
            option=input("enter your choise:")
            print "your option:",option
            if option==1:
                print"the_begining"
                the_begining()
            if option==2:
                print"the_ending"
                the_ending()

            if option==3:
                print"write_anything_anywhere"
                write_anything_anywhere()

            if option==4:
                Loop=1
    if choise==10:
        print"copy_into_a_new_file"
        copy_into_a_new_file()

    if choise==11:
        loop==0
