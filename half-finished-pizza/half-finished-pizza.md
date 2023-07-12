`Half-finished Pizza: The Euler's Equation`
---
I know, I know. Such a suprise to see Euler (pronounced as oy-ler) again in some random math thread. But you see, he had been a nerd for quite a while and from there, the legendary $e$ was born. Such an overrated constant, I should say. Besides, our point here is to celebrate the <kbd>Euler's equation</kbd>, more known as <kbd>Euler's identity</kbd> which is 

$$e^{i\pi} + 1 = 0.$$

I bet my last 2 bucks you've seen this already (ha! I won.) And you might be wondering how this is true, or you might start with how absurd this equation is which is pretty much my concern too. Why in any possibility the constants $e$ and $\pi$ are both in the same equation together with the foreign element $i$ (there's much to the  <kbd>foreign</kbd> term, yes. Might be the next topic? Let's see!) It is like the <i>Avengers' Endgame</i> of math haha! 

But to get straight to it, why I called this half-finished pizza I don't know. Kidding! I have taken <kbd>Complex Analysis</kbd> this semester and I learned how to read this equation once again in another language (or say, field) of math. Let's dive in!

To start, in <kbd>Complex Analysis</kbd>, we'd learn that numbers not in the real world are called <kbd>complex</kbd> and that circles do come in the form of $ke^{2\pi i}$ which is right off the bat, a complex (literally and figuratively) expression. **We** (like shouting) should be smart by now that we take the complex number $i$ as a 90-degree counterclockwise rotation. And magically, $i$ is just another form of such <kbd>90-deg ccw</kbd> action. Another form of it is $i = e^{i\pi/2}$ which should also do the same action. Thereafter, <kbd>we</kbd> should also accept the fact that the unit circle (in complex, it is $e^{2\pi i}$) also rotates a position (this is $+1$ unit from <i>real axis</i>) 360-degree. A full-<kbd>circle</kbd> moment, exactly! Which makes sense since if $e^{i\pi/2}$ is a 90-deg rotation, we just need four of these to get a 360-deg rotation. And yes, math checks out (sighs) because 

$$e^{i\pi/2}\cdot e^{i\pi/2}\cdot e^{i\pi/2}\cdot e^{i\pi/2} = e^{2i\pi}$$

which is another full-<kbd>circle</kbd> moment! 

Now, we should introduce the half-finished pizza which is anticlimactic since it is just the simple <kbd>semicircle</kbd>. That is, we rotate that 1-unit 180-degrees. Exactly, it is equal to $e^{i\pi}$. 

Now, we only need to setup a plane to where we apply the rotations since it does not make sense without it. Imagine a cartesian plane. Change the $x-$axis to <kbd>real axis</kbd> and the y-axis to <kbd>imaginary axis</kbd> (the points here are $i, 2i, 3i$.) Now, the rotations are possible! For example, if our point is on the $+1$ of the real axis, then applying 90-degree rotation should change our point to $i$. We are now close! Our 180-degree rotation, therefore, changes the point $+1$ to $-1$. And yey, we are done. By now, we should be clapping our hands to pay respects for Euler (again) for this equation. By the way, the final step is therefore, changing the form of $e^{i\pi}$ to $-1$ and then add this to $1$. We should get $0$! (this is not factorial, just to be clear. I am just as elated as you haha.) 

And that's how we read <kbd>Euler's Equation</kbd>.

---
`Extended Reading`
The <kbd>Euler's Equation</kbd> has so much applications in the real world. For instance, <kbd>wave functions</kbd> (Pedro,2021) and <kbd>circuits</kbd> (M.Malarvizhi, 2021) are some of the most notable ones to list. To know more about the <kbd>Euler's Equation and Identity</kbd>, check the lecture from <kbd>Khan Academy</kbd> below:

> https://www.khanacademy.org/math/ap-calculus-bc/bc-series-new/bc-10-14/v/euler-s-formula-and-euler-s-identity#:~:text=Euler%27s%20formula%20is%20e%E2%81%B1%CB%A3%3Dcos,(x)%2C%20and%20e%CB%A3.

References:
>[1] Malarvizhi, M. "Diagonally implicit and explicit Euler’s methodsfor RLC circuit", Turkish Journal of Computer and Mathematics Education, 2021.
>
>[2] Pedro, L. "Relating the wave-function collapse with Euler’s formula, with applications to Classical Statistical Field Theory", 2021.