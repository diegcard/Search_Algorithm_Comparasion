import random
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Callable
from datetime import datetime

from search import data_generator, algorithms, constants


def take_execution_time(minimum_size: int, maximum_size: int, step: int, samples_by_size: int) -> List[List[int]]:
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print(f"Processing size: {size}")
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)
    return return_table


def take_times(size: int, samples_by_size: int) -> List[int]:
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
        take_time_for_algorithm(samples, targets, algorithms.interpolation_search),
        take_time_for_algorithm(samples, targets, algorithms.ternary_search),
    ]


def take_time_for_algorithm(samples_array: List[List[int]], targets: List[int], search_approach: Callable) -> int:
    times = []
    for sample, target in zip(samples_array, targets):
        start_time = time.perf_counter()
        for _ in range(1000):
            search_approach(sample, -1)  # Worst case
        elapsed = (time.perf_counter() - start_time) * constants.TIME_MULTIPLIER / 1000
        times.append(int(elapsed))
    times.sort()
    return times[len(times) // 2]


def measure_time(func: Callable, arr: List[int], target: int) -> float:
    start_time = time.perf_counter()
    for _ in range(1000):
        func(arr, target)
    return (time.perf_counter() - start_time) / 1000


def compare_and_plot_algorithms(sizes: List[int], algorithms: Dict[str, Callable], repetitions: int = 5):
    results = {name: [] for name in algorithms}
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Gather data
    for size in sizes:
        print(f"Testing size {size}")
        data = data_generator.get_random_sorted_list(size)
        target = random.choice(data)
        for name, func in algorithms.items():
            times = [measure_time(func, data, target) for _ in range(repetitions)]
            results[name].append(np.mean(times))

    # Enhanced Regular Plot
    plt.figure(figsize=(12, 7))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', linewidth=2, label=name)
    plt.xlabel("Array Size", fontsize=12)
    plt.ylabel("Time (seconds)", fontsize=12)
    plt.title("Search Algorithms Comparison", fontsize=14, pad=15)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"images/comparison_regular_{timestamp}.png", dpi=300)
    plt.close()

    # Enhanced Logarithmic Plot
    plt.figure(figsize=(12, 7))
    for name, times in results.items():
        plt.loglog(sizes, times, marker='o', linewidth=2, label=name)
    plt.xlabel("Array Size (log scale)", fontsize=12)
    plt.ylabel("Time (seconds, log scale)", fontsize=12)
    plt.title("Search Algorithms Comparison (Log Scale)", fontsize=14, pad=15)
    plt.legend(fontsize=10)
    plt.grid(True, which="both", linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"images/comparison_log_{timestamp}.png", dpi=300)
    plt.close()

    # Bar Plot for Key Sizes
    key_sizes = [sizes[0], sizes[len(sizes) // 2], sizes[-1]]
    bar_results = {name: [results[name][i] for i in [0, len(sizes) // 2, -1]] for name in algorithms}

    fig, ax = plt.subplots(figsize=(12, 7))
    bar_width = 0.12
    x = np.arange(len(key_sizes))
    for i, (name, times) in enumerate(bar_results.items()):
        plt.bar(x + i * bar_width, times, bar_width, label=name)
    plt.xlabel("Array Size", fontsize=12)
    plt.ylabel("Time (seconds)", fontsize=12)
    plt.title("Algorithm Performance at Key Sizes", fontsize=14, pad=15)
    plt.xticks(x + bar_width * (len(algorithms) - 1) / 2, key_sizes)
    plt.legend(fontsize=10)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"images/comparison_bar_{timestamp}.png", dpi=300)
    plt.close()