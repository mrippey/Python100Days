# My attempt utilizing the collections module on a different dataset

'''
Dataset: https://raw.githubusercontent.com/Azure/Azure-Sentinel/
master/Sample%20Data/Feeds/MSTICIoCs-ExchangeServerVulnerabilitiesDisclosedMarch2021.csv
'''

from collections import defaultdict, Counter
from csv import DictReader 

hafnium_indicators = defaultdict(list)

def get_top_indicators(data):
    
    with open(data, 'r')as f:
        for line in DictReader(f):
            ioctype = line['Indicator']
            hafnium_indicators[ioctype].append(line)
            cnt = Counter()
            for indicator, indicatortyp in hafnium_indicators.items():
                cnt[indicator] += len(indicatortyp)
                indicator_output = "\n".join(e for e, c in cnt.most_common(5))  #Separate output by a \n character
        print('Top 5 Indiciators: \n')
    return indicator_output

get_top_indicators('MSTICIoCs-ExchangeServerVulnerabilitiesDisclosedMarch2021.csv')



# Using code from the lecture against the Microsoft CSV

Ioc = namedtuple('Ioc', 'type first_seen')

def get_indiciator_info_by_date(data):
    indicators = defaultdict(list)
    with open(data, 'r')as f:
        for line in DictReader(f):
            try:
                date = line['DateAdded']
                threat = line['IndicatorType']
                seen = line['FirstSeen']
            except ValueError:
                continue 

            ioc = Ioc(type=threat, first_seen=seen)
            indicators[date].append(ioc)
    return indicators

indicators = get_indicator_info_by_date('MSTICIoCs-ExchangeServerVulnerabilitiesDisclosedMarch2021.csv')
print(indicators['2021-03-09'])
