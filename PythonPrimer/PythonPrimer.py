import sys

if len(sys.argv) > 1:
    print("parametar je prosledjen")
    name= sys.argv[1]
    print("arg is: ", sys.argv[1])
else:
    print("ima vise argumenata neg sto je potrebno")
    sys.exit()
x = [(1,2),(3,4),(5,6),(7,8),(9,10)]

dictionary = {name:x}
dictionary["asdf"]=5

for key, value in dictionary.items():
    print("Key value: ",key, "|| Name Value: ",value)
#def main():
    