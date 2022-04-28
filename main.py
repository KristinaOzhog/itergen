nested_list = [
	['a', 'b', 'c'],
	['d', 'e', [4, 6, 8], 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, iter_list):
		self.iter_list = iter_list
		self.cursor = -1

	def __iter__(self):
		self.cursor += 1
		self.nested_cursor = 0
		return self

	def __next__(self):
		if self.nested_cursor == len(self.iter_list[self.cursor]):
			iter(self)
		if self.cursor == len(self.iter_list):
			raise StopIteration
		self.nested_cursor += 1
		return self.iter_list[self.cursor][self.nested_cursor - 1]


for item in FlatIterator(nested_list):
	print(item)

print([lst for lst in FlatIterator(nested_list)])

nested_list = [
	['a', 'b', ['s', 'g', 'k'], 'c'],
	['d', 'e', [4, 6, 8], 'f', 'h', False],
	[1, [True, 5], 2, None],
]


class FlatIterator:

	def __init__(self, iter_list):
		self.iter_list = iter_list

	def if_more_list(self, old_iter_list, new_iter_list):
		for elem in old_iter_list:
			if type(elem) != list:
				new_iter_list.append(elem)
			else:
				self.if_more_list(elem, new_iter_list)
		return new_iter_list

	def __iter__(self):
		self.cursor = -1
		return self

	def __next__(self):
		new_iter_list = []
		self.cursor += 1
		all_lists = self.if_more_list(self.iter_list, new_iter_list)
		if self.cursor >= len(all_lists):
			raise StopIteration
		return all_lists[self.cursor]




for item in FlatIterator(nested_list):
	print(item)

print([lst for lst in FlatIterator(nested_list)])

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(some_lst):
    for soml in some_lst:
        for sl in soml:
            yield sl


for item in flat_generator(nested_list):
    print(item)

print(list(flat_generator(nested_list)))

nested_list = [
    ['a', 'b', ['s', 'g', [True], 'l'], 'c'],
    ['d', 'e', [8, [1], 9, 5], 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
	for soml in some_list:
		if type(soml) == list:
			for more_sl in flat_generator(soml):
				yield more_sl
		else:
			yield soml


for item in flat_generator(nested_list):
	print(item)

print(list(flat_generator(nested_list)))


