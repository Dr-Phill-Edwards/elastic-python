import sys
from startrek.Elastic import Elastic

elastic = Elastic()

def exit():
    print('Goodbye!')
    sys.exit()

def get():
    uid = input('Enter species uid: ')
    species = elastic.get(uid)
    species.print()

def search(querytype):
    key = input('Enter key: ')
    value = input('Enter value: ')
    for species in elastic.search(querytype, key, value):
        species.print()

while True:
    print('0) Exit')
    print('1) Get Species')
    print('2) Search on key and matching value')
    print('3) Search on key and prefix')
    option = input('Enter an option: ')
    if option == '0':
        exit()
    elif option == '1':
        get()
    elif option == '2':
        search('match')
    elif option == '3':
        search('prefix')
    else:
        print('Invalid option')
        