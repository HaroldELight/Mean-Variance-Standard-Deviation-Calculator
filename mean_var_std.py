import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    list_array = np.array(list).reshape(3,3)
    
    # mean
    mean_flat = np.mean(list_array)
    mean_axis0 = np.mean(list_array, axis=0)
    mean_axis1 = np.mean(list_array, axis=1)
    array_means = [mean_axis0.tolist(), mean_axis1.tolist(), mean_flat]

    # Variance
    variance_flat = np.var(list_array)
    variance_axis0 = np.var(list_array, axis=0)
    variance_axis1 = np.var(list_array, axis=1)
    array_variance = [variance_axis0.tolist(), variance_axis1.tolist(), variance_flat]

    # standard deviation
    std_dev_flat = np.std(list_array)
    std_dev_axis0 = np.std(list_array, axis=0)
    std_dev_axis1 = np.std(list_array, axis=1)
    array_std_dev = [std_dev_axis0.tolist(), std_dev_axis1.tolist(), std_dev_flat]

    # max
    max_flat = np.max(list_array)
    max_axis0 = np.max(list_array, axis=0)
    max_axis1 = np.max(list_array, axis=1)
    array_max = [max_axis0.tolist(), max_axis1.tolist(), max_flat]

    # min
    min_flat = np.min(list_array)
    min_axis0 = np.min(list_array, axis=0)
    min_axis1 = np.min(list_array, axis=1)
    array_min = [min_axis0.tolist(), min_axis1.tolist(), min_flat]

    # sum
    sum_flat = np.sum(list_array)
    sum_axis0 = np.sum(list_array, axis=0)
    sum_axis1 = np.sum(list_array, axis=1)
    array_sum = [sum_axis0.tolist(), sum_axis1.tolist(), sum_flat]

    # all into dictionary
    calculations = {'mean': array_means, 
                  'variance': array_variance, 
                  'standard deviation': array_std_dev, 
                  'max': array_max, 
                  'min': array_min, 
                  'sum': array_sum
                  }
    return(calculations) 