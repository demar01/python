
def isIsomorphic(s,t):
    S, T, j, k = {} ,{}, 0, 0
    for a,b in zip(s,t):
        if a not in S: S[a], j = j, j + 1
        if b not in T: T[b], k = k, k + 1
    print(S, T)
    return all([S[s[i]] == T[t[i]] for i in range(len(s))])


s = "egg"; t = "add"
isIsomorphic(s,t)