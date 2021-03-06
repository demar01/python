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
	first_parent = tax_dict.get(taxon)
	second_parent = tax_dict.get(first_parent)
	third_parent = tax_dict.get(second_parent)
	return[first_parent, second_parent, third_parent]

print ('Ancestors of Hominoidea are' + str((get_ancestors('Hominoidea'))))

t = time.time()
get_ancestors('Hominoidea')
elapsed = time.time() - t

print(f'Iteration takes takes {elapsed}. Iteration consumes CPU and tends to be faster than recursion.' )