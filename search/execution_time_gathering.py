import random
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Callable

from search import data_generator, algorithms, constants


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print(f"Processing size: {size}")
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)
    return return_table


def take_times(size, samples_by_size):
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


def take_time_for_algorithm(samples_array, targets, search_approach):
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


def measure_time(func: Callable, arr: List[int], target: int) -> float:
    start_time = time.perf_counter()
    for _ in range(1000):  # Repeat 1000 times
        func(arr, target)
    return (time.perf_counter() - start_time) / 1000  # Average per search


def compare_and_plot_algorithms(sizes: List[int], algorithms: Dict[str, Callable], repetitions: int = 5):
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
