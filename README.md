# Leetcode 2021
I will use this repo to solve leetcode questions by topic (for the most part, some are unsorted)

lang: python

## To do's
- Review all the sorting algorithms, what they do and their consequesnt space/time complexity
- practise converting between recurrsive and iterative solutions
- keep going down list of type of problems
- Look into union find


## To come back to

## Lessons
### General
- When doing loops by index, make sure to update the index to the next postion to avoid inifinite loops
- "++" is not an operation in python
- In the container with most water problem, area if formed by width*min(left height, right height). A two pointer solution is natural here because, as width decreases -> area is limited by the height of the smaller one, so you must move the smaller one. Look for problems where moving one index must force only one other possible change in index. Two pointer solution are likely here
- Hash Sets in python are types like {"item1", "item2", "item3"}. Dicts, without the values as one would expect. 
- You can hash immutable objects in python. since lists and sets are mutable -> they can't be hashed. But variations of those objects, like frozensets, which are immutable are hashable
- set.add() does not actually return the resulting set. 
- use constructors to make deep copies of objects. Python copies everything by reference/pointer
- have you considered actually reading the problem you are soling before solving it. smh.
- list.sort() will sort the list
- `diff = float('inf')` gives you infinity in float
- remember to account for length of stack when doing memory complexity calc

### Array
- sort+2 pointer combos allow you to move closer to a sum in linear time

### Backtracking
- 

### Heap
- import heappq
- heappq.heap




