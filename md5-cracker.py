print("Note: This script is for ethically use only..")
print("MD5 Hash Cracker! version:1.0.0")
print("                                             ")
print(" +=========================================+ ")
print(" |..........MD5 Hash Cracker v 1...........| ")
print(" +-----------------------------------------+ ")
print(" |#Author: Nur Alam                        | ")
print(" |#Contact: www.facebook.com/myself.nuralam   | ")
print(" |#This tool is made for pentesting.       | ")
print(" |#Website: www.myteghari.blogspot.com              | ")
print(" +=========================================+ ")
print(" |.........Thank You From Nur Alam.........| ")
print(" +-----------------------------------------+ ")
print("                                             ")
print("                                             ")
import hashlib
hashed_psk =raw_input("Enter Hashed Password Here: ")
dictionary = raw_input(r"Input Your Dictionary Here Without Quatation: ")

try:
    reading_dic = open(dictionary, " rU")
    read_dic = reading_dic.read()
    dic_list = read_dic.split()
except:
    print(" ")
    print("Sorry no dictionary found in this directory: ",'"',dictionary,'"')

#read_dic ekhane string
#r amra re method use sting tir protita word k list er item korediyechhi
#ebong list ti k ekti variable a store kore rekhe diyechhi

try:
    for i in dic_list:
        print("Trying current password: ",i)
        hash_object = hashlib.md5(i.encode())
        x = hash_object.hexdigest()
        if hashed_psk == x:
            print(" ")
            print("          Congratulations! password cracked successfully")
            print("          Your password is: ",i)
            break
        else:
            print(str(i) + " is incorrect password")
            print(" ")
            continue
finally:
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Thank you for using.......")
    print("                 Author: Nur Alam")
