import numpy as np

# Pick a decision you want to make. Make sure you pick a binary decision,
# meaning the answer is either yes or no: 
decision = "Should I do my homework for [insert class here] this evening?"

# Pick three factors that affect your decision and write them as strings
factor_1 = "Is the class after lunch?"
factor_2 = "Will the teacher in this class notice that I did not finish the work?"
factor_3 = "Will the work take longer than 40 minutes?"

# think about how much each of these factors matter
# create a numpy array of length 3 where the first
# value is how much the first factor matters, the 
# second value is how much the second factor matters
# etc:


weights = np.array([9, 6, 6])#your code here

# pick a value for the bias: explain to your partner what this means
bias = -10 # change this

# now create a numpy array that says if the factors are true or not.
# Use 1 = true, 0 = false
# for example, if your first factor is "rain", and it's not raining
# the first value in your array will be 0
factor_values = np.array([1, 1, 0])# your code here

# now the perceptron is going to calculate the outcome. Make sure you understand
# what this code is and what it does: 

output_1 = np.dot(weights,factor_values) + bias
if output_1 > 0:
	output = 1
else:
	output = 0 

# the rest of the code just prints this to output:
test_dict = {0 : "no", 1:"yes"}#{ 0 : "no",1 : "yes" }
print(decision)
print("*************************")
print(factor_1+": "+test_dict[factor_values[0]]+" | weight: "+ str(weights[0]))
print(factor_2+": "+test_dict[factor_values[1]]+ "| weight: "+ str(weights[1]))
print(factor_3+": "+test_dict[factor_values[2]]+" | weight: "+ str(weights[2]))
print("bias = "+str(bias))
print("*************************")
print("calculating decision ...")
print("*************************")
print("weighted sum = "+str(output_1))
print("final decision: "+ test_dict[output])

# print(output_1)




