Title: The Other Thing Turing Invented
Date: 2026-5-25 10:00
Tags: mathematics, simulation, biology, javascript
Category: Blog
Slug: morphogenesis
Summary: Everyone knows Turing cracked Enigma and defined computation. Fewer know he also explained why leopards have spots.
featured_image: /images/morphogenesis/turingglasses.jpg

![turing glasses]({static}/images/morphogenesis/turingglasses.jpg)  

## The Alan Turing You Know

- Cracked Enigma. 
- Founded computer science. 
- Described the limits of computation before computers existed. 
- Proposed a test for machine intelligence before there was anything worth testing.

Most people stop there.

In 1952, two years before he died, he published one more paper. It had nothing to do with cryptography or computing. The title was [*The Chemical Basis of Morphogenesis*](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/turing1952.pdf).

---

## What Is Morphogenesis

Morphogenesis is the process by which a single fertilised cell becomes a creature with a head, a spine, working limbs, and - if it's a leopard - spots arranged in a specific pattern.

The mystery isn't that it happens. The mystery is the coordination. The egg contains no spots. There's no coordinate map in the DNA saying "start brown patch here, radius 3cm." Nothing tells any individual cell what its neighbours are doing. Yet the pattern emerges, every time, at the right scale, in roughly the right places.

Turing's paper proposed a mechanism.

He wasn't working with molecular biology - that field was barely starting. He didn't know which specific chemicals were involved. What he did was more abstract: he showed that a *class of system* would produce spatial patterns spontaneously, from a nearly uniform start, given two ingredients and one counterintuitive condition.

![giraffe stages]({static}/images/morphogenesis/giraffestages.png)  

---

## The Key Idea

Imagine two chemicals, U and V, spreading through a tissue:

- **U is the activator**: it promotes production of both itself and V
- **V is the inhibitor**: it suppresses U production
- **V diffuses faster than U**

On the surface this looks self-regulating. U fires, V catches up, everything settles. Stable.

But the different diffusion rates break the symmetry. Where U is slightly higher than average, it amplifies itself before V can arrive to suppress it. V, spreading faster, suppresses the *surrounding* region instead. High-U patches stay high, while their neighbours stay low.

A small random fluctuation in concentration - which exists in any real system - is enough to start the process. The pattern isn't programmed in. It *grows out of instability*.

This is the Turing instability. It's counterintuitive enough that it took a mathematician to spot it: instability plus diffusion produces order, not chaos.

---

## The Equations

The Gray-Scott model (a close relative of Turing's original formulation) captures this in two equations:

```
∂u/∂t = Dᵤ ∇²u  -  u·v²  +  F·(1 - u)

∂v/∂t = D_v ∇²v  +  u·v²  -  (F + k)·v
```

Reading each term left to right for U:

- `Dᵤ ∇²u` — U spreads by diffusion. The Laplacian (∇²) measures how much a cell differs from its neighbours - it's just a weighted average of the surrounding cells minus the centre.
- `u·v²` — the reaction. U and V combine, consuming U and producing V.
- `F·(1 - u)` — feed rate. U flows in from outside, replenishing it toward 1.

V follows the same structure: it spreads faster (D_v < Dᵤ), gains from the reaction, and drains away at rate `(F + k)`.

Two parameters do all the work: **F** (feed rate) and **k** (kill rate). Different (F, k) pairs produce entirely different patterns from the same equations - spots, stripes, mazes, spirals, bubbles. Same physics, different character.

---

## The Simulation

Simulation can be found [here](/projects/morphogenesis/morphogenesis.html)

The canvas runs the Gray-Scott model in your browser. It starts with random perturbations scattered through a uniform field, then runs forward in time.

![maze]({static}/images/morphogenesis/diffusionscreenshot.png)  

Each preset loads a different (F, k) pair. **spots** and **coral** settle quickly into stable formations. **maze** and **worms** take longer to resolve. **spirals** never fully settles.

Try the sliders manually. Moving toward the boundary between two pattern types often produces interesting transients before the system makes up its mind.

> If anybody knows why the worms and bubbles aren't working please give me a shout. I've used the defaults found online but can't get them to work

---

## Why This Matters Now

The 1952 paper spent several decades as a mathematical curiosity. No one could find the specific chemicals it predicted.

Then molecular biology caught up.

In 2012, researchers showed that the spacing of fingers in mouse embryos follows a Turing mechanism - two proteins, Wnt and Bmp, playing activator and inhibitor. Zebrafish stripes, hair follicle spacing, tooth arrangement, sea shell pigmentation - the same mechanism keeps showing up once you know to look for it.

Game developers use reaction-diffusion in procedural terrain and texture generation - it produces organic-looking structure without needing anyone to design it by hand. The same equations turn up in GPU shaders for water and skin rendering. A-life researchers have been running variants of this for decades to study how complex structure emerges from local rules with no central coordinator.

It's one of the cleaner examples of a mathematical result being sixty years ahead of the biology. The patterns were sitting in the equations long before anyone found them in a cell.

---

My inspiration for this came from having read a Turing biography a number of years ago. I had a vague recollection about him doing other work around animal markings. Some googling and the awesome video below and I was set to build my own simulation.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JtGIc18CGgo?si=seyfBNyf8SqD2YmC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

*He died in 1954, two years after the paper was published. It took biology sixty years to catch up.*
