# Leetcode 2021
I will use this repo to solve leetcode questions by topic

lang: python


## Lessons
### General
- When doing loops by index, make sure to update the index to the next postion to avoid inifinite loops
- "++" is not an operation in python
- In the container with most water problem, area if formed by width*min(left height, right height). A two pointer solution is natural here because, as width decreases -> area is limited by the height of the smaller one, so you must move the smaller one. Look for problems where moving one index must force only one other possible change in index. Two pointer solution are likely here

### Array
- 