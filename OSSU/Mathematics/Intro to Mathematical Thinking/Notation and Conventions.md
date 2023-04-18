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
