from lib.solutions.CHK import checkout_solution


class TestCheck():
    def test_check(self):
        assert checkout_solution.checkout('AAA') == 130
