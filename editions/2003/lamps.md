# Lamps

This task has basically 3 solutions with different complexity.

# $O(NM)$
The first solution is to simply compute all the intermediate patterns. In this case, M different states for each of the N lamps must be computed, yielding an O(NM) solution.

# $O(N 2^N)$
A standard approach to improve the solution (for smaller values of M) is to hash the pattern with some function. Then it can be easily checked (probably with O(1) complexity), whether the same pattern has ever occured before.
If the same pattern occurs at different moments t1 and t2, then the patterns repeat with cycle of length t2 - t1. Knowing that, the pattern at the moment M is equal to the pattern at the moment t1 + (M - t1) % (t2 -t1), where x % y denotes the remainder of the division x / y.
The most intuitive hash function to use is to simply view the representation of the pattern as a binary number. Since the number of different patterns of length N is $2^N$, the number of hash values is exponential to N. This method has a running time complexity $O(N 2^N)$, which does not depend on M. But it also requires $O(2^N)$ of memory.
However, since for most numbers N, the maximum length of the cycle of patterns consisting of N lamps is only a small fraction of 2^N, hash functions with less hash values can be used. For example, one could use only the states of k < N fixed lamps, rather than the states of all lamps, when hashing the pattern. We believe that the most suitable values for k are 20..24, as the array of 2^k elements should fit into the memory. However, for small values of N (N < 100), this seems to be enough.
Although for most (if not all) numbers N, the running time comlexity is asymptotically less, than $O(N 2^N)$, we do not know any better bound.

# $O(N \log(M))$
The third solution is based on the fact that we do not need to calculate all the M-1 intermediate patterns, to get the M-th one.
First of all, we need to prove the following lemma:
Lemma 1. For every prime p and positive integers k, l, which satisfy 1 < l < $p^k$, the binomial coefficient C($p^k$, l) is divisible by p.
Proof. Skipped, but not difficult.

Choosing = 2, C($2^k$, l) is thus an even number.

```
Let L (l, t) denote the state of lamp l at moment t.
Let XOR (a1 * b1, a2 *b2, ..., ai *bi) denote the Xor of binary digits
a1, a1, ..., a1, a2, a2, ..., a2, ..., ai, ai, ..., ai
   b1 times         b2 times              bi times
As the function XOR is both commutative and associative, we ca write:
L (n, n) = XOR (L(n-1, n-1) * 1, L(n, n-1) *1) =
   = XOR ( XOR (L(n-2, n-2) * 1, L(n-1, n-2) *1), 
           XOR (L(n-1, n-2) * 1, L(n, n-2) *1)) =
   = XOR (L(n-2, n-2) * 1, L(n-1, n-2) *2, L(n, n-2) *1)=
   = XOR (L(n-3, n-3) * 1, L(n-2, n-3) *3, L(n-1, n-3) *3, L(n, n-3) *1)=
...
...
   = XOR (L(n-j  , n-j) * C(j, j),
          L(n-j+1, n-j) * C(j, j-1),
          L(n-j+2, n-j) * C(j, j-2),
          ...
          L(n-1  , n-j) * C(j, 1),
          L(n    , n-j) * C(j, 0))
Choosing j = 2^k, and bearing in mind that C(2^k, l) is even and XOR (a, a) = 0, we get
L (n, n) = XOR (L(n-2^k  , n-2^k) * C(2^k, 2^k),
                L(n-2^k+1, n-2^k) * C(2^k, 2^k-1),
                L(n-2^k+2, n-2^k) * C(2^k, 2^k-2),
                ...
                L(n-1    , n-2^k) * C(2^k, 1),
                L(n      , n-2^k) * C(2^k, 0)) =
         = XOR (L(n-2^k, n-2^k) * 1, L(n, n-2^k) * 1),
```
thus the state of the lamp is determined by the states of 2 lamps 2^k seconds before, and can be computed with a single XOR.
Hence we only need to compute $\log(M)$ intermediate patterns to get the answer, therefore the time complexity is $O(N \log(M))$.
