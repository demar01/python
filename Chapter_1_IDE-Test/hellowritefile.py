import sys
output_file = sys.argv[1]
output_prefix = sys.argv[2]

print(f"The program: {sys.argv[0]} will write to {output_file}{output_prefix}")


def write_expected(output_file, output_prefix):
    output_file_final = output_file + output_prefix

    with open(output_file_final, "w+") as out:
        for count, text, in enumerate(range(10)):
            out.write( "Content of the" + str(count) + " row of the new file" + "\n")

write_expected(output_file, output_prefix)


#python3 Chapter_1_IDE-Test/hellowritefile.py demofile2 test_1