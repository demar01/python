
#!/usr/bin/env python3

def parse_table(table_text):
    # Remove whitespace (this will remove the n at the beggining)
    table = table_text.strip()
    # Split into rows on newline
    rows = table.split('\n')[1:]
    return [[float(e) for e in col.split()[1:]] for col in rows]

def prob_calc(path, states, matrix):
    prob = 0.5
    for i in range(len(path) - 1):
        el1, el2 = path[i], path[i + 1]
        #compute the probability for the given path
        prob *= matrix[states.index(el1)][states.index(el2)]
    return prob

def parse(text):
    path, states_raw, table = text.split('--------')
    # Remove trailing whitespace (this will remove the n at the end)
    path = path.strip()
    # List of states (there is going to be 2 states A and B)
    states = states_raw.split() 
    matrix = parse_table(table)
    return prob_calc(path, states, matrix)


def main(filename='Chapter_Rosalind/ba10a/rosalind_ba10a.txt'):
    with open(filename) as f:
        text = f.read()
    print(parse(text))

if __name__ == "__main__":
    main()