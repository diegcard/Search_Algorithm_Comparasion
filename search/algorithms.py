from typing import List, Optional
import math


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Linear Search implementation
    Time Complexity: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Binary Search implementation (requires sorted array)
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def jump_search(arr: List[int], target: int) -> Optional[int]:
    """Jump Search implementation (requires sorted array)
    Time Complexity: O(√n)
    """
    n = len(arr)
    step = int(math.sqrt(n))

    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return None


def exponential_search(arr: List[int], target: int) -> Optional[int]:
    """Exponential Search implementation (requires sorted array)
    Time Complexity: O(log n)
    """
    n = len(arr)
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None