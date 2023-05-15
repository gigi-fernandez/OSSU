$\neg$ -> NOT
Conjunction: $\wedge$ -> AND. Arguments are called 'conjuncts'
Disjunction: $\vee$ -> OR (inclusive OR, True if both statements are True). Arguments are 'disjuncts'

Implication: =>. Antecedent => Consequent. Implication is the negation of "not implication". It might sound obvious, but the truth table for implication is derived from "not implication" ($\not$=>). In order to determine that the antecedent is True does NOT imply the consequent is True, you must determine that when the antecedent is True, the consequent is False. Implication is the opposite of that.

Sufficiency: If $\phi$ is sufficient for $\psi$, it means that $\phi$ => $\psi$.
Necessity: If $\phi$ is necessary for $\psi$, it means that $\psi$ => $\phi$.

Equivalence: <=>. It means that $\phi$ and $\psi$ are both in a biconditional relationship. $\phi$ is sufficient and necessary for $\psi$, meaning that they both imply each other. It is only True when both are True or False (after all, that's what equivalence colloquially means). Another way of saying it is: A is True if and only if (abb 'iff') B is True.

---
There exists: $\exists$. Means that there is at least an instance of an object following a set of rules. Variation: $\exists$!. Means that there is a unique instance of an object following a set of rules. Syntax is as follows: $\exists$ x (x + 1 = 0)
For all: $\forall$. Means that every instance of an object follows a set of rules. Syntax is as follows: 
$\forall$ x (x$^2$ $\geq$ 0)

Universal quantifier: A condition for a huge amount of numbers. The following UniQ means "for every number x in the set of all real numbers...": $\forall$x$\in$$\mathbb{R}$ (_rule_)

Membership (in set): $\in$. Means that something is included in a set. Obj $\in$ Set.

---
# Binding precedence
_The order in which logical operators are applied_

1. Quantifiers bind the first next thing.
	$\forall$ _L_( ... )
2. Same for negation.
	$\neg$( ... )
3. Then conjunction (use parenthesis if near a disjunction)
	( ... ) $\wedge$ ( ... )
4. Then disjunction and implication (should always use parenthesis anyways)
	( ... ) $\vee$ ( ... ) ------ ( ... ) => ( ... )

# Types of proofs

### Proof by example

For a given proposition _A_, try to think of an example in which _A_ is true (if we are trying to prove a single case) or false (if we are trying to disprove a $\forall$ statement). In this proof, you need multiple quantifiers, one of which will be replaced by __any arbitrary__ number. You must solve the statement for any arbitrary number.

### Proof by contradiction

For a given proposition _A_, try to extract logical conclusions (maybe with the help of an example) that are contradictory. If those two conclusions are logically valid from the premise, but the result is paradoxical, the you have proven that the _A_ is not logically sound (and therefore, false).

### Proof by cases

For a given proposition _A_ try to branch its possibilities into cases (if P(x) is True, if P(x) is False...). If all possible cases lead to the same conclussion, you just have proven something.

## Proof by induction

Based on the Principle of Mathematical Induction, this proof only works for $\forall$ type statements $\in$$\mathbb{N}$. 
PMI: ($\forall$n) \[_A_(n) => _A_(n + 1)\]
For a proposition _A_(n):
0. Start by clarifying that you are using PMI: 
	_By mathematical induction..._
1. Test _A_(n) for the first few cases. Usually 0 or 1.
2. Write down _A_(n) and _A_(n+1).
3. Reduce _A_(n+1) to a form where you can use A(n)
4. Hence, by PMI, the identity holds $\forall$n _A_(n). 
5. 