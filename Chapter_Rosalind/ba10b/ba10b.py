#!/usr/bin/env python3

""" Compute the Probability of an Outcome Given a Hidden Path """

def read_data(file_name):
    with open(file_name, 'r') as file:  
        observation_sequence = file.readline().strip() #this will read the xxyzyxzzxzxyxyyzxxz line
        file.readline() #this will read the --- line 
        observation = file.readline().strip().split() #this will read the  x   y   z line
        file.readline()
        hidden_sequence = file.readline() #this will read the BBBAAABABABBBBBBAAAAAA line
        file.readline()
        hiddens = file.readline().strip().split()
        file.readline()
        file.readline()
        matr = []
        for i in range(len(hiddens)):
            matr.append(file.readline().strip().split()[1:])

        for row in matr:
            for i in range(len(row)):
                row[i] = float(row[i])

        return observation_sequence, hidden_sequence, observation, hiddens, matr

def main(str1, str2, alph1, alph2):
    length = len(str1)
    answer = 1
    for i in range(length):
        answer *= matr[alph2.index(str2[i])][alph1.index(str1[i])]

    return answer
if __name__ == "__main__":
    str1, str2, alph1, alph2, matr = read_data("Chapter_Rosalind/ba10b/rosalind_ba10b.txt")
    print (main(str1, str2, alph1, alph2))