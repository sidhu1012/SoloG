#!/usr/bin/env python
# coding: utf-8

import colorama
from colorama import Fore,Style
import time


def print_body():
    l="FILMANZA"
    print(f"{Fore.RED} {Style.BRIGHT}")
    print('\t\t',end='')
    for i in l:
        time.sleep(0.9)
        print(i,end='\t')
    time.sleep(5)   

    print(f"{Fore.BLUE}{Style.BRIGHT}\n\nM O D E S:\n\n {Fore.YELLOW}{Style.BRIGHT} \tEASY\n\n {Fore.GREEN}{Style.BRIGHT} \t\tMEDIUM\n\n {Fore.CYAN}{Style.BRIGHT} \t\t\t\tHARD")
    a='LOADING.....'
    print(f"{Fore.MAGENTA}{Style.BRIGHT}")
    print("\n")
    print("\t",end='')
    for i in a:
        time.sleep(1)
        print(i,end='\t')

    E="/EASY/"
    print(f"{Fore.YELLOW}{Style.BRIGHT}")
    print("\t\t\t\t",end='')
    for i in E:
        time.sleep(0.5)
        print(i,end=' \t')

    M='/MEDIUM/'
    print(f"{Fore.GREEN}{Style.BRIGHT}")
    print("\t\t\t",end='')
    for i in M:
        time.sleep(0.5)
        print(i,end=' \t')

    H='/HARD/'
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("\t\t\t\t",end='')
    for i in H:
        time.sleep(0.5)
        print(i,end=' \t')
