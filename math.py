import gnu.math.CComplex

import gnu.math.DComplex

import gnu.math.DFloNum

import gnu.math.IntNum

import gnu.math.Numeric

import gnu.math.Quantity

import gnu.math.RealNum

class Complex(Quantity):
    """ generated source for class Complex """
    imMinusOne = CComplex()
    imOne = CComplex()

    @classmethod
    @overloaded
    def add(cls, complex_, complex2, n):
        """ generated source for method add """
        return Complex.make(RealNum.add(complex_.re(), complex2.re(), n), RealNum.add(complex_.im(), complex2.im(), n))

    @classmethod
    @overloaded
    def compare(cls, complex_, complex2):
        """ generated source for method compare """
        n = complex_.im().compare(object(complex2.im()))
        if n != 0:
            return n
        return complex_.re().compare(object(complex2.re()))

    @classmethod
    def divide(cls, complex_, complex2):
        """ generated source for method divide """
        if not complex_.isExact() or not complex2.isExact():
            return DComplex.div((complex_.doubleRealValue()), (complex_.doubleImagValue()), (complex2.doubleRealValue()), (complex2.doubleImagValue()))
        realNum = complex_.re()
        realNum2 = complex_.im()
        realNum3 = complex2.re()
        realNum4 = complex2.im()
        realNum5 = RealNum.add(RealNum.times(realNum3, realNum3), RealNum.times(realNum4, realNum4), 1)
        realNum6 = RealNum.add(RealNum.times(realNum, realNum3), RealNum.times(realNum2, realNum4), 1)
        realNum7 = RealNum.add(RealNum.times(realNum2, realNum3), RealNum.times(realNum, realNum4), -1)
        return Complex.make(RealNum.divide(realNum6, realNum5), RealNum.divide(realNum7, realNum5))

    @classmethod
    @overloaded
    def equals(cls, complex_, complex2):
        """ generated source for method equals """
        return complex_.re() == object(complex2.re()) and complex_.im() == object(complex_.im())

    @classmethod
    def imMinusOne(cls):
        """ generated source for method imMinusOne """
        if cls.imMinusOne == None:
            cls.imMinusOne = CComplex(RealNum(IntNum.zero()), RealNum(IntNum.minusOne()))
        return cls.imMinusOne

    @classmethod
    def imOne(cls):
        """ generated source for method imOne """
        if cls.imOne == None:
            cls.imOne = CComplex(RealNum(IntNum.zero()), RealNum(IntNum.one()))
        return cls.imOne

    @classmethod
    @overloaded
    def make(cls, d, d2):
        """ generated source for method make """
        if d2 == 0.0:
            return DFloNum(d)
        return DComplex(d, d2)

    @classmethod
    @make.register(object, RealNum, RealNum)
    def make_0(cls, realNum, realNum2):
        """ generated source for method make_0 """
        if realNum2.isZero():
            return realNum
        if not realNum.isExact() or not realNum2.isExact():
            return DComplex(realNum.doubleValue(), realNum2.doubleValue())
        return CComplex(realNum, realNum2)

    @classmethod
    @overloaded
    def neg(cls, complex_):
        """ generated source for method neg """
        return Complex.make(complex_.re().rneg(), complex_.im().rneg())

    @classmethod
    @overloaded
    def polar(cls, d, d2):
        """ generated source for method polar """
        return DComplex(d * Math.cos((d2)), d * Math.sin((d2)))

    @classmethod
    @polar.register(object, RealNum, RealNum)
    def polar_0(cls, realNum, realNum2):
        """ generated source for method polar_0 """
        return Complex.polar(realNum.doubleValue(), realNum2.doubleValue())

    @classmethod
    def power(cls, complex_, complex2):
        """ generated source for method power """
        if isinstance(complex2, (IntNum, )):
            return Complex(complex_.power(IntNum(complex2)))
        d = complex_.doubleRealValue()
        d2 = complex_.doubleImagValue()
        d3 = complex2.doubleRealValue()
        d4 = complex2.doubleImagValue()
        if d2 == 0.0 and d4 == 0.0 and (d >= 0.0 or Double.isInfinite((d)) or Double.isNaN((d))):
            return DFloNum(Math.pow((d), (d3)))
        return DComplex.power((d), (d2), (d3), (d4))

    @classmethod
    def times(cls, complex_, complex2):
        """ generated source for method times """
        realNum = complex_.re()
        realNum2 = complex_.im()
        realNum3 = complex2.re()
        realNum4 = complex2.im()
        return Complex.make(RealNum.add(RealNum.times(realNum, realNum3), RealNum.times(realNum2, realNum4), -1), RealNum.add(RealNum.times(realNum, realNum4), RealNum.times(realNum2, realNum3), 1))

    def abs(self):
        """ generated source for method abs """
        return DFloNum(Math.hypot((self.doubleRealValue()), (self.doubleImagValue())))

    @add.register(object, object, int)
    def add_0(self, object2, n):
        """ generated source for method add_0 """
        if isinstance(object2, (Complex, )):
            return Complex.add(self, Complex((object(object2))), n)
        return (Numeric((object(object2)))).addReversed(self, n)

    def addReversed(self, numeric, n):
        """ generated source for method addReversed """
        if isinstance(numeric, (Complex, )):
            return Complex.add(Complex(numeric), self, n)
        raise IllegalArgumentException()

    def angle(self):
        """ generated source for method angle """
        return DFloNum(Math.atan2((self.doubleImagValue()), (self.doubleRealValue())))

    @compare.register(object, object)
    def compare_0(self, object2):
        """ generated source for method compare_0 """
        if not (isinstance(object2, (Complex, ))):
            return (Numeric((object(object2)))).compareReversed(self)
        return Complex.compare(self, Complex((object(object2))))

    def div(self, object2):
        """ generated source for method div """
        if isinstance(object2, (Complex, )):
            return Complex.divide(self, Complex((object(object2))))
        return (Numeric((object(object2)))).divReversed(self)

    def divReversed(self, numeric):
        """ generated source for method divReversed """
        if isinstance(numeric, (Complex, )):
            return Complex.divide(Complex(numeric), self)
        raise IllegalArgumentException()

    def doubleImagValue(self):
        """ generated source for method doubleImagValue """
        return self.im().doubleValue()

    def doubleRealValue(self):
        """ generated source for method doubleRealValue """
        return self.doubleValue()

    def doubleValue(self):
        """ generated source for method doubleValue """
        return self.re().doubleValue()

    @equals.register(object, object)
    def equals_0(self, object2):
        """ generated source for method equals_0 """
        if object2 == None or not (isinstance(object2, (Complex, ))):
            return False
        return Complex == self, Complex((object(object2)))

    def exp(self):
        """ generated source for method exp """
        return Complex.polar(Math.exp((self.doubleRealValue())), self.doubleImagValue())

    def isExact(self):
        """ generated source for method isExact """
        return self.re().isExact() and self.im().isExact()

    def isZero(self):
        """ generated source for method isZero """
        return self.re().isZero() and self.im().isZero()

    def log(self):
        """ generated source for method log """
        return DComplex.log((self.doubleRealValue()), (self.doubleImagValue()))

    def longValue(self):
        """ generated source for method longValue """
        return self.re().longValue()

    def mul(self, object2):
        """ generated source for method mul """
        if isinstance(object2, (Complex, )):
            return Complex.times(self, Complex((object(object2))))
        return (Numeric((object(object2)))).mulReversed(self)

    def mulReversed(self, numeric):
        """ generated source for method mulReversed """
        if isinstance(numeric, (Complex, )):
            return Complex.times(Complex(numeric), self)
        raise IllegalArgumentException()

    @neg.register(object)
    def neg_0(self):
        """ generated source for method neg_0 """
        return Complex.neg(self)

    def number(self):
        """ generated source for method number """
        return self

    def sqrt(self):
        """ generated source for method sqrt """
        return DComplex.sqrt((self.doubleRealValue()), (self.doubleImagValue()))

    def toExact(self):
        """ generated source for method toExact """
        realNum = self.re()
        realNum2 = self.im()
        complex_ = realNum.toExact()
        complex2 = realNum2.toExact()
        if complex_ == realNum and complex2 == realNum2:
            return self
        return CComplex(RealNum(complex_), RealNum(complex2))

    def toInexact(self):
        """ generated source for method toInexact """
        if self.isExact():
            return self
        return DComplex(self.re().doubleValue(), self.im().doubleValue())

    def __str__(self, n):
        """ generated source for method toString """
        if self.im().isZero():
            return self.re().toString(n)
        string = self.im().toString(n) + "i"
        if string.charAt(0) != '-':
            string = "+" + string
        if self.re().isZero():
            return string
        return self.re().toString(n) + string