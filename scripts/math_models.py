"""Pure-stdlib numerical examples; not AI safety certification."""
from math import log, sqrt
from statistics import NormalDist

def entropy(probs):
    if not probs or any(p < 0 or p > 1 for p in probs) or abs(sum(probs)-1) > 1e-9:
        raise ValueError("Expected a normalized probability vector")
    return -sum(p*log(p, 2) for p in probs if p)

def brier_score(probs, outcomes):
    if not probs or len(probs) != len(outcomes):
        raise ValueError("Nonempty equal-length arrays required")
    if any(not 0 <= p <= 1 for p in probs) or any(y not in (0, 1) for y in outcomes):
        raise ValueError("Probabilities and binary outcomes required")
    return sum((p-y)**2 for p,y in zip(probs,outcomes))/len(probs)

def wilson_interval(successes, trials, confidence=0.95):
    if not isinstance(trials, int) or not isinstance(successes, int) or trials <= 0 or not 0 <= successes <= trials:
        raise ValueError("Invalid binomial observations")
    if not 0 < confidence < 1:
        raise ValueError("Confidence must lie in (0,1)")
    z = NormalDist().inv_cdf((1+confidence)/2)
    p = successes/trials
    denom = 1+z*z/trials
    center = (p+z*z/(2*trials))/denom
    radius = z/denom*sqrt(p*(1-p)/trials+z*z/(4*trials*trials))
    return max(0,center-radius),min(1,center+radius)

def discounted_return(rewards, discount):
    if not 0 <= discount <= 1:
        raise ValueError("Discount must lie in [0,1]")
    return sum(discount**i*r for i,r in enumerate(rewards))

def cvar_empirical(losses, alpha=0.95):
    if not losses or not 0 <= alpha < 1:
        raise ValueError("Nonempty losses and alpha in [0,1) required")
    # Rockafellar-Uryasev empirical CVaR; handles fractional tail mass.
    ordered=sorted(losses,reverse=True)
    tail_mass=(1-alpha)*len(ordered)
    full=int(tail_mass)
    frac=tail_mass-full
    weighted=sum(ordered[:full])
    if frac > 1e-12:
        weighted+=frac*ordered[full]
    return weighted/tail_mass
