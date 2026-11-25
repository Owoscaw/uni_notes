
We have seen have gravity affects the [[year 4/Project/Geodesics#Geodesics|geodesic]] paths a particle will follow as well as the state of matter fields. We will now see the converse, how matter affects spacetime [[Curvature|curvature]].

# Equations of Motion for gravity:

A naive attempt to write an EOM for the metric in the presence of matter fields would look like$$\huge W_{\mu\nu}=\kappa T_{\mu\nu}$$, with the tensor $W_\mu\nu$ being constructed from derivatives of the metric and $\kappa$ is a proportionality constant.

A first stab would be to guess $W_\mu\nu$ is simply the [[Curvature#Ricci tensor|Ricci tensor]], however this leads to an inconsistency as the RHS is the stress-energy tensor that is manifestly divergence-free. Therefore we consider the [[Curvature#Einstein tensor|Einstein tensor]] which has our desired property. Our consistent EOM for gravity therefore has form:$$\Large R_{\mu\nu}-\frac{1}{2}g_{\mu\nu}R=\kappa T_{\mu\nu}$$
Contracting with the metric, we find$$\Large\begin{aligned}
 g^{\mu\nu}R_{\mu\nu}-\frac{1}{2}g^{\mu\nu}g_{\mu\nu}&=R-2R=\kappa g^{\mu\nu}T_{\mu\nu}\\
\implies R&=-\kappa T^\mu_\mu
\end{aligned}$$, allowing us to write Einstein's equation in the form:$$\Large R_{\mu\nu}=\kappa(T_{\mu\nu}-\frac{1}{2}g_{\mu\nu}T^\lambda_\lambda)$$