## Learning Objectives

- The students should be able to apply the concept of recursion to solve problems by implementing recursive functions in Python.
- The students should be able to understand the importance of base cases in recursion and how they prevent infinite loops.

#### Recursive Functions:
Recursive functions are functions, that will call themselves conditionally until they reach a what we call a base case.

The base case represents the scenario which allows it to finally terminate/return.

Once the base case is reached, each one of the recursive function calls is able to return.

Recursion is often used in scenarios where a problem can be broken down into smaller, similar sub-problems, making it suitable for tasks like tree traversal, searching, sorting, and mathematical computations like factorial calculation.

![factorial](https://www.mathwarehouse.com/programming/images/recusion-factorial-code-animated-gifs.gif)

#### Advantages and Disadvantages of Recursion

##### Advantages
- Recursion can boil large complex problems down in to smaller, more manageable problems
- Elegant and consise structure making them more readable, and easier to follow
- Depending on the language they might also grant a benefit to memory/stack usage
- Can offer a higher level of repeatable expression

#### Disadvantages
- Stack Overflow: Each function call recruits a new stack frame (portion of memory), excessive recursion that can lead to the depletion of system resources
https://www.techtarget.com/whatis/definition/stack-overflow
- Risk of entering into a infinite loop of recursive calls, if the base case is never reached, and the function continues to call itself, it can time out.
- Typically slower than iteration
