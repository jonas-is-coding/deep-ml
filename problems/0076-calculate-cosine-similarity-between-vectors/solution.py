import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot = []
	v1_2 = 0.0
	v2_2 = 0.0	

	if len(v1) != len(v2):
		return -1

	for i in range(len(v1)):
		v1_2 += v1[i]**2
		v2_2 += v2[i]**2

	v1_2 = np.sqrt(v1_2)
	v2_2 = np.sqrt(v2_2)

	for i in range(len(v1)):
		dot.append(v1[i] * v2[i])

	return sum(dot) / (v1_2 * v2_2)
	