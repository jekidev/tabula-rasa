# Decision theory and robust optimization

## Expected utility

For a policy pi and uncertain state s:

EU(pi) = sum over s of P(s | information) times U(s, pi).

The utility function is a normative modeling assumption, not an objective measurement of moral value.

## Constrained sequential decisions

Maximize the expected discounted sum of rewards, subject to expected discounted cost constraints.

An expectation constraint cannot guarantee that rare catastrophic outcomes never occur. Consequential actions also require hard runtime controls.

## Conditional value at risk

For a loss random variable L and confidence level alpha between zero and one:

CVaR_alpha(L) = min over eta of { eta + E[max(L - eta, 0)] / (1 - alpha) }.

This measures upper-tail loss. It is not a certificate of safety.

## Distributionally robust optimization

Choose a policy to minimize the worst expected loss across an explicitly defined family of plausible deployment distributions. Conclusions depend on the uncertainty set containing realistic scenarios.

## Value of information

Gross value of information is the expected optimal utility after receiving evidence minus the optimal utility before receiving evidence. Net value also subtracts acquisition cost and any risks.

## Limits

Optimization models do not independently establish corrigibility, human legitimacy, or AI consciousness. Evaluate these properties in actual operational environments and report assumptions.