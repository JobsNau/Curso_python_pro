def numerador(a):
    def denominador(b):
        return b/a
    return denominador

def run():
    a=int(input())
    b=int(input())
    aa=numerador(a)
    bb=aa(b)
    return print(bb)

if __name__=="__main__":
    run()