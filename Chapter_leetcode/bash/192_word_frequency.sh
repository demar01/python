cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'

# tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -r | awk '{print $2, $1}'

# cat words.txt | sed 's/\ /\n/g' | sort | uniq -c |sort -r | awk '{print $2,$1}'