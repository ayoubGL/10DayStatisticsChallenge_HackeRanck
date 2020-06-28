"""
	In this challenge, we practice solving problems based on the Central Limit Theorem

	Task:
	 	A large elevator can transport a maximum of 8900 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean 205 of pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
"""
import math
if __name__ == "__main__":
	"""
		Since we have n > 30, we will use Central Limit Theorem to find mean of the sample and std
	""" 
	# input 


	max_w = int(input())
	n_boxes = int(input())
	mean_box = int(input())
	std_box = int(input())

	# find the mean and std of our new sample
	simple_mean = mean_box * n_boxes
	std_boxes = std_box * n_boxes ** 0.5

	# use CDF to compute the area under the curve
	p_n_boxes = 0.5 * (1 + math.erf((max_w - simple_mean)/(std_boxes * 2**0.5)))
	print(round(p_n_boxes,4))