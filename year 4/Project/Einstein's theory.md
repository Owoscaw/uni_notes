
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

# Action principle for gravity:

We have found the EOM for gravity, however are yet to find an action that yields said EOM. The RHS is the stress-energy tensor, which we found by varying the matter sector of the action wrt the metric. This suggests we can write the full action as:$$\Large S[g_{\mu\nu},\phi]=S_\text{gravity}[g_{\mu\nu}]+S_\text{matter}[g_{\mu\nu},\phi]$$After our variation, we found the stress-energy tensor EOM:$$\Large\begin{aligned}
\frac{\delta S_\text{gravity}}{\delta g^{\mu\nu}}+\frac{\delta S_\text{matter}}{\delta g^{\mu\nu}}&=0\\
\implies \frac{\delta S_\text{gravity}}{\delta g^{\mu\nu}}-\frac{1}{2}\sqrt{-g}T_{\mu\nu}&=0
\end{aligned}$$Comparing to Einstein's equation for gravity, we see that we need to find a functional $S_\text{gravity}[g_{\mu\nu}]$ such that (upon variation):$$\Large \frac{\delta S_\text{gravity}}{\delta g^{\mu\nu}}=\frac{1}{2\kappa}\sqrt{-g}\left(R_{\mu\nu}-\frac{1}{2}g_{\mu\nu R}\right)$$We propose that the correct action is the Einstein-Hilbert action:
> This has form:$$\Large S_\text{gravity}[g_{\mu\nu}]=S_{EH}=\frac{1}{2\kappa}\int d^nx\sqrt{-g}R$$
> To do our variation, we need the following matrix identity:$$\Large\begin{aligned}
\delta\ln\det M&=\sum_{\alpha\beta}(M^{-1})_{\alpha\beta}\delta M_{\beta\alpha}\\
_{\det M=\sqrt{-g}}\implies\delta\ln\sqrt{-g}&=-\frac{1}{2}g_{\mu\nu}\delta g^{\mu\nu}
\end{aligned}$$
> Now, performing our variation yields:$$\Large\begin{aligned}
\delta S_{EH}&=\frac{1}{2\kappa}\int d^nx\sqrt{-g}(g^{\mu\nu}R_{\mu\nu}\delta\ln\sqrt{-g}+R_{\mu\nu}\delta g^{\mu\nu}+g^{\mu\nu}\delta R_{\mu\nu})\\
&=\frac{1}{2\kappa}\int d^nx\sqrt{-g}\left(-\frac{1}{2}g_{\mu\nu} R\delta g^{\mu\nu}+R_{\mu\nu}\delta g^{\mu\nu}+g^{\mu\nu}\delta R_{\mu\nu}\right)
\end{aligned}$$
> For the last term, we can write the variation of the Ricci in terms of the variation of the Riemann tensor:
> > This seems daunting, as we are varying wrt the metric. However, we will first vary wrt the connection coefficients:$$\Large \delta R_{\mu\nu}=\delta  R^{\lambda}{}_{\mu\lambda\nu}=\underline{\nabla}_\rho\delta\Gamma^\lambda_{\nu\mu}-\underline{\nabla}_\nu\delta\Gamma^\lambda_{\rho\mu}$$
> > This is a meaningful expression, since the variation $\delta\Gamma^\lambda_{\mu\nu}$ can be thought of as a difference of connections. It is therefore reasonable to take the covariant derivative, so we write the last term as:$$\Large g^{\mu\nu}\delta R_{\mu\nu}=\underline{\nabla}_\lambda(g^{\mu\nu}\delta \Gamma_{\mu\nu}^\lambda-g^{\lambda\rho}\delta\Gamma^\beta_{\beta\rho})$$
> > This shows that the last term in our action is a total derivative, which will evaluate to a surface term when integrated. We therefore neglect the last term.
> We therefore find$$\Large \delta S_{EH}=\frac{1}{2\kappa}\int d^nx\sqrt{-g}\left(-\frac{1}{2}g_{\mu\nu}R+R_{\mu\nu}\right)\delta g^{\mu\nu}$$, dividing through by our variation recovers our expression for $\delta S_{EH}$ wrt $\delta g^{\mu\nu}$:$$\Large\implies\frac{\delta S_{EH}}{\delta g^{\mu\nu}}=\frac{1}{2\kappa}\sqrt{-g}\left(R_{\mu\nu}-\frac{1}{2}g_{\mu\nu}R\right)$$As required.
