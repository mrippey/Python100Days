from prompt_toolkit import prompt
from secrets import ( RISKIQ_USERNAME,
RISKIQ_KEY,
GN_KEY,
key)
import requests.exceptions
import json
import sys
from greynoise import GreyNoise
import logbook 
import time 

app_log = logbook.Logger('App')
PASSIVE_DNS_URL = 'https://api.passivetotal.org/v2/dns/passive'

# Style class borrowed from: https://github.com/NoDataFound/RiskIQ.Article.API/blob/main/RiskIQ.Article.API.v0.py
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    IGREEN = '\033[92m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[1;35m'
    GRAY = '\033[1;30m'
    WHITE = '\033[37m'


def get_domain_res_info():
    auth = (RISKIQ_USERNAME, RISKIQ_KEY)
    try:
        search = input("[+] 1 Domain query  Enter domain to query:  ")

        if not search:
            msg = 'Search field was empty'
            print(style.RED + f'Error: {msg}')
            app_log.warn(msg)
            raise ValueError('empty string')

        resp = requests.get(PASSIVE_DNS_URL, auth=auth, json={"compact_record": True, 
                                                                        "query": search})
        presponse = json.loads(resp.text)

        print(style.PURPLE + 'Please wait, retrieving Passive DNS information')
        time.sleep(2)
    
        for resolve in presponse['results']:
            print(style.BLUE + f"Resolution: {resolve['resolve']}")
        
        app_log.trace(f'Search successful search_term: {search} results: {len(presponse)}')

    except ValueError as e:
        print(f'Error: {e}')
        search

    except requests.exceptions.ConnectionError:
        msg = 'Network connection not established. Check your connection, or the lookup URL.'
        print(style.RED + 'Error: ' + msg)
        app_log.warn(msg)


def get_greynoise_info_ip():

    ip_lookup = input("[+] 2 IPv4 query  Enter IP Address to query: ")
    
    greynoise_lookup = GreyNoise(api_key=GN_KEY)
    gn_seen_before = greynoise_lookup.quick(ip_lookup)

    print(style.BLUE + f'GreyNoise Output: {gn_seen_before}' + "\n")


def setup_logging(filename):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = f'Logging initialized, level: {level}, mode: {filename}'
    logger = logbook.Logger('Startup')
    logger.notice(msg)

   
def main():
    print(style.GRAY + '1 ' + style.YELLOW+'Retrieve Suspicious Domain Info {Expects a domain name as input}')
    print(style.GRAY + '2 ' + style.YELLOW+'GreyNoise API IP Address Lookup {Expects an IPv4 Address}')
    print(style.GRAY + 'Q ' + style.YELLOW + 'Quit Program')

    while True:
        print()
        menu_choice = input(style.WHITE+'[MENU] ' + style.GREEN+'Enter one of the choice above:  ' + style.WHITE)
        
        if menu_choice == '1':
            get_domain_res_info()
        elif menu_choice == '2':
            get_greynoise_info_ip()
        elif menu_choice.lower() == 'q':
            sys.exit()
        
            
if __name__ == '__main__':
    setup_logging('lookup-app.log')
    main()
