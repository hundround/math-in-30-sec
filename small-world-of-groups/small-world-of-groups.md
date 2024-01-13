`Small World of Groups`
---
I decided to make a jump from <kbd>analysis</kbd> to <kbd>algebra</kbd> which is not a huge jump to take in the first place. You know, I have been wondering why aren't all of us are introduced to the world of <b>Groups</b> even though we're using it every time we're accessing a mere number, say $1$ or $2$ or $\pi$ (absurd, lmao). For what it's worth, <b>Groups</b> are  important for us! They are one of the slickest, if not the slickest, of maths I encountered thus far.

The name <kbd>Groups</kbd> has a nice ring to it since it is literally a group of numbers, more generally called elements but we're not abstract algebra-ists here, are we? (please no) Now, the first time I learned about groups, I had not been able to really appreciate their essence not until I put some analogy—a poor one, but still—to it. I'd think that a group is a small world, small enough to contain simple people in it. There are different worlds (remind yourself we're talking about groups here) just like in real life. Some are big—like really big that an infinite number of people were in it—some are small. There's this world, they say that it was the first world ever made, called <kbd>trivial group</kbd>. The trivial group only contains a single person. He's that special. He calls himself the <kbd>identity element</kbd>. He might be a narcissist but who cares. His nickname's $e$. The world of groups also requires a language that the people use to interact with each other. They call it <kbd>operations</kbd>. They denote it usually by $*$. This is a general language. Specific languages that are often used by the people are $+,-,\times,\div$.

Now, when do we say that a group is a <i>group</i>? They say that a group is a group if the following are satisfied:
- Fences can travel from one pair of people to another. We often call this <kbd>associativity</kbd>. That is, for pairs of people $a$ and $b$, and $b$ and $c$, we have
$$(a*b) *c = a *(b * c).$$ <br>
- The narcissistic identity $e$ is always in that group. Also, $e$ have a special interaction with all the people within the same group. That is, say any person $a$, we have
$$a*e = e *a = a.$$ <br>
- Every person has an inverted doppelganger (lmao). Say, for instance, a person $a$. Then within the same world, $a^{-1}$ exists. And that $e$ is an accomplice of this doppelganger $a^{-1}$. We have
$$a*a^{-1} = e = a^{-1}*a.$$ <br>

This is fun, right? Haha, no. But it was handy indeed to talk about groups in general. This idea of generalizing things is a working thought in all of <kbd>Abstract Algebra</kbd>. Sometimes we might ask ourselves the essence of these, and to do that, always try to apply the generality to a particular case. The groups for instance can be applied to the set of real numbers. Who are the people in it? Any real numbers you can think of. What is their language? We have addition $+$ How do we check if this set is indeed a group? Let's try to pick three real numbers, say $1$, $2$, and $4$. We have
- $(1+2)+4 = 7 = 1+(2+4)$. Hence, associativity works well.
- The identity $e$ here is $0$ for addition since $1+0 = 1 = 0+1$. 
- Inverses are also here. They are the negative numbers. We have for any person (real number) $a$, $a+a^{-1} = 0$. This implies that
  $$a+a^{-1} = 0 \longrightarrow a^{-1} = -a+0 = -a.$$ 

And we're done showing that the set of real numbers is a group under addition $+$. How about multiplication? Is the set of real numbers a group under multiplication $\times$? Prove or disprove it for yourself!

---
`References` <br>
Hi thanks for reading this! If you are interested about <kbd>Groups</kbd> and other abstractions in Math, you should read Fraleigh's <kbd>Abstract Algebra</kbd> book:
> J. B. Fraleigh, “A First Course in Abstract Algebra,” 7th Edition, Addison-Wesley, Boston, 1982.

