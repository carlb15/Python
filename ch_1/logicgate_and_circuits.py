"""Logic Gate Classes. Multiple inheritance practice."""


class LogicGate:
    """Logic Gate Class."""

    def __init__(self, n):
        """Initialization for Logic Gate."""
        self.label = n
        self.output = None

    def getLabel(self):
        """Getter gate name."""
        return self.label

    def getOutput(self):
        """Getter output of gate."""
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """Binary Gate class -- two inputs, one output."""

    def __init__(self, n):
        """Initializing the inherited classes data items."""
        LogicGate.__init__(self, n)
        # Above can rewritten as super(BinaryGate, self).__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        """Getter for pin A."""
        if self.pinA is None:
            return int(input("Enter Pin A input " + self.getLabel() + "-->"))
        return self.pinA.getFrom().getOutput()

    def getPinB(self):
        """Getter for pin B."""
        if self.pinB is None:
            return int(input("Enter Pin B input " + self.getLabel() + "-->"))
        return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        """Setter for next pin."""
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    """Unary Gate Class."""

    def __init__(self, n):
        """Initializing the inherited classes data items."""
        LogicGate.__init__(self, n)
        # Above can rewritten as super(UnaryGate, self).__init__(n)

        self.pin = None

    def getPin(self):
        """Getter for pin."""
        if self.pin is None:
            return(int(input("Enter Pin input " + self.getLabel() + "-->")))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        """Setter for pin."""
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Cannot Connect: NO EMPTY PINS on this gate.")


class AndGate(BinaryGate):
    """And Gate Class."""

    def __init__(self, n):
        """Initializing the parent classes data items."""
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        """Perform gate logic."""
        a = self.getPinA()
        b = self.getPinB()

        return ((a == 1) and (b == 1))


class OrGate(BinaryGate):
    """Or Gate Class."""

    def __init__(self, n):
        """Initialization for Binary gate."""
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        """Perform gate logic."""
        a = self.getPinA()
        b = self.getPinB()

        return ((a == 1) or (b == 1))


class NotGate(UnaryGate):
    """Not Gate Class."""

    def __init__(self, n):
        """Initialization for Unary Gate."""
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        """Perform gate logic."""
        a = self.getPin()
        return (not a)


class NorGate(OrGate):
    """NOR Gate Class."""

    def performGateLogic(self):
        """Perform gate logic."""
        return not (super().performGateLogic())


class NandGate(AndGate):
    """Nand Gate Class."""

    def performGateLogic(self):
        """Perform gate logic."""
        return not (super().performGateLogic())


class XorGate(BinaryGate):
    """XOR Gate Class."""

    def __init__(self, n):
        """Initializing the parent classes data items."""
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        """Perform gate logic."""
        a = self.getPinA()
        b = self.getPinB()

        return ((a == 1 and b == 0) or (a == 0 and b == 1))



class HalfAdder(XorGate, AndGate):
    """Half Adder Class."""

    def __init__(self, n):
        """Initializing the parent classes data items."""
        XorGate.__init__(self, n)
        AndGate.__init__(self, n)

        self.sum = XorGate.performGateLogic(self)
        self.carry = AndGate.performGateLogic(self)

        def performGateLogic(self):
            """Perform half gate logic."""
            return self.carry, self.sum


class FullAdder(HalfAdder):
    """Full Adder Class."""

    def __init__(self, n):
        """Initializing the parent classes data items."""
        HalfAdder.__init__(self, n)

        self.carry = AndGate.performGateLogic(self)
        self.sum = XorGate.performGateLogic(self)

    def performGateLogic(self):
        """Perform half gate logic."""
        return self.carry, self.sum


class Connector:
    """Connector Gate Class."""

    def __init__(self, fgate, tgate):
        """Initialization for Connector class."""
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        """Getter for input gate."""
        return self.fromgate

    def getTo(self):
        """Getter for output gate."""
        return self.togate


def main():
    """Testing Classes.
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    Connector(g1, g3)
    Connector(g2, g3)
    Connector(g3, g4)
    print(g4.getOutput())

    g5 = NandGate("G5")
    g6 = NandGate("G6")
    g7 = AndGate("G7")
    Connector(g5, g7)
    Connector(g6, g7)
    print(g7.getOutput())

    g8 = XorGate("G8")
    print(g8.getOutput())"""

    g9 = HalfAdder("G9")
    print(g9.getOutput())

main()
