# Loi de composition interne
#     Pour tous a et b éléments de G, le résultat a • b est aussi dans G.
# Associativité
#     Pour tous éléments a, b et c de G, l'égalité (a • b) • c = a • (b • c) est vraie.
# Élément neutre
#     Il existe un élément e de G tel que, pour tout a dans G, e • a = a • e = a, "e" est appelé élément neutre du groupe (G, •).
# Inverse
#     Pour tout élément a de G, il existe b dans G tel que a • b = b • a = e, où e est l'élément neutre. b est appelé symétrique de a.


class GroupChecker(object):

	def __init__(self, E, operation):
		self.E = E
		self.operation = operation
		self.tuples_2 = [(i, j) for i,j in product(self.E, self.E)]	
		self.tuples_3 = [(i, *j) for i,j in product(self.E, product(self.E, self.E))]


	def _is_intern_composition_operation(self):
		for x, y in self.tuples_2:
			if self.operation(x, y) not in self.E:
				return False
		return True

	def _is_associative(self):
		for x, y, z in self.tuples_3:
			if self.operation(self.operation(x, y),z) != self.operation(x, self.operation(y,z)) :
				return False
		return True

	def _is_symetric(self):
		for x, y in self.tuples_2:
			if self.operation(x, y) != self.operation(y, x):
				return False
		return True

	def has_neutral_element(self):
		neutral_elem = None
		for potential_neutral_elem in self.E:
			counter = 0
			for x in self.E:
				if self.operation(x, potential_neutral_elem) == self.operation(potential_neutral_elem, x) == x:
					counter +=1
					if counter == len(self.E):
						neutral_elem = potential_neutral_elem
						return {'result': False if neutral_elem == None else True, 'value' :neutral_elem}
				else:
					break
		return {'result': False if neutral_elem == None else True, 'value' :neutral_elem}

	def _all_have_inverse(self):
		res_neut_elem = self.has_neutral_element()
		if res_neut_elem['result']:
			for elem in self.E:
				if not self._has_inverse(elem, res_neut_elem['value']):
					return False
			return True
		return False

	def _has_inverse(self, elem, neutral_elem):
		for potential_inverse in self.E:
			if self.operation(elem, potential_neutral_elem) == self.operation(potential_neutral_elem, elem)\
					== neutral_elem:
				return True
		return False

	def is_group(self):
		if self._is_intern_composition_operation() and self._is_associative() \
			and self.has_neutral_element()['result']: 
			print("E muni de l'opération fournie est un groupe")
			return True
		print("E muni de l'opération fournie n'est pas un groupe")
		return False

	def is_abelian(self):
		if self.is_group() and self._is_symetric(): 
			print("E muni de l'opération fournie est un groupe abélien")
			return True
		print("E muni de l'opération fournie n'est pas un groupe abélien")
		return Falsehas_neutral_element
