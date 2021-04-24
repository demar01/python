games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def winners():
    for key in games_won:
        if games_won[key]==1:
            print(f'{key} has won {games_won[key]} game')
        else:
            print(f'{key} has won {games_won[key]} games')

#This works but it's probably easier to iterate directly though items


def winners():
    for k, v in games_won.items():
        if v == 1:
            print(f'{k} has won {v} game')
        else:
            print(f'{k} has won {v} games')

#This works but it can be done more elegantly

def winners():
    for k, v in games_won.items():
        msg = f"{k} has won {v} game"
        if v !=1:
            msg += "s"
        print(msg)    
