import os


"""
Determine the flag of input to the  program

The options I have now are:
    Output to a JSON format
    Only output the hostname, public ip, and the "grade"
    Ignoring mismatch, which is just for the testing
"""
flag = input("Enter a flag: (J)SON, (G)rade, (I)gnore mismatch, or (N)one\r\n")

if flag == 'J' or flag == 'j':
    input_flag = '--json-flat '
    output_file = 'output.json'
elif flag == 'G' or flag == 'g':
    input_flag = '--grade '
    output_file = 'host_grades.txt'
elif flag == 'I' or flag == 'i':
    input_flag = '--ignore mismatch '
    output_file = 'simple_output.txt'
elif flag == 'N' or flag == 'n':
    input_flag = ''
    output_file = 'output.txt'
else:
    print("Invalid input. Exiting")
    exit(-1)


"""
This portion determines if the user is using a single host or a txt file of hosts
If it contains .txt, treat it like a text file input
Otherwise, if it doesn't, treat it as a single host
"""

host = input("Enter a host or a file of hosts. A file must be a text file format with each host on a new line:\r\n")

if '.txt' in host:
    host = '--hostfile ' + str(host)

input_flag += host

"""
Call the GO binary, ssllabs-scan-v3, passing in all of the required flags, outputting that to a file, output.txt
"""
print("Sending results to: " + output_file + "\r\n")
os.system("./ssllabs-scan-v3 " + str(input_flag) + " > " + str(output_file))

