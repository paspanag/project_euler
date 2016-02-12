thirties = [ 3,5,8,10 ]
thirty_ones = [0,2,4,6,7,9,11]
why_greg = [ 1 ]
days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]

YEAR = 365
LEAP = 366

def get_mod_n_f(n):
	def mod_n(x):
		return True if x % n == 0 else False
	return mod_n

mod_4 = get_mod_n_f(4)
mod_100 = get_mod_n_f(100)
mod_400 = get_mod_n_f(400)

def month_offset_from_jan_1(d,m,y):
	offset = 0
	for month in range(0,m):
		offset += days_in_month(y,month)
	return offset + d

def days_in_month(y,m):
	if m in thirties:
		return 30
	elif m in thirty_ones:
		return 31
	else:
		if is_leap(y):
			return 29
		else:
			return 28

def offset_to_m_d_y(offset, y=1900, m=0, d=1):
	if offset == 0:
		return d,m,y
	elif offset - (LEAP if is_leap(y) else YEAR) >= 0:
		return offset_to_m_d_y(offset -  (LEAP if is_leap(y) else YEAR), y + 1, m, d)
	elif offset - days_in_month(y,m) >= 0:
		return offset_to_m_d_y(offset - days_in_month(y,m), y, m + 1, d)
	else:
		return offset_to_m_d_y(0, y, m, d+offset)
	

def what_day(offset):
	return days[ offset % 7 ]

def date_to_offset(d,m,y,zero=(1,0,1900)):
	year_off = y - zero[2]
	leap_years = len([ x for x in range(zero[2], y) if is_leap(x)])
	return YEAR * (y - zero[2]) + leap_years + month_offset_from_jan_1(d,m,y) - 1 # -1 is to offset

def is_leap(year):
	return mod_4(year) and ( not mod_100(year) or ( mod_100(year) and mod_400(year)))

def sundays(year, counter):
	pass

if __name__ == "__main__":
#	for x in range(1900, 2016):
#		if is_leap(x):
#			print "{0} is a leap year".format(x)

	print " From goog 42408 since jan 1 1900 on feb 10 2016"
	print date_to_offset(10,1,2016)
	print what_day(date_to_offset(1,1,2016))
	print offset_to_m_d_y(date_to_offset(1,1,2016))

	sundays = [ x for x in range(0, date_to_offset(1, 1, 1901)) if x % 7 == 6 ]
	first_of_month = [ x for x in sundays if offset_to_m_d_y(x)[0] == 1 ]
	print len(first_of_month)
	#print sundays
	#print what_day(36644)
	#print offset_to_m_d_y(36644)
	#for day_offset in first_of_month:
	#	print offset_to_m_d_y(day_offset), what_day(day_offset)


