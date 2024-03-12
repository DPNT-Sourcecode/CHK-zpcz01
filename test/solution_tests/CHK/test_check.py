from lib.solutions.CHK import checkout_solution


class TestCheck():
    def test_1(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_2(self):
        assert checkout_solution.checkout('BB') == 45

    def test_3(self):
        assert checkout_solution.checkout('AAABB') == 175

    def test_4(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_5(self):
        assert checkout_solution.checkout('BBB') == 75

    def test_6(self):
        assert checkout_solution.checkout('AAAAABBB') == 305

    def test_7(self):
        assert checkout_solution.checkout('ABCD') == 115
