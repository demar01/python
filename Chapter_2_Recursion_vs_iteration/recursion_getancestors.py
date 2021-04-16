import time
tax_dict = { 
'Pan troglodytes' : 'Hominoidea',       'Pongo abelii' : 'Hominoidea', 
'Hominoidea' :  'Simiiformes',          'Simiiformes' : 'Haplorrhini', 
'Tarsius tarsier' : 'Tarsiiformes',     'Haplorrhini' : 'Primates',
'Tarsiiformes' : 'Haplorrhini',         'Loris tardigradus' : 'Lorisidae',
'Lorisidae' : 'Strepsirrhini',          'Strepsirrhini' : 'Primates',
'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' : 'Strepsirrhini',
'Galago alleni' : 'Lorisiformes',       'Lorisiformes' : 'Strepsirrhini',
'Galago moholi' : 'Lorisiformes'
} 

def get_ancestors(taxon):
	if taxon == 'Primates':
		return [taxon]
	else:
		parent = tax_dict.get(taxon)
		parent_ancestors = get_ancestors(parent) 
		return [parent] + parent_ancestors

print(get_ancestors('Hominoidea'))

t = time.time()
get_ancestors('Hominoidea')
elapsed = time.time() - t

print(f'Recursion takes {elapsed}.Recursion is more expensive than iteration because it requires the allocation of a new stack frame')


