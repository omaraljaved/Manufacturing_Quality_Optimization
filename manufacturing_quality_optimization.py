import numpy as np
import matplotlib.pyplot as plt

np.seterr(divide="ignore")

initial_param_1 = 5.0
initial_param_2 = 3.0

def manufacturing_quality_objective(param_1, param_2):
    defects = param_1 ** 2
    waste = param_2 ** 3
    return defects + waste

param_1 = initial_param_1
param_2 = initial_param_2
current_quality = manufacturing_quality_objective(param_1, param_2)

T0 = 100.0
M = 300
N = 15
alpha = 0.85
k = 0.1

temp = []
quality_values = []

for i in range(M):
    
    for j in range(N):
        
        rand_num_1 = np.random.rand()
        rand_num_2 = np.random.rand()
        
        step_size_1 = k * rand_num_1
        step_size_2 = k * rand_num_2
        
        param_1_temp = param_1 + step_size_1
        param_2_temp = param_2 + step_size_2
        
        quality_temp = manufacturing_quality_objective(param_1_temp, param_2_temp)
        
        rand_num = np.random.rand()
        formula = 1 / (np.exp((quality_temp - current_quality) / T0))
        
        if quality_temp <= current_quality:
            param_1 = param_1_temp
            param_2 = param_2_temp
            current_quality = quality_temp
        elif rand_num <= formula:
            param_1 = param_1_temp
            param_2 = param_2_temp
            current_quality = quality_temp
        else:
            param_1 = param_1
            param_2 = param_2
    
    temp.append(T0)
    quality_values.append(current_quality)
    T0 = alpha * T0

plt.plot(temp, quality_values)
plt.title("Quality Improvement at Temperature Values", fontsize=20, fontweight='bold')
plt.xlabel("Temperature", fontsize=18, fontweight='bold')
plt.ylabel("Quality Value", fontsize=18, fontweight='bold')

plt.xlim(max(temp), 0)
plt.xticks(np.arange(min(temp), max(temp), 100), fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()
