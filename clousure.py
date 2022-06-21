
def make_repeater_of(n):
    def repeater(string):
        assert type(string)==str, "Solo puedes utilizar cadenas"
        return string*n
    return repeater

def run():
    repeater_5=make_repeater_of(5)
    print(repeater_5("Hola"))
    repeater_10 = make_repeater_of(10)
    print(repeater_5("Nuevo "))

if __name__=="__main__":
    run()