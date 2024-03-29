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
        assert checkout_solution.checkout('EEBB') == 110

    def test_11(self):
        assert checkout_solution.checkout('EEEE') == 160

    def test_12(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_13(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330

    def test_14(self):
        assert checkout_solution.checkout('EEEEBB') == 160

    def test_15(self):
        assert checkout_solution.checkout('FFF') == 20

    def test_16(self):
        assert checkout_solution.checkout('FFFFFF') == 40

    def test_17(self):
        assert checkout_solution.checkout('FFFF') == 30

    def test_18(self):
        assert checkout_solution.checkout('FF') == 20

    def test_19(self):
        assert checkout_solution.checkout('ABCDEF') == 165

    def test_20(self):
        assert checkout_solution.checkout('RRRQ') == 150

    def test_21(self):
        assert checkout_solution.checkout('UUUU') == 120

    def test_22(self):
        assert checkout_solution.checkout('UUUUUU') == 200

    def test_23(self):
        assert checkout_solution.checkout('UUU') == 120

    def test_24(self):
        assert checkout_solution.checkout('UUUUUUUU') == 240

    def test_25(self):
        assert checkout_solution.checkout('STX') == 45

    def test_26(self):
        assert checkout_solution.checkout('STXSTX') == 90

    def test_27(self):
        assert checkout_solution.checkout('SSSSSSS') == 110

    def test_28(self):
        assert checkout_solution.checkout('STXYZ') == 82

    def test_29(self):
        assert checkout_solution.checkout('XYZZ') == 62

