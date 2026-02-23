
Solitons are special solutions to [[Introduction to PDEs#PDEs|non-linear PDEs]] that behave like localised particles. We build basic physical observations into a complex framework:
> A soliton is defined by three essential properties:
> > Locality, a lump of localised space
> > Stability, shape is maintained over time
> > Collision-proof, solitons re-emerge after collision with each other with their original shapes and velocities (though may experience phase shift).
> Our foundational equation is the [[Basic properties of Solitons#The KdV equation|KdV]] equation, though we also consider the [[Travelling Waves#The sine-Gordon equation|sine-Gordon]] equation. This introduces topological lumps (kinks/anti-kinks) that remain stable due to their "winding number" at infinity.

We develop many solution-generating techniques that we can apply to some "vacuum solution" to give new, unique solutions:
> [[Backlund transformations]] map known solutions to new, more complex solutions. The [[Backlund transformations#Theorem of permutability|theory of permutability]] allows for the algebraic "addition" of solitons.
> [[The Hirota method]] allows for $N$-soliton solutions to be constructed systematically using exponentials. This works by substitution of a bilinear [[The Hirota method#Hirota's bilinear operator|operator]] to transform the PDE into quadratic form.

Our most powerful tool comes from studying the connection between KdV-like equations and the [[Time evolution of QM states#Schrodinger equation motivation|time independent Schrodinger equation]]. It is essentially a "non-linear Fourier analysis":
> We treat the initial wave profile as a potential in the TISE and define the [[Scattering theory#Summary|discrete spectrum]] (correspondent to solitons) and the continuous spectrum (dispersive "junk") associated with the initial wave profile.
> We evolve the associated wave function according to the Schrodinger equation with our defined potential. The scattering data evolves via simple linear ODEs.
> 