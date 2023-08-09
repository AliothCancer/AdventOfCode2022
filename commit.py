from os import listdir, system, chdir, path
from time import sleep
from sys import argv

for dir in [i for i in listdir() if path.isdir(i)]:
    chdir(dir)
    system("git add *")
    system("git commit -m 'first commit'")
    chdir("..")

system(f'git commit -m {argv[1]}')