# Information theory, calibration and evidence

For discrete X with mass function p(x):

\[
H(X)=-\sum_x p(x)\log_2 p(x).
\]

Mutual information:

\[
I(X;Y)=\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}.
\]

Kullback–Leibler divergence:

\[
D_{KL}(P\Vert Q)=\sum_x p(x)\log\frac{p(x)}{q(x)}.
\]

KL divergence is asymmetric and infinite when q(x)=0 for any x with p(x)>0.

## Proper scoring rules

Brier score for binary events:

\[
BS=\frac{1}{n}\sum_{i=1}^n (p_i-y_i)^2.
\]

Log loss:

\[
LL=-\frac1n\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)].
\]

Calibration requires that events assigned probability p occur approximately p of the time in suitable groups. Calibration alone does not guarantee discrimination, fairness, causal validity or safety.

## Bayesian updating

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}.
\]

Bayes factors compare relative evidential support under explicitly specified likelihood models. They do not turn a disputed consciousness theory into an empirically validated detector.
