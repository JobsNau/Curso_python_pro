def is_primo(number:int)->bool:
    a=True
    for i in range(2,number):
        if number%i==0:
            a=False
    return a
def run():
    c=4
    print(is_primo(c))

if __name__=="__main__":
    run()