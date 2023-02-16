import numpy as np
import struct
# Define the signal
def m(t):
    return -2 * np.cos(200*np.pi*t) + np.sin(50*np.pi*t)
#--------------------------------------TASK1----------------------------------------------------------------

sample_rate1 = 200   # we took the nyquist sample rate
dt1 = 1 / sample_rate1 #time interval of samples
t_values1 = np.arange(dt1, 2, dt1) # time value list that will be used for sampling
samples = m(t_values1)
required_samples = samples[:10]  #we took first 10 samples as wanted
Level = 128
delta_v = 6/128  #the length of a level
quantized_samples = []

# I just labelized the levels and I wrote -3.03 as final value to include min value = -3
levelsingle = np.arange(3,-3.03,-delta_v) 

#made this round function for down round when .5 case occur because if 127.5 come I have to take 127 instead of 128
def round(x):  
    if (x - np.floor(x)) > 0.5:
        return np.ceil(x)
    return np.floor(x)

#here I just quantized my samples as mid point of interval, border in the loop is the value of end of such an interval
for rsample in required_samples: 
    for border in levelsingle:
        if rsample >= border:
            final_quantized_sample = (2*border+delta_v)/2
            quantized_samples.append(final_quantized_sample)
            break


final_levels = []  
for samplee in quantized_samples:
    levelx = round((-(samplee-3))/(6/128))
    final_levels.append(levelx)   

#for integer to binary conversion
final_string= ""
for binary in final_levels:
        binary = bin(int(binary))
        binary = binary[2:]
        offset = 7 - len(binary)
        binary = '0'*offset + binary
        final_string += binary+"-"
final_string = final_string[0:-1]
final_string = '\"'+final_string+'\"'
print(final_string)


#----------------------------------------TASK2---------------------------------------------------------------


sample_rate2 = 800 #nyquist rate is 200 so we take 4 multiple of nyquist rate

dt2 = 1/sample_rate2  # this is the delta time period for samples

t_values2 = np.arange(dt2, 0.5, dt2) #list of the time values

#if we solve max|m'(t)| < Efs we will find E as 1.77
E = 1.77 #get from the equation above

t_values_requested = t_values2[0:20] #to list first 20 sample we get first 20 time value
sum = 0 #sum of the E values according to comparision will done in for loop 
Binary_code = "" #final result
for i in m(t_values_requested):
    if i < sum:   #if the message sample is smaller than sum value then we add 0 to our code and subtract E from total sum 
        Binary_code = Binary_code + "0"
        sum = sum - E
    else: #vice versa of < case
        Binary_code = Binary_code + "1"
        sum = sum + E
print(Binary_code)