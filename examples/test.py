import os

def c(s):
    print ">",s
    os.system(s)


c("node ../lib/cli.js exprelon.jison")

c("node exprelon.js exprelon_in.txt")
