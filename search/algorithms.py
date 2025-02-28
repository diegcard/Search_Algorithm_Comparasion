from typing import List, Optional
import math


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Linear Search implementation
    Time Complexity: O(n)
    """
    for i in range(len(arr)): # O(n)
        if arr[i] == target: # O(1)
            return i # O(1)
    return None # O(1)


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Binary Search implementation (requires sorted array)
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1 # O(1)
    while left <= right: # O(log n)
        mid = (left + right) // 2 # O(1)
        if arr[mid] == target: # O(1)
            return mid # O(1)
        elif arr[mid] < target: # O(1)
            left = mid + 1 # O(1)
        else: # O(1)
            right = mid - 1 # O(1)
    return None # O(1)


def jump_search(arr: List[int], target: int) -> Optional[int]:
    """Jump Search implementation (requires sorted array)
    Time Complexity: O(√n)
    """
    n = len(arr) # O(1)
    step = int(math.sqrt(n)) # O(1)

    prev = 0 # O(1)
    while arr[min(step, n) - 1] < target: # O(√n)
        prev = step # O(1)
        step += int(math.sqrt(n)) # O(1)
        if prev >= n: # O(1)
            return None # O(1)

    for i in range(prev, min(step, n)): # O(√n)
        if arr[i] == target: # O(1)
            return i # O(1)
    return None # O(1)


def exponential_search(arr: List[int], target: int) -> Optional[int]:
    """Exponential Search implementation (requires sorted array)
    Time Complexity: O(log n)
    """
    n = len(arr) # O(1)
    if arr[0] == target: # O(1)
        return 0 # O(1)

    i = 1 # O(1)
    while i < n and arr[i] <= target: # O(log n)
        i *= 2 # O(1)

    left = i // 2 # O(1)
    right = min(i, n - 1) # O(1)
    while left <= right: # O(log n)
        mid = (left + right) // 2 # O(1)
        if arr[mid] == target: # O(1)
            return mid # O(1)
        elif arr[mid] < target: # O(1)
            left = mid + 1 # O(1)
        else: # O(1)
            right = mid - 1 # O(1)
    return None # O(1)
