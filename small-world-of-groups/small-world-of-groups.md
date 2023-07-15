`Small world of Groups`
---
I decided to make a jump from <kbd>analysis</kbd> to <kbd>algebra</kbd> which is not a huge jump to take in the first place. You know, I have been wondering why aren't all of us are introduced in the world of <b>Groups</b> eventhough we're using it every time we're accessing the mere number, say $1$ or $2$ or $\pi$ (absurd, lmao). For what its worth, <b>Groups</b> are worthy our time! They are one of the slickest, if not the slickest, of maths I encountered thus far.

The name <kbd>Groups</kbd> has a nice ring to it since it is literally a group of numbers, more generally called elements but we're not abstract algebra-ists here, are we? (please no) Now, the first time I learned about groups, I had not able to really appreciate its essence not until I put some analogy—a poor one, but still—to it. I'd think that a group is a small-world, small enough to contain simple people in it. There are different worlds (remind yourself we're talking about groups here) just like in real life. Some are big—like really big that an infinite people were in it—some are small. There's this world, they say that it was the first world ever made, called <kbd>trivial group</kbd>. The trivial group only contains a single person. He's that special. He calls himself the <kbd>identity element</kbd>. He might be narcissist but who cares. His nickname's %e%. The world of groups also requires a language that the people use to talk to each other. They call it <kbd>operations</kbd>. They denote it usually by $*$. This is a general language. Specific languages that often used by the people are $+,-,\times,\divide$.

Now, when do we say that a group is a <i>group</i>? They say that a group is a group if the following are satisfied:
> Fences can travel from a pair of people to another. We often call this <kbd>associativity</kbd>. That is, for pairs of people $a$ and $b$, and $b$ and $c$, we have $$(a*b)*c = a*(b*c)$$
> The narcissistic identity $e$ is always in that group. Also, $e$ have special interaction with all the people within the same group. That is, say any person $a$, we have $$a*e = e*a = a$$. 
> Every person has an inverted doppelganger (lmao). Say for instance, person $a$. Then within the same world, $a^{-1}$ exists. And that $e$ is an accomplice of this doppelganger $a^{-1}$. We have $$a*a^{-1} = e = a^{-1}*a$$.

This is fun, right? Haha, no. But it was handy indeed to talk about groups in general. This idea of generalizing things is a working thought in the whole of <kbd>Abstract Algebra</kbd>. Sometimes we might ask ourselves the essence of these, and to do that, always try to apply the generality to a particular case. The groups for instance can be applied to the set of real numbers. Who are the people in it? Any real numbers you can think of. What is their language? There are two: addition $+$ and multiplication $\times$. Either of them can be. How do we check if this set is indeed a group? Let's try to pick three real numbers, say $1$, $2$ and $4$. We have
> $(1+2)+4 = 7 = 1+(2+4)$
> Identity $e$ here is $0$ for addition since $1+0 = 1 = 0+1$. 
> Inverses are also here. They are the negative numbers. We have for any person $a$, $a+a^{-1} = 0$. This implies that $a^{-1} = -a+0 = -a$. 

And we're done showing that the set of real numbers is a group under addition $+$!

---
`References`
Hi thanks for reading this! If you are interested about <kbd>Groups</kbd> and other abstractions in Math, you should read Fraleigh's <kbd>Abstract Algebra</kbd>:
> J. B. Fraleigh, “A First Course in Abstract Algebra,” 7th Edition, Addison-Wesley, Boston, 1982.

