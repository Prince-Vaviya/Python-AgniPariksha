from multiprocessing import Pool

def square_number(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=4) as pool:  
        results = pool.map(square_number, numbers)  
    print(results)  
