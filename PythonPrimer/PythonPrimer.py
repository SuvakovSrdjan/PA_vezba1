import sys

print("__name__ value: ",__name__)

print("MAIN: Hello bithces!")

print('MAIN: Butches Hello!')

def myfoo(arg1):
    print("MAIN: Hello from foo fighter!")
    print(arg1);
   

def main():
    print("MAIN: Harro fromu maino!")
    myfoo("MAIN: myfood from main!")

if __name__ == "__main__":
        print("MAIN: Hello from exe module")
else:
    print("MAIN: Hello from the other side")
main()