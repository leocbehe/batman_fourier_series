import math
import numpy as np
from numpy import pi,sin,cos
import matplotlib.pyplot as plt

terms = 70
a_const = 13/16
x_start = 0
x_stop = 6*pi
x_inc = 500

def main():
	a_coefficients = calc_a(terms)
	b_coefficients = calc_b(terms)
	x_vals = np.arange(x_start, x_stop, (x_stop-x_start)/x_inc, dtype=np.float16)
	y_vals = []
	for x in x_vals:
		cos_terms = sum_cos_terms(terms, a_coefficients, x)
		sin_terms = sum_sin_terms(terms, b_coefficients, x)
		total_value = a_const * 0.5 + cos_terms + sin_terms
		y_vals.append(total_value)
	plt.plot(x_vals, y_vals)
	plt.title("Batman; terms={0:0.2f}; x_values={0:0.2f}".format(terms, x_inc))
	plt.show()
	

def calc_a(terms):
	coefficients = np.arange(0, terms, dtype=np.float16)
	for i in range(0, terms):
		n = i+1
		coefficient_section_1 = 4/(n**2 + pi**2)
		coefficient_section_2 = 2*cos(n*pi / 4) + 2*cos(5*pi*n / 4) - cos(3*n*pi / 8) \
			- cos(9*n*pi / 8) - cos(12*n*pi / 8) - 1
		coefficient = coefficient_section_1 * coefficient_section_2
		coefficients[i] = coefficient
	return coefficients
	
def calc_b(terms):
	coefficients = np.arange(0, terms, dtype=np.float16)
	for i in range(0, terms):
		n = i+1
		coefficient_section_1 = 4/(n**2 + pi**2)
		coefficient_section_2 = 2*sin(n*pi / 4) + 2*sin(5*pi*n / 4) - sin(3*n*pi / 8) \
			- sin(9*n*pi / 8) - sin(12*n*pi / 8)
		coefficient = coefficient_section_1 * coefficient_section_2
		coefficients[i] = coefficient
	return coefficients
	
def sum_cos_terms(terms, a_coefficients, x):
	sum_of_terms = 0.0
	for i in range(0, terms):
		n = i+1
		term = a_coefficients[i] * cos(n*x)
		sum_of_terms += term
	return sum_of_terms
	
def sum_sin_terms(terms, b_coefficients, x):
	sum_of_terms = 0.0
	for i in range(0, terms):
		n = i+1
		term = b_coefficients[i] * sin(n*x)
		sum_of_terms += term
	return sum_of_terms
	
if __name__ == "__main__":
	main()