#Question 2

sports = ["basketball", "softball", "football", "baseball", "track"]

filename = "sports.txt"
outfile = open(filename, "w")
outfile.writelines(i + '\n' for i in sports)
outfile.close()

infile = open(filename, "r")
for i in infile:
    print (i, end="")
infile.close()