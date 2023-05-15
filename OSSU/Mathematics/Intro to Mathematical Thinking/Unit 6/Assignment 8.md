![[Pasted image 20230426175708.png]]

I shall prove or disprove the statement A(m, n) by finding an example. Take A(0, 0):
	0 + 0 + 0 is a perfect square.
Therefore there are integers m and n for A(m, n) to be a perfect square (0$^2$)

![[Pasted image 20230426184427.png]]

Let's try to use a proof by example:
	$\forall$m ($\exists$n (mn + 1 = p$^2$))
	_p_ being a positive integer and, therefore, p$^2$ is a perfect square
	Let's asume that _m_ is arbitrary:
	$\exists$n (mn + 1 =  p$^2$ )
	Now we can pick an _n_ that can prove the statement. We can do that by solving for n
	How can we have $mn + 1 = p^2$? 
		$mn = p^2 - 1$
		$mn = (p+1)(p-1)$
		We can say that $m = p-1$ and $n = p+1$
		$p = m + 1$ and, replacing p in n with that: $n = (m+1) + 1 = m + 2$
	n = m + 2
	m*(m+2) + 1 = p$^2$ 
	m$^2$ + 2m + 1 = p$^2$ 
	(m+1)(m+1) = p$^2$ 
	(m+1)$^2$ = p$^2$ 
(m + 1)$^2$ is a perfect square. Therefore, for any m, there's an n where mn+1 is a perfect square.

![[Pasted image 20230515174135.png]]

$\forall$n ($\exists$ b,c (n$^2$ + bn + c = pq)), p and q being two positive integers
Construction of an example:
	Let's consider that b = 2 and c = 1 for all possible _n_
	$n^2 + 2n + 1 = pq$
	$(n+1)(n+1) = pq$
	$f(n)$ is a product of two numbers, and thus composite for all $n$ where $b=2,c=1$. For this case, the proposition is always true.

![[Pasted image 20230515180629.png]]

$2n = p+q => 2n+1 = r+s+t$
$2n - (p+q) = 2n+1 - (r+s+t)$
substract 2n from both sides
-(p+q) = 1 - (r+s+t)