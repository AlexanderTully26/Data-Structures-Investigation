# Data-Structures-Investigation

Learn a little bit more about each of these three data structures. Think about:

What are the defining characteristics of the data structure?
What kinds of data might go into such a data structure? 
What sorts of problems does this data structure solve?
What are some real world applications of this data structure?
Write your responses here. 


## 1. Array
- **Defining Characteristics:** A collection of elements stored in contiguous memory locations, indexed for easy access. Fixed size in most languages.
- **Types of Data:** Integers, floats, characters, objects, etc.
- **Problems It Solves:** Fast access to elements via index, cache-friendly due to memory locality.
- **Real-World Applications:** Storing lists, image processing, database indexing, and scheduling tasks.
  
## 2. Matrix/Grid
- **Defining Characteristics:** A two-dimensional array where elements are arranged in rows and columns. Can extend to multi-dimensional arrays.
- **Types of Data:** Numbers, booleans, characters, objects.
- **Problems It Solves:** Representation of spatial data, structured data storage.
- **Real-World Applications:** Image processing, game maps, scientific computing (e.g., physics simulations), and graphs in adjacency matrix form.
  
## 3. String
- **Defining Characteristics:** A sequence of characters, typically immutable in many languages. Can be treated as an array of characters.
- **Types of Data:** Alphabetic, numeric, and special characters.
- **Problems It Solves:** Text storage, pattern matching, text processing.
- **Real-World Applications:** Search engines, natural language processing (NLP), data compression, and encryption.
  
## 4. Stack
- **Defining Characteristics:** A Last-In-First-Out (LIFO) data structure where elements are added and removed from the top.
- **Types of Data:** Any data type, including function calls, expressions, and operations.
- **Problems It Solves:** Reverse operations, function call tracking, undo operations.
- **Real-World Applications:** Backtracking algorithms (e.g., maze solving), expression evaluation (parsing), browser history, and recursion handling.
  
## 5. Queue
- **Defining Characteristics:** A First-In-First-Out (FIFO) data structure where elements are inserted at the rear and removed from the front.
- **Types of Data:** Tasks, events, messages, etc.
- **Problems It Solves:** Order processing, scheduling, real-time event handling.
- **Real-World Applications:** Print job scheduling, CPU process scheduling, networking (packet queues), and customer service queues.
## 6. Linked List
- **Defining Characteristics:** A collection of nodes where each node stores a value and a reference to the next node. Variants include singly, doubly, and circular linked lists.
- **Types of Data:** Any type of object or primitive data type.
- **Problems It Solves:** Dynamic memory allocation, efficient insertions/deletions.
- **Real-World Applications:** Implementing stacks, queues, file systems, and navigation systems (e.g., browser back/forward history).
  
## 7. Hash (Hash Table / Hash Map)
- **Defining Characteristics:** Key-value storage with a hashing function for fast lookups. Provides average O(1) access time.
- **Types of Data:** Any type of data mapped to unique keys.
- **Problems It Solves:** Fast search, quick data retrieval, caching, reducing duplicate storage.
- **Real-World Applications:** Databases (indexing), caching (e.g., DNS lookups), symbol tables in compilers, and password storage (hashing passwords).

## 8. Tree
- **Defining Characteristics:** A hierarchical structure where each node has a value and references to child nodes.
- **Types of Data:** Any structured data, including hierarchical information.
- **Problems It Solves:** Organizing data in a way that enables efficient searching and hierarchical representation.
- **Real-World Applications:** File systems, organizational charts, decision trees (AI/ML), and XML/JSON parsing.
  
## 9. Binary Tree
- **Defining Characteristics:** A tree where each node has at most two children (left and right).
- **Types of Data:** Any ordered data or data requiring hierarchical organization.
- **Problems It Solves:** Searching, sorting, efficient data retrieval.
- **Real-World Applications: **Expression trees (parsing expressions), game AI (minimax tree), and Huffman coding (data compression).

## 10. Binary Search Tree (BST)
- **Defining Characteristics:** A binary tree where the left subtree contains smaller values, and the right subtree contains larger values.
- **Types of Data:** Numbers, strings, or objects that support ordering.
- **Problems It Solves:** Fast lookup, insertion, and deletion operations (O(log n) time complexity).
- **Real-World Applications:** Database indexing, auto-complete features, and dictionary implementations.

## 11. Heap
- **Defining Characteristics:** A specialized binary tree where the parent node is always smaller (min-heap) or larger (max-heap) than its children.
- **Types of Data:** Priority-based data, such as tasks with urgency levels.
- **Problems It Solves:** Efficient priority queue management, fast retrieval of the highest/lowest priority element.
- **Real-World Applications:** Priority queues (e.g., scheduling algorithms), Dijkstra’s algorithm for shortest paths, and memory allocation (garbage collection).

## 12. Graph
- **Defining Characteristics:** A set of nodes (vertices) connected by edges, which can be directed or undirected, weighted or unweighted.
- **Types of Data:** Entities and relationships between them.
- **Problems It Solves:** Representing complex relationships and network structures.
- **Real-World Applications:** Social networks, GPS navigation, recommendation systems, and circuit design.
  
## 13. Advanced Data Structures

### Trie (Prefix Tree)
- **Defining Characteristics:** A tree-like structure for storing strings efficiently.
- **Types of Data:** Words, sequences, prefixes.
- **Problems It Solves:** Fast prefix searches and autocomplete.
- **Real-World Applications:** Dictionary search, autocomplete, and IP routing.

### Segment Tree
- **Defining Characteristics:** A tree used for range queries and updates.
- **Types of Data:** Numeric data with range-based operations.
- **Problems It Solves:** Fast range queries and updates.
- **Real-World Applications:** Competitive programming, range sum queries, and game development.
  
### Fenwick Tree (Binary Indexed Tree - BIT)
- **Defining Characteristics:** A space-efficient structure for cumulative frequency queries.
- **Types of Data:** Numeric frequency/count data.
- **Problems It Solves:** Efficient prefix sum and range sum calculations.
- **Real-World Applications:** Competitive programming, frequency analysis, and financial data analysis.

### Skip List
- **Defining Characteristics:** A probabilistic alternative to balanced trees, enabling O(log n) lookups.
- **Types of Data:** Ordered elements requiring fast access.
- **Problems It Solves:** Efficient searching and insertions.
- **Real-World Applications:** Databases, in-memory storage, and distributed systems.
