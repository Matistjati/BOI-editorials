Given some water level $X$, it is easy to compute the
total volume of water $V(X)$. Basically, one has
to compute for each object whether it is floating
or touching the lid. Luckily, $V(X)$ is monotonic
in $X$. We need to find such $X$ that $V(X) = P$,
where $P$ is the volume of water in the input data.
This can be done using binary search. We suggest
that the complexity of such task is 4 out of 10.

Another solution, which is much more educating, is
to observe that the set of possible water levels
can be split into disjoint set of intervals such
that within every interval each object is either
floating or touches the lid. This allows solving
the task using a linear equation. This is so-called
"scanning line" principle. Unfortunately we do
not see any way to force the contestants to use
this method.
