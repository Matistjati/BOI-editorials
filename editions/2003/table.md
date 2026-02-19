# Table Editorial (unofficial)

This editorial only shows one possible way to solve the problem; it is likely that many other solutions exist. In particular, one could probably write a simpler solver for specific $M$ by considering their prime factorization. We will focus on finding the smallest valid $N$ for a given $M$.

## Solving $M=3$

Case 1 has $M=3$, which can easily be solved by hand. A valid optimal table is
```
3 6
9 0
```

## Solving $M=3, 13, 51, 62$

The number of tables with $N$ entries is $10^(N^2)$, which is excessive for $N>3$.

First, we can realize that every row of the table should contain a multiple of $M$. Thus, we can iterate over $N$ from $2$ to $10$, generating all $N \times N$ tables where every row is a multiple of $M$ and checking its validity. To implement it, we can use recursion, deciding an entire row at each step.
By doing a rough estimation of the number of valid $N \times N$ matrices, we can see that this solution can realistically check all $N$ up to $N \leq 4$
If the solution is implemented with good constant factor and run with a timeout of 5 minutes, it gives the following results (- = timeout):

| M    | Result    | N |
| ----------- | ----------- | ----------- |
| 3   | 0s  | 2 |
| 13  | 0s  | 3 |
| 36  | -   | - |
| 45  | -   | - |
| 51  | 70s | 4 |
| 62  | 36s | 4 |
| 125 | -   | - |
| 137 | -   | - |
| 171 | -   | - |
| 259 | -   | - |

## Pruning

If the code has been implemented reasonably, then the bottleneck should be calling the function to check whether a given matrix is valid. Speeding this up can gain us a most a constant factor improvement: we need to be able to check an order of magnitude more matrices, not a constant factor. Thus, let's try returning early in the recursion. At every step in the recursion, we can check for each partially filled column whether there exists some multiple of $M$ that could be placed to complete the column. If not, we can return early. This can be implemented quickly by storing all $M$ in a list of sorted strings, and then binary searching in it. This solution can handle $N \leq 5$.

| M    | Result    | N |
| ----------- | ----------- | ----------- |
| 3   | 0s  | 2 |
| 13  | 0s  | 3 |
| 36  | 1s  | 5 |
| 45  | -   | - |
| 51  | 0.2s | 4 |
| 62  | 0.1s | 4 |
| 125 | -   | - |
| 137 | -   | - |
| 171 | 97s | 5 |
| 259 | -   | - |

## Pruning even more

To solve more cases, we can prune in two ways: first, in the recursion, we compute for every column the set of numbers that can extend this column, and let our candidates for the next row be the intersection of all of these. Second, for every every pair of multiples of $M$, we compute the column sums mod $M$, and store these in a vector keyed by the residues of the columns. When there are only two rows left in the recursion, we can use this lookup table to only check pairs of numbers that will result in correct column residues. Shuffling the candidates seems necessary to find a solution.

| M    | Result    | N |
| ----------- | ----------- | ----------- |
| 3   | 0s  | 2 |
| 13  | 0s  | 3 |
| 36  | 3s  | 5 |
| 45  | -   | - |
| 51  | 0s  | 4 |
| 62  | 0s  | 4 |
| 125 | 99s | 6 |
| 137 | 60s | 6 |
| 171 | 6s  | 5 |
| 259 | 62s | 6 |


## Solving $M=45$
$M=45$ is special: we can prove that there exists no solution for $N \leq 8$. First, for the columns to be divisible by 45, they must also be divisible by 5. The only thing that matters for the columns to be divisible by 5 is that the last digit of the column is 5 or 0. Therefore, the last row must only contain the digits 0 or 5. Further, every row must be divisible by 9, which implies that every row has digit a sum that is a multiple of 9. Thus, the last row must have a sum of at least lcm(5,9)=45, which can be attained by $N=9$ at the smallest (only zeros is not allowed, as this would create leading zeros).

We can also prove that $N=9$ is impossible. The previous argument applies to both rows and columns, which means that the last row and column must consist of only 0 or 5. They can not be zero due to the leading zero requirement, so both must consist entirely of 5. However, this contradicts the requirement that all numbers must be unique, and $N=9$ is this impossible.

Therefore, let's search for a solution with $N=10$ (the statement guarantees that one exists). One construction is as follows: first, set the last row and column to some valid numbers (their exact values don't matter much), and the ones with R set to random values (first row and column must of course not have leading zeros):
```
R R R R R R R R - 5
R R R R R R R R - 0
R R R R R R R R - 5
R R R R R R R R - 5
R R R R R R R R - 5
R R R R R R R R - 5
R R R R R R R R - 5
R R R R R R R R - 5
- - - - - - - - 0 5
5 5 0 5 5 5 5 5 5 5
```

Then, use the row and columns marked with `-` to fix divisibility by 9 for the first 7 rows and columns. Now, what is the probability that this construction works? Let's estimate the probability of success for different parts:
- No duplicate numbers: ~1
- Column 8 and row 8 not being assigned a leading 0: ~8/9 each
- Column 8 and row 8 divisible by 9: ~1/9 each
- Diagonals divisible by 9: ~1/9 each

Thus, the probability of a given sample of this construction working is roughly a 1/7000, which is very good. The actual probability is turns out to be slightly better, although this does not matter.

## More $M$

Assuming my code is bug-free, I have computed the smallest $N$ for some $M$ in the following [table](table-solutions.txt).

$M$ that my code does not manage to solve:

| 85 | 95 | 105 | 115 | 125 | 135 | 145 | 155 | 165 | 175 | 195 | 205 | 215 | 225 | 235 | 245 | 255 |
| -  | -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |  -  |

Empirically, it seems that $M=5$ (mod 10) are the "hardest" $M$. Notably, the backtracker does manage to solve $M=185.

A solution for $M=45$ is as follows:
```
9 7 3 1 7 1 3 1 8 5
9 6 3 4 7 8 3 1 8 5
4 5 8 8 1 7 1 8 3 0
8 3 5 2 7 3 6 8 7 5
3 9 5 1 8 3 6 6 8 5
2 6 7 5 6 4 2 5 3 5
2 7 8 1 6 9 5 1 1 5
9 8 9 2 5 6 1 7 2 5
3 3 1 7 2 8 4 3 0 5
5 0 5 5 5 5 5 5 5 5
```

