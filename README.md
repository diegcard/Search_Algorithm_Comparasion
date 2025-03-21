# 🔍 Search Algorithms Performance Analysis

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/diegcard/search_algorithm_comparison?style=social)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**A comprehensive analysis of common search algorithms and their performance metrics**

</div>

## 📋 Table of Contents
- [Overview](#-overview)
- [Algorithms](#-algorithms)
- [Results](#-results)
- [Installation](#-installation)
- [Usage](#-usage)
- [Testing & Code Quality](#-testing--code-quality)
- [Author & Credits](#-author--credits)

## 🔎 Overview

This project provides an in-depth study of various search algorithms, analyzing their time complexity and real-world performance across different array sizes.

**Algorithms Analyzed:**
- Linear Search
- Binary Search
- Jump Search
- Exponential Search
- Interpolation Search
- Ternary Search

## 🧮 Algorithms

### Linear Search
<details>
<summary>Implementation & Analysis</summary>

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

**Complexity:**
- **Time Complexity (Worst):** O(n)
- **Time Complexity (Best):** O(1)
- **Time Complexity (Average):** O(n)
- **Space Complexity:** O(1)

</details>

### Binary Search
<details>
<summary>Implementation & Analysis</summary>

```python
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
```

**Complexity:**
- **Time Complexity (Worst):** O(log n)
- **Time Complexity (Best):** O(1)
- **Time Complexity (Average):** O(log n)
- **Space Complexity:** O(1)

</details>

### Jump Search
<details>
<summary>Implementation & Analysis</summary>

```python
import math

def jump_search(arr, target):
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


```

**Complexity:**
- **Time Complexity (Worst):** O(√n)
- **Time Complexity (Best):** O(1)
- **Time Complexity (Average):** O(√n)
- **Space Complexity:** O(1)

</details>

### Exponential Search

<details>
<summary>Implementation & Analysis</summary>

```python
def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i *= 2
    return binary_search(arr[:min(i, len(arr))], x)
```

**Complexity:**
- **Time Complexity (Worst):** O(log n)
- **Time Complexity (Best):** O(1)
- **Time Complexity (Average):** O(log n)
- **Space Complexity:** O(1)

</details>

### Interpolation Search

<details>
<summary>Implementation & Analysis</summary>

```python
def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (x - arr[low])
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

**Complexity:**
- **Time Complexity (Worst):** O(log log n)
- **Time Complexity (Best):** O(1)
- **Time Complexity (Average):** O(log log n)
- **Space Complexity:** O(1)

</details>

### Ternary Search

<details>
<summary>Implementation & Analysis</summary>

```python
def ternary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif x < arr[mid1]:
            high = mid1 - 1
        elif x > arr[mid2]:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1
    return -1
```

**Complexity:**
- **Time Complexity (Worst):** O(log n)
- **Time Complexity (Best):** O(1)
- **Time Complexity (Average):** O(log n)
- **Space Complexity:** O(1)

</details>



## 📊 Results

### Performance Comparison

The following table shows the execution time (in milliseconds) for each algorithm across different array sizes:

<div align="center">

| Size   | Linear | Binary | Jump | Exp | Interp | Ternary |
|--------|--------|--------|------|-----|--------|---------|
| 10000  | 15     | 0      | 0    | 0   | 0      | 0       |
| 20000  | 32     | 0      | 0    | 0   | 0      | 0       |
| 30000  | 52     | 0      | 0    | 0   | 0      | 0       |
| 40000  | 73     | 0      | 0    | 0   | 0      | 0       |
| 50000  | 93     | 0      | 0    | 0   | 0      | 0       |
| 60000  | 114    | 0      | 0    | 0   | 0      | 0       |
| 70000  | 134    | 0      | 0    | 0   | 0      | 0       |
| 80000  | 155    | 0      | 0    | 0   | 0      | 0       |
| 90000  | 175    | 0      | 0    | 0   | 0      | 0       |
| 100000 | 196    | 0      | 0    | 0   | 0      | 0       |

</div>

### Visualization

<div align="center">
<img src="images/comparison_bar.png" alt="Bar Chart Comparison" width="80%">
<img src="images/comparison_log.png" alt="Logarithmic Scale Comparison" width="80%">
</div>

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/diegcard/search_algorithm_comparison.git
cd search_algorithm_comparison

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python app.py
```

## 📂 Project Structure

```
search_algorithm_comparison/
├── app.py                     # Main script
├── algorithms/                # Algorithm implementations
├── data/                      # Test datasets
├── visualizations/            # Chart generation
├── tests/                     # Unit tests
├── results/                   # Analysis results
└── requirements.txt           # Dependencies
```

## 👨‍💻 Author & Credits

- **Author:** [Diego Cardenas](https://github.com/diegcard)
- **Institution:** Escuela Colombiana de Ingeniería Julio Garavito
- **Professor:** [Rafael Niquefa](https://github.com/niquefa)
- **Course:** Algorithms and Data Representation
- **Date:** March 2025

