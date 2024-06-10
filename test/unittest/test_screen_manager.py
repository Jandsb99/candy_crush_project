import unittest
from Candy_crush_project.screen_manager import ScreenManager


class TestScreenManagerChain(unittest.TestCase):
    def setUp(self):
        matriu = [[1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1]]
        self.sm = ScreenManager(matriu)

    def test_chain_fail_esquerra(self):
        self.assertFalse(self.sm.chain(0, 0, -1, 0))

    def test_chain_fail_superior(self):
        self.assertFalse(self.sm.chain(0, 0, 0, -1))

    def test_chain_fail_dreta(self):
        self.assertFalse(self.sm.chain(5, 0, 1, 0))

    def test_chain_fail_inferior(self):
        self.assertFalse(self.sm.chain(0, 5, 0, 1))

    def test_chain_fail_NO(self):
        self.assertFalse(self.sm.chain(0, 0, -1, -1))

    def test_chain_fail_NE(self):
        self.assertFalse(self.sm.chain(5, 0, 1, -1))

    def test_chain_fail_SO(self):
        self.assertFalse(self.sm.chain(0, 5, -1, 1))

    def test_chain_fail_SE(self):
        self.assertFalse(self.sm.chain(5, 5, 1, 1))

    def test_chain_pass(self):
        assert(self.sm.chain(0, 0, 0, 1))

    def test_chain_fail(self):
        self.assertFalse(self.sm.chain(0, 0, 1, 1))


class TestScreenManagerUnchained(unittest.TestCase):
    def setUp(self):
        matriu = [[1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,3],
                  [1,2,1,2,1,2,1]]
        self.sm = ScreenManager(matriu)

    def test_unchained_true_chain(self):
        value, dx, dy = self.sm.unchained(0, 0)
        self.assertTrue(value)
        self.assertEqual(dx, 0)
        self.assertEqual(dy, 1)

    def test_unchained_false(self):
        value, dx, dy = self.sm.unchained(6, 6)
        self.assertFalse(value)
        self.assertIsNone(dx)
        self.assertIsNone(dy)


class TestScreenManagerSwap(unittest.TestCase):
    def test_swap_return(self):
        a = 1
        b = 2
        c, d = ScreenManager.swap(a, b)
        self.assertEqual(a, d)
        self.assertEqual(b, c)


class TestScreenManagerCoordenades(unittest.TestCase):
    def setUp(self):
        matriu = [[1,4,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1]]
        self.sm = ScreenManager(matriu)

    def test_coordenades_return(self):
        x = 1
        y = 0
        self.assertEqual(self.sm.coordenades(x, y),4)

    def test_set_coordenades(self):
        x = 5
        y = 4
        v = 8
        self.sm.set_coordenades(x, y, v)
        self.assertEqual(self.sm.coordenades(x, y), v)


class TestScreenManagerRearrange(unittest.TestCase):
    def setUp(self):
        matriu = [[8,4,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1],
                  [1,2,1,2,1,2,1]]
        self.sm = ScreenManager(matriu)

    def test_rearrange(self):
        x0 = 0
        y0 = 0
        x1 = 1
        y1 = 0

        v0 = self.sm.coordenades(x0, y0)
        v1 = self.sm.coordenades(x1, y1)

        self.sm.rearrange(x0, y0, x1, y1)

        self.assertEqual(self.sm.coordenades(x0, y0), v1)
        self.assertEqual(self.sm.coordenades(x1, y1), v0)


class TestScreenManagerClear(unittest.TestCase):
    def setUp(self):
        matriu = [[1, 1, 1, 2, 1, 2, 1],
                  [1, 1, 1, 2, 1, 2, 1],
                  [1, 1, 1, 2, 1, 2, 1],
                  [1, 2, 1, 2, 1, 2, 1],
                  [1, 2, 1, 2, 1, 2, 1],
                  [1, 2, 1, 2, 1, 2, 1],
                  [1, 2, 1, 2, 1, 2, 1]]
        self.sm = ScreenManager(matriu)

    def test_clear_x(self):
        self.sm.clear(0, 0)
        self.assertEqual(self.sm.coordenades(0, 0),0)
        self.assertEqual(self.sm.coordenades(0, 1), 0)
        self.assertEqual(self.sm.coordenades(0, 2), 0)

