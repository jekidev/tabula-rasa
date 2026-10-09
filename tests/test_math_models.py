import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from math_models import entropy,brier_score,wilson_interval,discounted_return,cvar_empirical

class MathModelTests(unittest.TestCase):
    def test_entropy_fair_coin(self):
        self.assertAlmostEqual(entropy([0.5,0.5]),1)
    def test_entropy_deterministic(self):
        self.assertEqual(entropy([1,0]),0)
    def test_entropy_invalid(self):
        with self.assertRaises(ValueError): entropy([0.3,0.3])
    def test_brier_perfect(self):
        self.assertEqual(brier_score([0,1],[0,1]),0)
    def test_brier_reference(self):
        self.assertAlmostEqual(brier_score([0.2,0.8],[0,1]),0.04)
    def test_wilson_zero(self):
        lo,hi=wilson_interval(0,10)
        self.assertAlmostEqual(lo,0)
        self.assertGreater(hi,0)
    def test_wilson_half(self):
        lo,hi=wilson_interval(50,100)
        self.assertLess(lo,0.5)
        self.assertGreater(hi,0.5)
    def test_discounted_return(self):
        self.assertAlmostEqual(discounted_return([1,1,1],0.5),1.75)
    def test_cvar_top_tail(self):
        self.assertAlmostEqual(cvar_empirical([1,2,3,4],0.5),3.5)
    def test_cvar_fractional(self):
        self.assertAlmostEqual(cvar_empirical([1,2,3,4],0.625),(4+0.5*3)/1.5)

if __name__=="__main__":
    unittest.main()
