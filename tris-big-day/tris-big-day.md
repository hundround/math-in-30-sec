`Tri's Big Day: The Modular Arithmetic`
---
In a faraway land, so far that gravity exists unstably, there was an advanced civilization superior to that of Earth. The people there have eyes that can identify an object even from a mile of distance. I don't know, maybe they needed it so thus evolution. Anyway, there's this kid named <kbd>Tri</kbd>. He has a class every $2^{18}$ th day of the week. Kind of weird how they count, right? Well, I forgot to say it but in their world, there are 12 days in a week; it is not <i>week</i> they call it, it is <kbd>semaine</kbd>. 

If, by chance, he ever transferred to Earth, things would be so disorienting for him. It's your responsibility, as his friend, to know what day of the week he should go to school had it been here on earth. Miraculously, you already know about <b>Modulo</b>!

<kbd>Modular Arithmetic</kbd> had been useful for more than thousands of years solving countless problems involving numbers be they simple or complex. How do we do modulo? It's eaaaaaaaaaasy! Think of modulo as a function. We already know that a function has an input and an output. You should expect that the output of a modulo function is the exact remainder when you divide a number, say $k$, to another number, say $m$. Structure-wise, it is $$r \equiv k\bmod m.$$ The remainder denotes $r$. 

What can we do with Modulo? Well...
* We can add any number we fancy on the left (or right) side of the equivalence, provided that it is divisible by $m$. Say we have $2 \equiv 9 \bmod 7$. Now, we can add any multiple of 7 to either $2$ or $9$ and it should still work. That is,
  $$2 + 10(7) = 72 \longrightarrow 72 \bmod 7 = 2.$$
* We can multiply a number $s$ to both sides of the equivalence provided that $s$ is <i>relatively prime</i> to $m$. By relatively prime, we mean that $s$ and $m$ do not have any other common factors except $1$.
* We can reduce any factor by its equivalent modulo $m$. It means, for instance, $72 \bmod 7$, that we can easily find the remainder by finding the factors of $72$ and evaluating each factor to modulo $7$. That is,
  $$72 \bmod 7 \longrightarrow 9(8) \bmod 7 \longrightarrow 2(1) \bmod 7 \equiv 2.$$

Now, Tri's elf, <kbd>reik</kbd>, has heard of Tri's travel and decided to help us help him. Reik said that in order to keep count of the number, we should know about <kbd>Fermat's Little Theorem (FLT)</kbd>! It says

> For any prime $p$ and integer $a$, we have the equivalence $$a^p \bmod p \equiv a$$

which is tremendous! That's exactly what we need. Let's work on the problem! The problem's simple: we have to find what day of the week, given that our week has only $7$ days in it, should Tri go to school if he goes every $2^{18}$ th day. We have
$$2^{18} \bmod 7.$$

Using Fermat's little (read this in the tiniest voice you can make lmao) theorem, since the problem suffices the requirements of the theorem (we have $p = 7$ and $a = 2$), we then have
$$2^{18} \bmod 7\longrightarrow 2^{7(2)+4}\bmod 7 \longrightarrow 2^{7(2)}\cdot 2^4\bmod 7.$$

by laws of exponents. Now, we can apply the third noted rule we have for Modulo. That is, we reduce each factor to modulo $7$. But since the first factor, $2^{7(2)}$ is suited for FLT, we have
$$2^{7(2)}\cdot 2^4\bmod 7\equiv 2\cdot 2^4\bmod 7 \longrightarrow 2(16)\bmod 7 \equiv 2(2) \bmod 7 \equiv 4.$$

And we got it! Tri should go to Earth school every 4th day of the week!

--- 
`References`
> [1] [Modular Arithmetic](https://crypto.stanford.edu/pbc/notes/numbertheory/arith.html) <br>
> [2] [Fermat's Little Theorem](https://brilliant.org/wiki/fermats-little-theorem/)