#!/usr/bin/env python3

input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# # We realize that there's a 2 character difference between the 
# # character pairs so we try to move 2 positions every char.
# We check if every character is a letter
# from a-z and if it is we shift it 2 positions in 
# the abc and store it in a new string.
sol=""
for ch in input_string:
    n = ord(ch)
    # 96 is the ascii code for a and 123 for z
    if (n>96) and (n<123):
        # since it is circular (z->b) we need to take it into account
        sol += chr((n - 96 + 2)%26 + 96)
    else:
        sol += chr(n)
print(sol)

# # So we try the same on the url...
# Since here there are only letters we don't need to check
# it. And also there's no edge cases (y,z)
sol = ""
for ch in "map":
    n = ord(ch)
    sol += chr(ord(ch) + 2)
print(sol)