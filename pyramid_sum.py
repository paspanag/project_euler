class Pyramid(object):
	def __init__(self, in_file_path):
		self._pyr = {}
		with open(in_file_path, 'r') as pyr_file:
			# expecting a pyramid layout
			self._pyr = [ map(lambda x: (int(x), 0),line.split()) for line in pyr_file ]
			self._pyr = self._proc_layer_element()

	def _proc_layer_element(self, layer=0):
		try:
			current_layer = self._pyr[layer]
			self._pyr = self._proc_layer_element(layer+1)
			self._pyr[layer] =  self._proc_element(layer,acc=[])
			return self._pyr
		except IndexError:
			return self._pyr
	
	def _proc_element(self, level, offset=0, acc=[]):
		try:
			current = self._pyr[level][offset]
		except IndexError:
			return acc

		try:
			left = self._pyr[level+1][offset][1]
			right = self._pyr[level+1][offset+1][1]
			cur_val = self._pyr[level][offset][0], self._pyr[level][offset][0] + max(left,right)
		except IndexError:
		 	cur_val = self._pyr[level][offset][0], self._pyr[level][offset][0]

		acc.append(cur_val)

		return self._proc_element(level, offset +1, acc)
		

	def __repr__(self):
		return str(self._pyr)

	@property
	def data(self):
		return self._pyr

def left_is_bigger(left, right):
	return True if left[1] > right[1] else False

def find_path(pyr, layer=0, offset=0, acc=[]):
	acc.append(pyr[layer][offset][0])
	try:
		if not left_is_bigger(pyr[layer+1][offset], pyr[layer+1][offset+1]):
			offset += 1
		
		return find_path(pyr, layer+1, offset, acc)
	except IndexError:
		return acc
		
		

def pprint_pyr(pyr):
	for layer in pyr:
		print layer

if __name__ == "__main__":
	pyra = Pyramid("p067_triangle.txt")
	import pprint
	#pyra(0,0)
	x = find_path(pyra.data)
	print(x)
	print(sum(x))
	#print tri_max(pyra(13,0))
				