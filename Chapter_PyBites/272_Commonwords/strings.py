from typing import List, Set

S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
##                  **                       **
T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']

def _extract_words(sentence: List[str]) -> Set[str]:
    return set(s.lower() for s in sentence)

def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    common = sorted(_extract_words(S).intersection(_extract_words(T))
    unique= sorted(_extract_words(S).symmetric_difference(_extract_words(T))
    return list(common)


common_words(S,T)