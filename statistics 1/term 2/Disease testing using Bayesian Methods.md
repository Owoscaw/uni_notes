A new test for covid-19 has been developed. It is fast and cheap but has moderate accuracy. This test was used on a sample people with known status of covid. Consider that you are selected at random from the UK population in August 2020 and you test positive. What is the probability that you have Covid?

The test was performed on $620$ hospital patients with known covid status by a gold-standard covid test:

|                     | Has Covid $D^+$ | Has not Covid $D^-$ | Total |
|:-------------------:|:---------------:|:-------------------:|:-----:|
| Test Positive $T^+$ |      $209$      |         $6$         | $215$      |
| Test Negative $T^-$ | $11$                | $394$                    | $405$      |
|        Total        | $220$                | $400$                    | $620$      |
A distinction between the test group and the UK population must be made. We then denote $P_t$ as the probability for the test group and $P$ for the probability of the general UK population. Define $P_t(T^+|D^+)$ as the sensitivity of the test, the probability of the test correctly diagnosing Covid. Similarly defined $P_t(T^-|D^-)$ as the specificity of the test, the probability of the test correctly diagnosing a person as Covid-free. Then define $P_t(T^+|D^-)$ as the probability of a false positive, $P_t(T^-|D^+)$ as the probability of a false negative. In the case of Covid-19, a false negative is far more detrimental than a false positive:$$\Huge P_t(T^+|D^+)=\frac{P_t(T^+\cap D^+)}{P_t(D^+)}=\frac{209/620}{220/620}=\frac{209}{220}\approx0.95$$$$\Huge P_t(T^-|D^-)=\frac{P_t(T^-\cap D^-)}{P_t(D^-)}=\frac{394/620}{400/620}=\frac{394}{400}=0.985$$