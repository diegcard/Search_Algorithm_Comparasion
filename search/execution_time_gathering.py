import random
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Callable

from search import data_generator, algorithms, constants

def take_execution_time(minimum_size: int, maximum_size: int, step: int, samples_by_size: int) -> List[List[int]]:
    """
    Measure the execution time of search algorithms over a range of input sizes.

    Args:
        minimum_size (int): The minimum size of the input array.
        maximum_size (int): The maximum size of the input array.
        step (int): The step size to increment the input array size.
        samples_by_size (int): The number of samples to generate for each input size.

    Returns:
        List[List[int]]: A table of execution times for each input size and algorithm.
    """
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print(f"Processing size: {size}")
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)
    return return_table

def take_times(size: int, samples_by_size: int) -> List[int]:
    """
    Generate samples and measure the execution time for each search algorithm.

    Args:
        size (int): The size of the input array.
        samples_by_size (int): The number of samples to generate.

    Returns:
        List[int]: A list of median execution times for each search algorithm.
    """
    samples = []
    targets = []
    for _ in range(samples_by_size):
        arr = data_generator.get_random_sorted_list(size)
        samples.append(arr)
        targets.append(random.choice(arr))

    return [
        take_time_for_algorithm(samples, targets, algorithms.linear_search),
        take_time_for_algorithm(samples, targets, algorithms.binary_search),
        take_time_for_algorithm(samples, targets, algorithms.jump_search),
        take_time_for_algorithm(samples, targets, algorithms.exponential_search),
    ]

def take_time_for_algorithm(samples_array: List[List[int]], targets: List[int], search_approach: Callable[[List[int], int], int]) -> int:
    """
    Measure the execution time for a specific search algorithm.

    Args:
        samples_array (List[List[int]]): A list of input arrays.
        targets (List[int]): A list of target values to search for.
        search_approach (Callable[[List[int], int], int]): The search algorithm to measure.

    Returns:
        int: The median execution time for the search algorithm.
    """
    times = []
    for sample, target in zip(samples_array, targets):
        # Perform multiple searches to accumulate measurable time
        start_time = time.perf_counter()
        for _ in range(1000):  # Repeat 1000 times
            search_approach(sample, target)
        elapsed = (time.perf_counter() - start_time) * constants.TIME_MULTIPLIER / 1000  # Average per search
        times.append(int(elapsed))
    times.sort()
    return times[len(times) // 2]

def measure_time(func: Callable[[List[int], int], int], arr: List[int], target: int) -> float:
    """
    Measure the execution time of a search function.

    Args:
        func (Callable[[List[int], int], int]): The search function to measure.
        arr (List[int]): The input array.
        target (int): The target value to search for.

    Returns:
        float: The average execution time per search.
    """
    start_time = time.perf_counter()
    for _ in range(1000):  # Repeat 1000 times
        func(arr, target)
    return (time.perf_counter() - start_time) / 1000  # Average per search

def compare_and_plot_algorithms(sizes: List[int], algorithms: Dict[str, Callable[[List[int], int], int]], repetitions: int = 5):
    """
    Compare the execution times of different search algorithms and plot the results.

    Args:
        sizes (List[int]): A list of input array sizes to test.
        algorithms (Dict[str, Callable[[List[int], int], int]]): A dictionary of search algorithms to compare.
        repetitions (int, optional): The number of repetitions for each size. Defaults to 5.
    """
    results = {name: [] for name in algorithms}

    for size in sizes:
        print(f"Testing size {size}")
        data = data_generator.get_random_sorted_list(size)
        target = random.choice(data)
        for name, func in algorithms.items():
            times = []
            for _ in range(repetitions):
                execution_time = measure_time(func, data, target)
                times.append(execution_time)
            results[name].append(np.mean(times))

    # Regular plot
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker="o", label=name)
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Search Algorithms Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparison_regular.png")
    plt.close()

    # Logarithmic plot
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.loglog(sizes, times, marker="o", label=name)
    plt.xlabel("Array Size (log)")
    plt.ylabel("Time (seconds) (log)")
    plt.title("Search Algorithms Comparison (Log Scale)")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparison_log.png")
    plt.close()