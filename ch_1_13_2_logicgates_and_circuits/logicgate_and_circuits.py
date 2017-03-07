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
    if self.pinA == None:    
      return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
    
    return self.pinA.getFrom().getOutput()
    
  def getPinB(self):
    if self.pinB == None:
      return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
    
    return self.pinB.getFrom().getOutput()
  
  def setNextPin(self, source):
    if self.pinA == None:
      self.pinA = source
    elif self.pinB == None:
      self.pinB = source
    else:
      raise RuntimeError("Error: NO EMPTY PINS")
        
class UnaryGate(LogicGate):
  
  def __init__(self, n):
    # initializing the inherited classes data items
    LogicGate.__init__(self, n)
    # Above can rewritten as super(UnaryGate, self).__init__(n)
    
    self.pin = None
    
  def getPin(self):
    if self.pin == None:
      return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))    
    else:
      return self.pin.getFrom().getOutput()
    
  def setNextPin(self, source):
    if self.pin == None:
      self.pin = source
    else:
      raise RuntimeError("Cannot Connect: NO EMPTY PINS on this gate.")
    
    
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
   
class Connector:
  
  def __init__(self, fgate, tgate):
    self.fromgate = fgate
    self.togate = tgate
    
    tgate.setNextPin(self)
    
  def getFrom(self):
    return self.fromgate
    
  def getTo(self):
    return self.togate
        
def main():
  g1 = AndGate("G1")
  g2 = AndGate("G2")
  g3 = OrGate("G3")
  g4 = NotGate("G4")
  c1 = Connector(g1,g3)
  c2 = Connector(g2,g3)
  c3 = Connector(g3,g4)
  print(g4.getOutput())

main()













