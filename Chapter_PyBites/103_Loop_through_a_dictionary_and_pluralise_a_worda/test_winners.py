from winners import winners

def how_many_wins(capfd):
    winners()
    output = capfd.readouterr()[0].splitlines()
    
    winner_prints = ["sara has won 0 games",
                     "bob has won 1 game",
                     "tim has won 5 games",
                     "julian has won 3 games",
                     "jim has won 1 game"]

    # dict so not relying on order of output
    for line in winner_prints:
        assert line in output
