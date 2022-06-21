from datetime import datetime

def remove_duplicate(some_list):
    without_duplicates=[]
    for elements in some_list:
        if elements not in without_duplicates:
            without_duplicates.append(elements)
    return without_duplicates

def run():
    ramdom_list=[1,1,2,2,4]
    a=set(ramdom_list)
    my_time=datetime.now()
    print(my_time.strftime('%d/%m/%Y'))
    print(list(a))

if __name__=="__main__":
    run()