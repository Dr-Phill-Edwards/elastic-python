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

while True:
    print('0) Exit')
    print('1) Get Species')
    option = input('Enter an option: ')
    if option == '0':
        exit()
    elif option == '1':
        get()
    else:
        print('Invalid option')