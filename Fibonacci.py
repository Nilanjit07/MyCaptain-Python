n1 =0
n2 =1
nterms = int(input("enter no of fibonacci terms to be displayed : "))
if nterms<=0 :
     print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else :
    for i in range(nterms):
        print(n1)
        x = n1 + n2
        n1 = n2
        n2 = x
