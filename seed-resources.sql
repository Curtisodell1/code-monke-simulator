
DROP TABLE IF EXISTS resources;
CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY,
                topic TEXT,
                synopsis TEXT,
                example TEXT,
                relevant_content TEXT
            );

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Arrays and Strings', 'Understanding arrays, strings, and operations like searching, sorting, and manipulation.', 'Given an array, find the maximum element.', 'https://www.geeksforgeeks.org/array-data-structure/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Linked Lists', 'Types of linked lists (singly, doubly, circular) and common operations like insertion and deletion.', 'Reverse a singly linked list.', 'https://www.geeksforgeeks.org/data-structures/linked-list/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Stacks and Queues', 'Implementing stacks and queues, and their use in solving problems.', 'Evaluate a postfix expression using a stack.', 'https://www.geeksforgeeks.org/stack-data-structure/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Trees (Binary, AVL, Red-Black)', 'Tree data structures, traversal algorithms, and balanced trees.', 'Find the lowest common ancestor in a binary tree.', 'https://www.geeksforgeeks.org/binary-tree-data-structure/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Graphs (DFS, BFS, Topological Sort)', 'Graph representations, traversal, shortest path, and topological sorting.', 'Perform breadth-first search (BFS) on a graph.', 'https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Dynamic Programming', 'Techniques for solving complex problems using dynamic programming.', 'Solve the Fibonacci sequence using dynamic programming.', 'https://www.topcoder.com/thrive/articles/Dynamic%20Programming:%20From%20Novice%20to%20Advanced');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Sorting Algorithms (Quick, Merge, etc.)', 'Various sorting algorithms and their time complexity analysis.', 'Implement the merge sort algorithm.', 'https://www.toptal.com/developers/sorting-algorithms');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Hashing and Hash Tables', 'Hashing principles, collision resolution, and hash table implementation.', 'Create a hash table with collision handling.', 'https://www.geeksforgeeks.org/hashing-data-structure/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Heap Data Structure', 'Binary heaps, priority queues, and their applications.', 'Implement a min-heap data structure.', 'https://www.geeksforgeeks.org/heap-data-structure/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Trie Data Structure', 'Trie (prefix tree) data structure and its use in efficient string search.', 'Implement an autocomplete system using a trie.', 'https://www.geeksforgeeks.org/trie-insert-and-search/');

INSERT INTO resources(topic, synopsis, example, relevant_content, id=None) 
VALUES ('Greedy Algorithms', 'Solve problems by making locally optimal choices at each step.', 'Implement the Huffman coding algorithm.', 'https://www.geeksforgeeks.org/greedy-algorithms/');