class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add_to_front(self, value):
    new_node = Node(value)
    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    else:
      self.tail= new_node
    self.head = new_node
    
  def add_to_end(self, value):
    new_node = Node(value)
    new_node.prev = self.tail
    if self.tail:
      self.tail.next = new_node
    else:
      self.head= new_node
    self.tai = new_node

  def delete_to_front(self, value):
    if not self.head:
      return None
    remved_value = self.head.value
    self.head = self.head.next
    if self.head:
      self.head.prev = None
    else:
      self.tail = None
    
    return remved_value

  def delete_to_end(self, value):
    if not self.tail:
      return None
    remved_value = self.tail.value
    self.tail = self.tail.prev
    if self.tail:
      self.tail.prev = None
    else:
      self.head = None
    
    return remved_value