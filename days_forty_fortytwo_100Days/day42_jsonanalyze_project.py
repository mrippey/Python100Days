import json 
from pprint import pprint
import sys 

json_file = 'ha_public-feed.json'

# Feed can be found at: https://hybrid-analysis.com/feed?json

with open(json_file, 'r', encoding='utf-8')as file_out:
    data = json.loads(file_out.read())


def interesting_subs():

    test = [item for item in data['data'] if item['isinteresting']]

    if test:
        print('Top 3 entries identified as interesting: ')
        print()
        pprint(test[:2])
        print()


def threatscore_gt_20():
    
    test_name = [item for item in data['data'] if item['threatscore'] in range(20,30) ]

    if test_name:
        print('Submissions with a threatscore between 20 and 30: ')
        print()
        pprint(test_name[:2])
        print()


def program_menu():
    print('1. ' + 'Obtain abbreviated results of submissions with a True "isinteresting" indicator')
    print('2. ' + 'Display abbreviated results for submissions with a threatscore between 20 & 30')


def main():
    while True:
        print('Days 40-42 Parse JSON file' +'\n')
        program_menu()
        print()
        menu_choice = input('[MENU] ' + 'Enter a selection from the choices above:  ' )
        print()
        if menu_choice == '1':
            interesting_subs()
        elif menu_choice == '2':
            threatscore_gt_20()
        elif menu_choice == 'q':
            print('exiting...')
            sys.exit()
        else:
            print('Sorry, couldnt recognize your choice, try again...')
            sys.exit()


if __name__ == '__main__':
    main()
