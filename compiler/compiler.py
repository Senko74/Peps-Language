texte = open("Hello_world.peps").read()
mots = texte.split()


asm = []
asm.append(f"includelib ucrt.lib")
asm.append(f"includelib legacy_stdio_definitions.lib")
asm.append(f"includelib msvcrt.lib")
asm.append(f"")
asm.append(f"   .data")
asm.append(f'   message db "Message : %lld", 10, 0')
asm.append(f"")
asm.append(f"   .code")
asm.append(f"   option casemap : none")
asm.append(f"   extern printf : proc")
asm.append(f"")
asm.append(f"   public main")
asm.append(f"main proc")
for idx, mot in enumerate(mots):
    if(mot.isdigit()):
        print(mot)
        asm.append(f"   mov r8, {mot}")
    elif(mot == "+"):
        asm.append(f"   mov r9, {mots[idx + 1]}")
        asm.append(f"   mov r10, r8")
        asm.append(f"   add r10, r9")
    elif(mot == "print"):
        asm.append(f"   lea rcx, message")
        asm.append(f"   mov rdx, r10")
        asm.append(f"   sub rsp, 40")
        asm.append(f"   call printf")
        asm.append(f"   add rsp, 40")
asm.append(f"   ret")
asm.append(f"main endp")
asm.append(f"   end")

with open("compiled.asm", "w") as f:
    f.write("\n".join(asm))