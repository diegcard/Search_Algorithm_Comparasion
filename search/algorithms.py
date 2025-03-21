from typing import List, Optional
import math


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """
    Linear Search - O(n)

    Sequentially checks each element in the array until the target is found or the end is reached.

    Args:
        arr (List[int]): The input array (unsorted or sorted).
        target (int): The value to search for.

    Returns:
        Optional[int]: Index of the target if found, None otherwise.

    Time Complexity:
        - Average: O(n) - Linear time proportional to the array size.
        - Best Case: O(1) - Target is at the first position (index 0).
        - Worst Case: O(n) - Target is at the last position or not present, requiring full traversal.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Binary Search - O(log n)

    Divides the search space in half repeatedly by comparing the target with the middle element.

    Args:
        arr (List[int]): The input sorted array.
        target (int): The value to search for.

    Returns:
        Optional[int]: Index of the target if found, None otherwise.

    Time Complexity:
        - Average: O(log n) - Logarithmic time due to halving the search space each step.
        - Best Case: O(1) - Target is at the middle of the array on the first iteration.
        - Worst Case: O(log n) - Target is at an extreme or not present, requiring log₂(n) iterations.
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
    """
    Jump Search - O(√n)

    Jumps ahead by fixed steps (√n) and performs a linear search within the identified block.

    Args:
        arr (List[int]): The input sorted array.
        target (int): The value to search for.

    Returns:
        Optional[int]: Index of the target if found, None otherwise.

    Time Complexity:
        - Average: O(√n) - Square root time due to jumping and linear search in a block.
        - Best Case: O(1) - Target is found in the first jump or very early.
        - Worst Case: O(√n) - Target is near the end or not present, requiring ~√n jumps + ~√n steps.
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
    """
    Exponential Search - O(log n)

    Finds a range where the target might exist by exponentially increasing the bound, then uses binary search.

    Args:
        arr (List[int]): The input sorted array.
        target (int): The value to search for.

    Returns:
        Optional[int]: Index of the target if found, None otherwise.

    Time Complexity:
        - Average: O(log n) - Logarithmic time for range finding and binary search.
        - Best Case: O(1) - Target is at the first position (index 0).
        - Worst Case: O(log n) - Target is near the end, requiring log₂(i) + binary search steps.
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


def interpolation_search(arr: List[int], target: int) -> Optional[int]:
    """
    Interpolation Search - O(log log n) average, O(n) worst

    Estimates the position of the target based on linear interpolation, then adjusts bounds.

    Args:
        arr (List[int]): The input sorted array (ideally uniformly distributed).
        target (int): The value to search for.

    Returns:
        Optional[int]: Index of the target if found, None otherwise.

    Time Complexity:
        - Average: O(log log n) - Very efficient for uniformly distributed data.
        - Best Case: O(1) - Target is found on the first probe.
        - Worst Case: O(n) - Data is exponentially distributed, degrading to linear search.
    """
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            return left if arr[left] == target else None
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        pos = max(left, min(right, pos))  # Ensure bounds
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return None


def ternary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Ternary Search - O(log₃ n)

    Divides the search space into three parts and eliminates one-third each iteration.

    Args:
        arr (List[int]): The input sorted array.
        target (int): The value to search for.

    Returns:
        Optional[int]: Index of the target if found, None otherwise.

    Time Complexity:
        - Average: O(log₃ n) - Logarithmic time base 3, slightly slower than binary search.
        - Best Case: O(1) - Target is at a midpoint in the first iteration.
        - Worst Case: O(log₃ n) - Target is at an extreme or not present, requiring log₃(n) steps.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return None