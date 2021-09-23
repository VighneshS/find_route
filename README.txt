UTA ID: 1001878596

Sivaraman, Vighnesh

Student at The University of Texas at Arlington

Masters in Computer and Information Sciences

Email ID: vxs8596@mavs.uta.edu

# find_route

## Introduction

This is a python application to implement the following tree search algorithms:

1. Informed Search using A* Search Algorithm
2. Uninformed Search using uniform cost search algorithm

## How to run

1. We need to install Python >=3.9. The application was developed in python 3.9. We will be able to get it in the
   [following URL](https://www.python.org/downloads/)
2. Next we need to open the command line interface i.e., CMD in windows and terminal in linux or Macintosh operating
   systems, at the directory of the [find_route.py](find_route.py)
3. Be ready with the input files which are similar to [input1.txt](input1.txt) and the [h_kassel.txt](h_kassel.txt) for
   giving input regarding the links and heuristic values respectively.
4. In the command line interface use any of the following commands to get the output accordingly:

```
find_route.py <links_file_location> <start_node> <end_node> <heuristic_file_location | optional>
```

Where,

- `links_file_location` is the file which holds the information about individual links and their cost similar to the
  format of [input1.txt](input1.txt)
- `start_node` is the origin node from which we need to start searching the route to `end_node` which is the destination
  node.
- `heuristic_file_location` is an optional file location which when given will make the program to perform informed
  search algorithm which is similar to the [h_kassel.txt](h_kassel.txt) file.

## Sample input and output:

### Uninformed Search:

- Input:

```
find_route.py input1.txt Bremen Kassel
```

- Output:

```
Nodes Popped: 27
Nodes Expanded: 11
Nodes Generated: 38
Distance: 297.0 km
Route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km
```

### Informed Search:

- Input:

```
find_route.py input1.txt Bremen Kassel h_kassel.txt
```

- Output:

```
Nodes Popped: 3
Nodes Expanded: 2
Nodes Generated: 8
Distance: 297.0 km
Route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km
```

### Infinite Distance i.e., No Route between start and end node:

- Output:

```
Nodes Popped: 14
Nodes Expanded: 7
Nodes Generated: 14
Distance: Infinity km
Route:
None
  ```

## About the Author:

UTA ID: 1001878596

Sivaraman, Vighnesh

Student at The University of Texas at Arlington

Masters in Computer and Information Sciences

Email ID: vxs8596@mavs.uta.edu

## References

- [Basic Difference between the Uniform Cost Search and A* search](https://stackoverflow.com/questions/44151713/what-is-the-difference-between-uniform-cost-search-and-best-first-search-methods)