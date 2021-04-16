import sys
import logging

logging.basicConfig(filename='Chapter_1_IDE-Test/hello_write_logfile.log',level=logging.INFO)
logging.debug('This message should go to the log file if level is set to DEBUG')
logging.info('This message only should go to the log file if level is set to INFO')


output_file = sys.argv[1]
output_prefix = sys.argv[2]

#note that the executed file will be printed out in capital letters
print(f"The program: {sys.argv[0].upper()} will write to {output_file}{output_prefix}")

def write_expected(output_file, output_prefix):
    output_file_final = output_file + output_prefix

    with open(output_file_final, "w+") as out:
        for count, text, in enumerate(range(10)):
            out.write( "Content of the " + str(count) + " row of the new file" + "\n")

write_expected(output_file, output_prefix)


#python3 Chapter_1_IDE-Test/hellowritefile.py Chapter_1_IDE-Test/demofile2 test_1