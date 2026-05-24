# Custom Hash Table Implementation

A robust implementation of a Hash Table data structure built from scratch in Python. This project demonstrates foundational knowledge of data structures, hashing functions, and collision resolution strategies.

## 🚀 Key Features
- **Custom Hashing:** Uses a Unicode-summation algorithm to map keys to indices.
- **Collision Handling:** Implements "Chaining" using nested dictionaries to ensure data integrity when multiple keys hash to the same value.
- **Core Operations:** Fully functional `add`, `remove`, and `lookup` methods.

## 🛠️ Technical Stack
- **Language:** Python 3
- **Concepts:** Hashing, Data Structures, Dictionary Manipulation, Time Complexity

## 🧩 How it Works
The Hash Table functions as an indexed warehouse. Each key is passed through a hashing function to determine its "shelf" (the hash value). If multiple items share a shelf (collision), they are stored in a nested dictionary within that index.



```mermaid
graph TD
    A[Input Key] --> B(Hash Function)
    B --> C{Hash Value}
    C --> D[Nested Dictionary]
    D --> E[Key-Value Pair 1]
    D --> F[Key-Value Pair 2]
