import timeit
import matplotlib.pyplot as plt
def F_recursive(n):
    if n <= 1:
        return n
    else:
        return F_recursive(n-1) + F_recursive(n-2)

def F_dynamic(n):
    if n <= 1:
        return n
    else:
        memo = [0] * (n+1)
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

recursive_times = []
dynamic_times = []
start_time = timeit.default_timer()
for n in range(10, 101, 10):
    recursive_time = timeit.timeit(lambda: F_recursive(n), number=10)
    recursive_times.append(recursive_time)

    dynamic_time = timeit.timeit(lambda: F_dynamic(n), number=10)
    dynamic_times.append(dynamic_time)

    elapsed_time = timeit.default_timer() - start_time
    if elapsed_time > 3600:
        print('Elapsed time exceeded 1 hour. Stopping loop.')
        break



plt.plot(range(10, n+1, 10), recursive_times, label='Recursive')
plt.plot(range(10, n+1, 10), dynamic_times, label='Dynamic')
plt.xlabel('n')
plt.ylabel('Execution time (s)')
plt.title(f'Execution time of F(n) for n=10,...,{n}')
plt.legend()
plt.show()
