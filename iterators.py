import time

class fiboIter():

    def __init__(self, max:int):
        self.maximo=max

    def __iter__(self):
        self.n1=0
        self.n2=1
        self.counter=0
        return self

    def __next__(self):
        if self.counter==0:
            self.counter+=1
            return self.n1
        elif self.counter==1:
            self.counter+=1
            return self.n2
        else:
            self.aux=self.n1+self.n2
            if self.aux<=self.maximo:
                #self.n1=self.n2
                #self.n2=self.aux
                self.n1, self.n2=self.n2, self.aux
                return self.aux
            else:
                raise StopIteration

if __name__=="__main__":
    finonachi=fiboIter(20)
    for element in finonachi:
        print(element)
        time.sleep(0.2)
