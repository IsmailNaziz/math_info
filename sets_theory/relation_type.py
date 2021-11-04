from inspect import signature
from random import choice
from itertools import product

class RelationChecker(object):

	def __init__(self, E, relation):
		self.E = tuple(set(E))
		self.relation = self._init_relation(relation)
		self.tuples_2 = [(i, j) for i,j in product(self.E, self.E)]	
		self.tuples_3 = [(i, *j) for i,j in product(self.E, product(self.E, self.E))]
		self.trans = self._transitive()
		self.reflex = self._reflexive()


	def _init_relation(self, relation):
		assert len(signature(relation).parameters) == 2
		return relation	

	@classmethod
	def _implies(cls, A, B):
		if not(A) or B:
			return True
		return False

	def _symmetry(self):
		for elem in self.tuples_2:
			x, y = elem[0], elem[1]
			if not(self._implies(self.relation(x, y), self.relation(y, x))):
				return False
		return True

	def _anti_symmerty(self):
		for elem in self.tuples_2:
			x, y = elem[0], elem[1]
			if not(self._implies(self.relation(x, y) and self.relation(y, x), x==y)):
				return False
		return True

	def _transitive(self):
		for elem in self.tuples_3:
			x, y, z = elem[0], elem[1], elem[2]
			if not(self._implies(self.relation(x, y) and self.relation(y, z), self.relation(x, z))):
				return False
		return True

	def _reflexive(self):
		for elem in self.E:
			if not(self.relation(elem, elem)):
				return False
		return True

	def is_equivalence_relation(self):
		if self._symmetry() and self.trans and self.reflex:
			print('the relation is an equivalence relation')
			return True 
		print('the relation is not an equivalence relation')
		return False

	def is_order_relation(self):
		if self._anti_symmerty() and self.trans and self.reflex:
			print('the relation is an order relation')
			return True 
		print('the relation is not an order relation')
		return False

	def is_total_order_relation(self):
		return 


if __name__ == '__main__':

	def greater_than_or_equal(x, y):
		if x >= y:
			return True
		return False

	E = [i for i in range(-100, 100)]

	RC = RelationChecker(E, greater_than_or_equal)
	RC.is_equivalence_relation()
	RC.is_order_relation()



