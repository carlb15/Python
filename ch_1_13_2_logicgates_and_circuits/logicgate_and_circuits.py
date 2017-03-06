class LogicGate:
  
  def __init__(self, n):
    self.label  = n
    self.output = None
    
  def getLabel(self):
    return self.label
    
  def getOutput(self):
    self.output = self.performGateLogic()
    return self.output
        
class BinaryGate(LogicGate):
  
  def __init__(self, n):
    # initializing the inherited classes data items
    LogicGate.__init__(self, n) 
    # Above can rewritten as super(BinaryGate, self).__init__(n)
    
    self.pinA = None
    self.pinB = None
    
  def getPinA(self):
    return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
    
  def getPinB(self):
    return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
    
class UnaryGate(LogicGate):
  
  def __init__(self, n):
    # initializing the inherited classes data items
    LogicGate.__init__(self, n)
    # Above can rewritten as super(UnaryGate, self).__init__(n)
    
    self.pin = None
    
  def getPin(self):
    return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))    
    
class AndGate(BinaryGate):
  
  def __init__(self, n):
    # Initializing the parent classes data items
    BinaryGate.__init__(self, n)    

  def performGateLogic(self):
    
    a = self.getPinA()
    b = self.getPinB()
    
    return ((a == 1) and (b == 1))
    
class OrGate(BinaryGate):
   
  def __init__(self, n):
    BinaryGate.__init__(self, n)
    
  def performGateLogic(self):
    a = self.getPinA()
    b = self.getPinB()
    
    return ((a == 1) or (b == 1))
    
class NotGate(UnaryGate):
  
  def __init__(self, n):
    UnaryGate.__init__(self, n)
    
  def performGateLogic(self):
    a = self.getPin()
    
    return (not a)
  
g1 = AndGate("G1")
print(g1.getOutput())

g2 = OrGate("G2")
print(g2.getOutput())

g3 = NotGate("G3")
print(g3.getOutput())
