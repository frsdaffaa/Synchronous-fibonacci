import time

def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    FibSeries = [0,1]
    for n in range(2,100): 
        new_series = FibSeries[n-1] + FibSeries[n-2]
        FibSeries.append(new_series)
    if x in FibSeries:
        print(x, True)
    else:
        print(x, False)  

start = time.perf_counter()

for num in range(1,10):
    find_fibonacci(num)

finish = time.perf_counter()

executed_time = round(finish - start, 5)
print(f"Finished in {executed_time} second(s)")