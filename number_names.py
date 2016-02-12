elements = {
	0:"",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen"
	
}

prefix = {
	2:"twen",
	3:"thir",
	4:"for",
	5:"fif",
	6:"six",
	7:"seven",
	8:"eigh",
	9:"nine"
}

suffix_over_tens = 'ty'
suffix_tens = 'teen'

def generate_name(n):
	try:
		name = elements[n]
	except KeyError:
		if n < 20:
			name = prefix[n % 10] + suffix_tens
		elif n < 100:
			name = prefix[n/10] + suffix_over_tens + elements[n%10]
		elif n < 1000:
			under_hundred = "" if generate_name(n%100) == "" else "and" + generate_name(n%100)
			name = elements[n/100] + 'hundred' + under_hundred
		elif n == 1000:
			name = "onethousand"
		else:
			name = ""

	return name

if __name__ == "__main__":
	nums = [ generate_name(x) for x in range(1,1001) ]
	import pprint
	pprint.pprint(nums)
	print reduce(lambda x,y: x + len(y), nums, 0)
	
		