"""
W = max row width
d = depth
o = offset
x = len of pipe
y = len of offset pre

if o == 0:
    w = W - d * x
else:
    w = W - (d - o) * x - y

M = minimal active width

let's say o = 0. What is the smallest value of d for which w < M?

W - d * x < M
W - M < d * x

(W - M) // x + 1 is the smallest value of d for which w < M

So if d == (W - M) // x and we want to increase d by 1, we must set o = (W - M) // x

Now, let's say o > 0. What is the smallest value of d for which w < M?

W - (d - o) * x - y < M
W - M - y < (d - o) * x
(W - M - y) // x + o < d

So, if d == (W - M - y) // x + o and we want to increase d by 1, we must set o = (W - M - y) // x + o

In other words, we firstly increase o by (W - M) // x, and then we always increase it by (W - M - y) // x
"""
