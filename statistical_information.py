#basic function to find out mean , variance and other statistical information of data
import numpy as np

def calculate(list):

  try:
    assert len(list) == 9
  except :
    raise ValueError("List must contain nine numbers.")

#converting to 3x3 matrix
  matrix = np.array(list).reshape(3,3)
  axis = [0,1,None]

#find mean
  mean = [(np.mean(matrix , axis = i)).tolist() for i in axis]
#find variance
  variance = [(np.var(matrix , axis = i)).tolist() for i in axis ]
#find standard deviation
  std_dev = [(np.std(matrix , axis = i)).tolist() for i in axis ]
#find minimum  
  minimum = [(np.min(matrix , axis = i)).tolist() for i in axis ]
#find maximum
  maximum = [(np.max(matrix , axis = i)).tolist() for i in axis ]
#find sum
  summation = [np.sum(matrix , axis = i).tolist() for i in axis ]

#final results

  calculations = {"mean" : mean , "variance" : variance , "standard deviation" : std_dev , "max" : maximum , "min" : minimum , "sum" : summation }

  return calculations

