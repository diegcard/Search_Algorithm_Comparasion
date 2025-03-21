from search.algorithms import (
    linear_search, binary_search, jump_search, exponential_search,
    interpolation_search, ternary_search
)
from search.execution_time_gathering import compare_and_plot_algorithms, take_execution_time

def run_comparison():
    sizes = [10000, 15000, 20000, 25000, 30000, 35000, 40000]
    algorithms = {
        "Linear Search": linear_search,
        "Binary Search": binary_search,
        "Jump Search": jump_search,
        "Exponential Search": exponential_search,
        "Interpolation Search": interpolation_search,
        "Ternary Search": ternary_search,
    }
    compare_and_plot_algorithms(sizes, algorithms)

def run_execution_time_test():
    minimum_size = 10000
    maximum_size = 50000
    step = 10000
    samples_by_size = 7
    table = take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print("Size  | Linear | Binary | Jump | Exp | Interp | Ternary")
    print("-" * 60)
    for row in table:
        print(f"{row[0]:5d} | {row[1]:6d} | {row[2]:6d} | {row[3]:6d} | {row[4]:6d} | {row[5]:6d} | {row[6]:6d}")

if __name__ == "__main__":
    run_comparison()
    run_execution_time_test()