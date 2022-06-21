import time

def fibo_gen(a):
    n1=0
    n2=1
    counter=0
    aux=0

    while a>aux:
        if counter==0:
            counter+=1
            yield n1
        elif counter==1:
            counter+=1
            yield n2
        else:
            counter+=1
            aux=n1+n2
            n1, n2=n2, aux
            yield aux

if __name__=="__main__":
    fibonachi=fibo_gen(10)
    for elements in fibonachi:
        print(elements)
        time.sleep(1)