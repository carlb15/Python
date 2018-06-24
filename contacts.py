
class ContactList():
  def __init__(self, names):
    """
      names is a list of strings.
    """
    self.names = names
  
  def __hash__(self):
    """Conceptually we want to hash the set of names. Since set 
    type is mutable it cannot be hashed so we use a frozenset
    """
    return hash(frozenset(self.names))
 
 
  def __eq__(self, other):
    """ 
    In practice we'd store the underlying set and hash code
    remembering to void these values on updates.
    """
    return set(self.names) == set(other.names)
    
  def merge_contact_lists(self):
    """
    Contacts is a list of ContactList.
    """
    return list(set(self.names))

    

names = ['joe', 'amir', 'mary', 'ana', 'vannessa', 'joe', 'mary', 'mary']
contacts = ContactList(names)
print(contacts.merge_contact_lists())
   