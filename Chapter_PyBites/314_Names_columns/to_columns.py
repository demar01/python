from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    result = []
    for idx, name in enumerate(names, 1):
        #to give space of 10 
        result.append(f'| {name:10}')
        # remember modulo % https://divisible.info/Modulo/What-is-2-mod-3.html.
        #wthis will create a new line for multiples of the column. 
        if idx % cols == 0:
            result.append('\n')
            
    
    print(''.join(result))


names = 'Sara Tim Ana Julian'.split()