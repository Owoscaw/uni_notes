
We have seen have gravity affects the [[year 4/Project/Geodesics#Geodesics|geodesic]] paths a particle will follow as well as the state of matter fields. We will now see the converse, how matter affects spacetime [[Curvature|curvature]].

# Equations of Motion for gravity:

A naive attempt to write an EOM for the metric in the presence of matter fields would look like$$\huge W_{\mu\nu}=\kappa T_{\mu\nu}$$, with the tensor $W_\mu\nu$ being constructed from derivatives of the metric and $\kappa$ is a proportionality constant.

A first stab would be to guess $W_\mu\nu$ is simply the [[Curvature#Ricci tensor|Ricci tensor]], however this leads to an inconsistency as the RHS is the stress-energy tensor that is manifestly divergence-free. Therefore we consider the [[Curvature#Einstein tensor|Einstein tensor]] which has our desired property. Our consistent EOM for gravity therefore has form:$$\Large R_{\mu\nu}-\frac{1}{2}g_{\mu\nu}R=\kappa T_{\mu\nu}$$
Contracting with the metric, we find$$\Large\begin{aligned}
 g^{\mu\nu}R_{\mu\nu}-\frac{1}{2}g^{\mu\nu}g_{\mu\nu}&=R-2R=\kappa g^{\mu\nu}T_{\mu\nu}\\
\implies R&=-\kappa T^\mu_\mu
\end{aligned}$$, allowing us to write Einstein's equation in the form:$$\Large R_{\mu\nu}=\kappa(T_{\mu\nu}-\frac{1}{2}g_{\mu\nu}T^\lambda_\lambda)$$
## [[year 4/Project/Geodesics#Newtonian limit|Newtonian limit]] revisited:
Recall in the Newtonian limit, we are close to Minkowski spacetime with a small correction term according to the metric, $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$. For matter fields, we assume they are close to static and $T_{ij}<<T_{00}$, giving leading order trace:$$\Large T^\mu_\nu\approx-T_{00}$$The $00$ component of Einstein's equation then reads:$$\Large R_{00}\approx\frac{\kappa}{2}T_{00}$$Now using our expression for the Riemann tensor we found before, we write:$$\Large\begin{aligned}
R_{00}= R^{j}{}_{0j0}&=\partial_j\Gamma^j_{00}-\partial_0\Gamma^j_{j0}
+\mathcal{O}(h^2)\\
&=\partial_j\Gamma^j_{00}+\mathcal{O}(\partial_{x^0})\\
&\approx-\frac{1}{2}\partial_i\partial^ih_{00}=\partial_i\partial^i\Phi\end{aligned}$$Here, we dropped all higher-order terms in the perturbation $h_{\mu\nu}$ as well as time derivatives (as they are small in the Newtonian limit). We then used our identification for gravitational potential we found [[year 4/Project/Geodesics#Newtonian limit|previously]]. Now, we identify energy density with mass density in the non-relativistic limit $T_{00}=\rho$, giving$$\Large \partial_i\partial^i\Phi=\frac{\kappa}{2}\rho$$which dictates the identification:$$\Large \kappa=8\pi G_N$$