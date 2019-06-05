f = open("host_grades.txt", "r")

lookup_grade = ':\"F\"'
lookup_err = ':\"Unable to connect to the server\"'

for line in f.readlines():
    if lookup_err in line:
        print("Connection Error: " + str(line))

    if lookup_grade in line:
        ip_addr = line.split(":")
        print("Server received grade F at: " + str(ip_addr[0]))

f.close()