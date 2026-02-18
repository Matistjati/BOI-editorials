# ANCIENT

The problem ANCIENT is solved by generating all possible variants and applying dynamic programming to avoid recalculating everything from scratch.

We have the following states in our DP:

```text
dp[i1, r, i2, i3, i4, i5]
```

It represents the number of ways a phrase can be completed if:

* The phrase is already filled up to the **i1-th letter** (inclusive).
* The **i1-th letter** is `r`.

Counting from the i1-th letter **backwards** (we are not interested in what happens at the beginning of the word, only at the end, i.e., the position from which we need to continue filling), there are:

* `i2` consecutive identical consonants
* `i3` consecutive consonants
* `i4` consecutive identical vowels
* `i5` consecutive vowels

For example, the initial phrase:

```text
y*af
```

Recursively, we fill it up to `aayb`, i.e.:

* `i1 = 4`
* `r = 'b'`
* `i2 = 1` (ends with one identical consonant `'b'`)
* `i3 = 2` (ends with two consonants `'yb'`)
* `i4 = 0` (no vowels at the end)
* `i5 = 0`

Instead of filling all `*` at once, we try to **insert all possible letters** from `'a'` to `'z'`. For each inserted letter, we check if it is allowed (i.e., whether it exceeds the set limits).

We then **fill the table**:

* If a value is already in the table, we **take it from there**.
* If not, it is **calculated recursively** and **saved in the table**.

