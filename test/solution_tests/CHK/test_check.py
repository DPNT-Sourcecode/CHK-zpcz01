from lib.solutions.CHK import checkout_solution


class TestCheck():
    def test_check(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('AAABB') == 175
        assert checkout_solution.checkout('AAAA') == 180

