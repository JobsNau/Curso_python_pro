from datetime import datetime

def time_execution(funci):
    def wrapper(*args, **kwargs):
        initial_time=datetime.now()
        funci(*args, **kwargs)
        final_time=datetime.now()
        time_lapse=final_time-initial_time
        print(f"Pasaron {time_lapse} segundos")
    return wrapper

@time_execution
def random_func():
    for _ in range(1,100000000):
        pass

@time_execution
def suma(a:int, b:int)-> int:
    return a+b

if __name__=="__main__":
    #random_func()
    suma(3,5)
