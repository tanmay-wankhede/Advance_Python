from multiprocessing import Pool 

def cube(number):
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool()

    # by default this allocate the max num of available 
    result = p.map(cube,  numbers)

    #pool.apply(cube, numbers[0])

    #result = [p.apply(cube, args=(i,)) for i in numbers]

    p.close()
    p.join()
    
    print(result)
