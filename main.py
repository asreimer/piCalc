from mpmath import mp

# A python function to calculate pi accurate to an input tolerance
def calculate_pi_to_nth_digit(tol=mp.power(10,-1000)):
#TODO: calculate pi up to the Nth requested digit. Only output up to Nth digit.
	mp.dps = -mp.log10(tol)
	diff = mp.mpf(1)
	i = mp.mpf(0)
	prev = mp.mpf(1)
	total = mp.mpf(0)
	while (diff > tol):
		temp_sum = mp.mpf(0)
		temp_sum += mp.mpf(4.0) / (8.0*i + 1.0)
		temp_sum -= mp.mpf(2.0) / (8.0*i + 4.0)
		temp_sum -= mp.mpf(1.0) / (8.0*i + 5.0)
		temp_sum -= mp.mpf(1.0) / (8.0*i + 6.0)
		#print total, temp_sum, i
		total += temp_sum / (16.0**i)
		i += 1
		diff = mp.absmax(total - prev)
		prev = total

	return total


# A python function that calculates the base nth base 16 digit of Pi
# For reference, pi in base 16 = 3.243F6A8885A308D313198A2E03707344A4093822299F31....
def calculate_nth_digit_pi_b16(digit_num=2):
#TODO: Implement modular power for speed: https://en.wikipedia.org/wiki/Modular_exponentiation

	mp.dps = 5 + digit_num
	i = mp.mpf(0)
	total = mp.mpf(0)
	while (i <= digit_num):
		temp_sum1 = mp.fmod(mp.power(16,digit_num-i) / (8.0*i + 1.0),8.0*i + 1.0)
		temp_sum2 = mp.fmod(mp.power(16,digit_num-i) / (8.0*i + 4.0),8.0*i + 4.0)
		temp_sum3 = mp.fmod(mp.power(16,digit_num-i) / (8.0*i + 5.0),8.0*i + 5.0)
		temp_sum4 = mp.fmod(mp.power(16,digit_num-i) / (8.0*i + 6.0),8.0*i + 6.0)
		#print total, temp_sum, i
		total += 4*mp.fmod(temp_sum1,1) - 2*mp.fmod(temp_sum2,1) - mp.fmod(temp_sum3,1) - mp.fmod(temp_sum4,1)
		i += 1

	while (i < digit_num + 10):
		temp_sum = mp.mpf(0)
		temp_sum += mp.mpf(4.0) * mp.power(16,digit_num-i) / (8.0*i + 1.0)
		temp_sum -= mp.mpf(2.0) * mp.power(16,digit_num-i) / (8.0*i + 4.0)
		temp_sum -= mp.mpf(1.0) * mp.power(16,digit_num-i) / (8.0*i + 5.0)
		temp_sum -= mp.mpf(1.0) * mp.power(16,digit_num-i) / (8.0*i + 6.0)
		#print total, temp_sum, i
		total += temp_sum
		i += 1

	# Now convert to base 16 output
	output = int(mp.fmod(total,1)*16)
	return hex(output).split('x')[1]


#TODO: Implement other calculation methods, e.g.:https://en.wikipedia.org/wiki/Chudnovsky_algorithm