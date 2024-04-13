import sys
file_input = sys.argv[1]
file_output= sys.argv[2]
f = open(file_output, "w")
f.write('file_input')
f.close()