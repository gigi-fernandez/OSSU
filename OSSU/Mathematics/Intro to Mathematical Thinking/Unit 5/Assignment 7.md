![[Pasted image 20230420123944.png]]

If assumption $\phi$ \[$\forall$ Bird (CanFly(Bird))\] is True, that necessarilly means assumption $\psi$ \[$\neg$$\exists$ Bird( $\neg$CanFly(Bird))\] is True. $\phi$ <=> $\psi$
Therefore, we must find a bird that cannot fly to disprove $\psi$.
Ostriches are birds and cannot fly, therefore $\psi$ is False.
If $\psi$ is False, it necessarily means that $\phi$ is False.
QED.

![[Pasted image 20230420124550.png]]

(Claim will be named $\phi$)
If $\phi$ is True, that implies that $\psi$ \[$\neg$$\exists$ x,y $\in$ $\mathbb{R}$ ( (x - y)$^2$ <= 0)\]
If we can prove that $\psi$ is False, it follows that $\phi$ must also be False.
We must think of an example for $\psi$ to be False.
Let's use the example of x=0 $\wedge$ y=0: 
	(0-0)^2 <= 0.
	0 <= 0
	0 = 0
Therefore, $\psi$ is false, and so is $\phi$.
QED.

![[Pasted image 20230420125537.png]]

If we consider x and y to be the two unequal rational, and z to be the third rational in the middle:
Let's assume that the claim is correct and every two unequal rationals have another third rational in-between.
This means:
	x $\not$= y
	x = a/b, y = c/d, (a,b,c,d) being integers.

x < z < y $\implies$ a/b < z < c/d
Let's equate z to the mean between x and y.
z = $\frac{x+z}{2}$ = $\frac{a/b + c/d}{2}$ =  $\frac{ad/bd + cb/db}{2}$ = $\frac{(ad+cb)/bd}{2}$
There is no way for the sum or the division between integers to return something other than a rational number. Therefore, z is necessarily rational.
QED.

![[Pasted image 20230420131412.png]]

The truth tables of those statements are as follows:

|$\phi$ | $\psi$ | $\phi$ $\implies$ $\psi$  | $\psi$ $\implies$ $\phi$ | $\phi$ <=> $\psi$ | $\phi$ $\implies$ $\psi$ $\wedge$ $\psi$ $\implies$ $\phi$ |
|--|--|--|--|--|--|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | T | F | F | F |
| F | F | T | T | T | T |

Saying that both $\phi$ $\implies$ $\psi$ AND $\psi$ $\implies$ $\phi$ are true is the same as saying that $\phi$ <=> $\psi$ by definition.
QED.

![[Pasted image 20230420132112.png]]

|$\phi$ | $\psi$ | $\neg$$\phi$ | $\neg$$\psi$ | $\phi$ $\implies$ $\psi$  | $\neg$$\phi$ $\implies$ $\neg$$\psi$ | $\phi$ <=> $\psi$ |
|--|--|--|--|--|--|--|
| T | T | F | F | T | T | T |
| T | F | F | T | F | T | F |
| F | T | T | F | T | F | F |
| F | F | T | T | T | T | T |

Or in a writen format: saying that $\phi$ $\implies$ $\psi$ and that $\neg$$\phi$ $\implies$ $\neg$$\psi$  is the same as saying that $\phi$ has total predictive factor over $\psi$. The state of $\psi$ is just a replica of the state of $\phi$, and $\phi$ <=> $\psi$ is just a way of representing it.

![[Pasted image 20230420132804.png]]

I'll try to prove that if 5 investors split 2M, at least one investor receives >= 400k:
	$\exists$ investor (400k(investor) )
The negation of this argument is that there is no case in which every investor receives <400k
	$\forall$ investor ($\neg$ 400k(investor))
What is the minimum quantity each investor can receive simultaneously? That's 2M split equally in 5, which results in 400k. Therefore, there is no way for all investors to receive less than that if we try to minimize their benefits for all. This implies that there's at the very least one investor that receives >= 400k. Finally, this is equivalent to the initial assumption, so it is true.
QED.

![[Pasted image 20230420144134.png]]

In order for $\sqrt{3}$ to be irrational, it cannot be a quotient of two integers with different factors.
Let us assume the opposite: that $\sqrt{3}$ is rational and q and d have different factors.
1. $\sqrt{3}$ = q/d
2. 3 = q$^2$/d$^2$
3. 3d$^2$ = q$^2$
4. d cannot have 3 as a factor, because it already is a factor of q
5. 3d$^2$ = (3k)$^2$
6. 3d$^2$ = 9k$^2$
7. d = 3k
10. This is not possible, since that would mean that d is a factor of q
11. Therefore, it is not rational.
12. It is instead, irrational.
QED.

![[Pasted image 20230420150934.png]]
![[Pasted image 20230420151321.png]]
(a) If the Yuan rises, the Dollar falls (FALSE)
(b) If -y < -x then x < y (x,y $\in$ $\mathbb{R}$) (TRUE)
(c) If two triangles have the same area they are congruent (FALSE)
(d) Whenever b$^2$ >= 4ac, the quadratic equation ax$^2$ + bx + c = 0 has a real solution (all numbers being Real and a $\not$= 0) (TRUE)
(e) ...

![[Pasted image 20230420151816.png]]

1. Let's assume it is true. If n$^3$ is divisible by 12 then n must be divisible by 12.
2. n$^3$ % 12 = 0 $\implies$ n % 12 = 0
3. n$^3$ = k * (2$^2$ * 3)
4. n = $\sqrt[3]{k * (2^2 * 3)}$
5. 