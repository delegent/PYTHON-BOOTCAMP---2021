"""files -> 1. Text files -> .txt .py
2. Binary files -> images videos ""

IMportant points
1. Open the file
2. work on the file
3. File ko close krna""

open('file location','mode')
modes:
r -> reading (error)
w -> writing (creates new file)
a -> writing (content ke end me )
r + -> reading and writing ()
w + -> ""
a + -> reading and wrting -<> last
x exculsive mode ->
"
#write

f = open('file1.txt','w');
#text = input("Enter some text : ")
#f.write(text); # it adds the string to the file
l = ["Indore\n","Delhi\n","Kanpur\n","Meerut\n"]
f.writelines(l) # it accepts the list of string
f.close();

f = open('file1.txt','r');
#s = f.read()
#s1 = f.read(7)
#s2 = f.read(7)

#s = f.readline()
s =  f.readlines()
print(s)
f.close();""
f = open('file1.txt','a');
f.write("Anubhav is my name34")
f.close();
""
f = open('file1.txt','r+');
text = input("ENter : ")
f.write(text)
f.close""
f = open('file1.txt','w+');
text = input("ENter : ")
f.write(text)
f.close();""
f = open('file2.txt','x');
text = input("ENter : ")
f.write(text)
f.close();"""


# Exception Handling

#syntax errors
#runtime errors ->(exeptions)
"""
x = int(input("ENter a number")) #int
y = int(input("ENter a number")) # string
print(x / y)
print("After the error")

""
(.py) -> (Exception) -> {DEM(Default Eception Mechanism)} ->
(Console -> eror ("Exception Class Name : error messgae"))-> program end.
""

raise         Handle
python      python
python      user
user            python
user            user

Keywords -
raise
try
except
finally

""
1. try ke andr wo statement likhenge jisme error aani hogi.
2. except hmesha handle krega.
""
x = int(input("Enter a number: ")) #int
y = (input("Enter a number: ")) # string
try:
    print(x + y)
except ZeroDivisionError:
    print("y cannot be 0")
except TypeError:
    print("unsupported type!")

print("After the error")
""
#Default Exception
x = int(input("Enter a number: ")) #int
y = int(input("Enter a number: ")) # string
try:
    print(x / y)
except:
    print("Error")


print("After the error")
""
x = int(input("Enter a number: ")) #int
y = int(input("Enter a number: ")) # string
try:
    print(x /y)
except Exception as e:
    print("Error: ",e)
else:
    print("mai tab chalunga jab error nahi aaegi")
finally:
    print("Hello Hmesha hu mai")

""
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if y == 0:
    raise ZeroDivisionError("y cannot be zero")
z = x / y
print(z)
""
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
try:
    if y == 0:
        raise ZeroDivisionError("y cannot be zero")
    z = x / y
    print(z)
except Exception as e:
    print("Program Error : ",e)
"""
# Program for Insufficient Balance
class InsufficientBalance(ZeroDivisionError):
    def __init__(self,arg):
        self.msg = arg


balance = 5000
w = int(input("Enter Amount to withdraw: "))
try:
    if w > balance:
        raise InsufficientBalance("Incomplete Balance ! ");
    balance = balance - w
except InsufficientBalance as i:
    print("Error : ",i.msg)
else:
    print("Money withdrawn successfully !", w)
finally:
    print("Current Balance ", balance)
    
















