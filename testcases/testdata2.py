# file=open('C:/Users/srika/PycharmProjects/automation/Pytestframwork1/testcases/dtt.txt')
# for line in file:
#         x = line.split(',')[1]
        # do something with x
        # print(x)
#-------------------------------------------------------------------------------------------------
# import  csv
# with open('C:/Users/srika/PycharmProjects/automation/Pytestframwork1/testcases/tdat2.csv') as  file:
#     read1=csv.reader(file)
    # print(next(read1))
#-------------------------------------------------------------------------------------------------
# import csv
# with open('C:/Users/srika/PycharmProjects/automation/Pytestframwork1/testcases/tdat2.csv') as file1:
#     csvreader = csv.reader(file1)
#     header = next(csvreader)
#     print(header)
#---------------------------------------------------------------------------------------------------
# import csv
#
# with open('C:/Users/srika/PycharmProjects/automation/Pytestframwork1/testcases/tdat2.csv') as inf:
#         csvReader = csv.reader(inf)
#         for row in csvReader:
#             s=row[1]
#             print(s)
# ---------------------------------------------------------------------------------------------
coloumn2 = []
with open(r"C:/Users/srika/PycharmProjects/automation/Pytestframwork1/testcases/dtt.txt", "r+") as f:
    data = f.readlines()
    # print(data)
    for line in data:
        sr=line.split(',')[0]
        print(sr)


