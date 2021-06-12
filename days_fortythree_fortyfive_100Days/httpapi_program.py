import httpapi
import sys
import time 
import webbrowser

def program_menu():
    print()
    print('*' * 10 + " WELCOME TO TALK PYTHON SEARCH TOOL " + '*' * 10)
    print()
    


def main():
    while True:
        program_menu()
        print()
        menu_choice = input('[+] Enter a search term: ' ).lower()
        print()

        if menu_choice == 'q':
            print('exiting...')
            sys.exit() 

        response = httpapi.talk_python_search_terms(menu_choice)
        
        print(f'\n Top {len(response)} found for {menu_choice}')
        print()
        time.sleep(2)

        for i, r in enumerate(response, start=1):
            print(f'{i} : {r.title}')
        print()

        time.sleep(2)
        pick_a_result_to_open = int(input('Which search result would you like to learn more about?: '))
        print()
        
        #https://github.com/Anthlis/My_100_Days_Of_Python/blob/master/43-45-search-api/my-code-D2/TPS_program.py
        
        get_search_result_link = response[int(pick_a_result_to_open)-1]
        print()
          
        
        tpython_url = 'https://talkpython.fm'
        request_url = tpython_url + get_search_result_link.url
        print(f"\nYour browser will now open: " + request_url)
        #webbrowser.open(request_url, new=2)
        
       
if __name__ == '__main__':
    main()
