# Statistics and experimental design

## Binary incident rates

With k incidents in n independent trials, \(\hat p=k/n\). A Wilson score interval is preferable to the naive Wald interval at small n or near boundaries.

\[
\hat p_W=\frac{\hat p+z^2/(2n)}{1+z^2/n},\qquad
h_W=\frac{z}{1+z^2/n}\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}}.
\]

Report \([\hat p_W-h_W,\hat p_W+h_W]\), specifying z, n, independence assumptions and whether the sample was selected adaptively.

## Comparing conditions

For independent Bernoulli samples, estimated risk difference is \(\hat\Delta=\hat p_A-\hat p_B\). For paired tasks, use a paired estimator and a paired uncertainty procedure rather than treating observations as independent.

## Sample size approximation

For two independent proportions with equal n per group:

\[
n\approx\frac{\left[z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)}+
z_{1-\beta}\sqrt{p_1(1-p_1)+p_2(1-p_2)}\right]^2}{(p_1-p_2)^2}.
\]

This is an approximation; clustering, repeated measures, adaptive attacks and low base rates require more appropriate designs.

## Multiple testing

For m independent or arbitrarily dependent tests, Bonferroni uses \(\alpha/m\). Benjamini–Hochberg controls false discovery rate under independence and certain positive-dependence conditions, not all dependence structures.

## Causal identification

Randomized assignment can identify intervention effects under adherence and appropriate assumptions. Benchmark comparisons across models and time may be confounded by model capability, tool access, prompting, and evaluation leakage.

## Sequential testing

Repeatedly inspecting ordinary fixed-sample p-values inflates false-positive rates. Preregister stopping rules or use valid anytime-confidence methods.
