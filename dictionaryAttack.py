#!/usr/bin/env python3
import sys
import hashlib
salts = ["1234567890", "1357924680", "0987654321"]
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
        ft1 = ""
        ft2 = ""
        match_hash = ""
        found = False
        x, y = -1, -1
        compare_hash = input("Please input one target MD5 hash value, then click enter: ")
        if compare_hash.lower() == "quit":
                print("Exiting.")
                break
        with open("passwords.txt", "r") as file:
                for line in file:
                        password_list = [[None for _ in range(4)] for _ in range(3)]
                        password_list_hashed = [[None for _ in range(4)] for _ in range(3)]
#plain password
                        password_list[0][0] = line.strip()
#reversed password
                        password_list[1][0] = password_list[0][0][::-1]
#-vowels password
                        tmp = [letter for letter in password_list[0][0] if letter not in vowels]
                        password_list[2][0] = ''.join(tmp)
                        for i in range(3):
                                for j in range(3):
                                        password_list[i][j+1] = salts[j] + password_list[i][0]
                        for i in range(3):
                                for j in range(4):
                                        password_list_hashed[i][j] = hashlib.md5(password_list[i][j].encode()).hexdigest()
                                        if password_list_hashed[i][j] == compare_hash:
                                                found = True
                                                match_hash = password_list[0][0]
                                                x, y = i, j
                                                break
                                if found: break
                        if found: break
        if found:
                if x == 1: ft1 = ", reversed"
                elif x == 2: ft1 = ", without vowels"
                if y != 0: ft2 = f", with salt {salts[y-1]}"
                print(f"The original password is: {match_hash}{ft1}{ft2}\nThank you for the input!")
        else:
                print("Cannot find a match.\nThank you for the input!")
