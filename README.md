## 🧠 Week 1 – Foundations (Day 1)

✅ **Goal**: Understand the building blocks of AI: vectors, dot products, and matrix multiplication.

📚 **What I Learned**:
- What is a **vector** and how it represents data in AI systems
- How to measure similarity between vectors using **dot product**
- How **matrix multiplication** simulates passing data between layers in neural networks

🧪 **Code Practice**:
```python
import numpy as np

# Define vectors
a = np.array([1, 2])
b = np.array([3, 4])

# Dot product
dot = np.dot(a, b)
print("Dot product:", dot)  # Output: 11

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print("Matrix result:\n", C)
