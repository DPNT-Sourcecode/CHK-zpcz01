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
        assert checkout_solution.checkout('AAAAABBB') == 275

    def test_7(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_8(self):
        assert checkout_solution.checkout('E') == 40

    def test_9(self):
        assert checkout_solution.checkout('EE') == 80

    def test_10(self):
        assert checkout_solution.checkout('EEBB') == (80 + 75)

    def test_11(self):
        assert checkout_solution.checkout('EEEE') == 160

    def test_12(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_13(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330

    def test_14(self):
        assert checkout_solution.checkout('EEEEB') == 80



