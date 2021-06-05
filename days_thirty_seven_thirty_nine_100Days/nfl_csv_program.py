import nfl_csv_research

def main():
    print('NFL Ticket Data for 2014')
    print()
    nfl_csv_research.setup_csv_stuff()
    print()

    print('Most Expensive Tickets: ')
    etp = nfl_csv_research.most_expensive()
    for idx, d in enumerate(etp[:5]):
        print(f'{idx+1}. Ticket Price: ${d.AvgTP:.2f},  Matchup: {d.Event}')
    print()

    print('Least Expensive Tickets: ') 
    ltp = nfl_csv_research.least_expensive()
    for idx, d in enumerate(ltp[:5]):
        print(f'{idx+1}. Ticket Price: ${d.AvgTP:.2f},  Matchup: {d.Event}')
    print()

    print('Division Appearances: ')
    nfl_csv_research.division_appearances()
    #print(div_appear)

if __name__ == '__main__':
    main()
