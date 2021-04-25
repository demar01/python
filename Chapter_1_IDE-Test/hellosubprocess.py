import subprocess

print(subprocess.call(['ls', '-1'], shell=True))


#to run salmon 

# #command = ['salmon', 'index', '-t', args.txfasta, '-i', 'txfasta.idx', '--type', 'quasi', '-k', '31', '--keepDuplicates']
# print('Indexing transcripts...')
# #subprocess.call(command)
# print('Done indexing!')

output = subprocess.check_output(['ls', '-1'])
print ('Have %d bytes in output' % len(output))
print (output)