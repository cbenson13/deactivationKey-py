import numbers
import numpy as np
import math
import chunk


base = np.fromfile('./Packet_Base.txt', dtype=int, sep='\n')
weight = np.fromfile('./Packet_Weight.txt', dtype=float, sep='\n')

print(np.split(base * weight, len(base)/ 8)[:4])
#print(np.split (base, len(base)/ 8)[:4])
#print(weight)

#Load both packets as a array
with open('Packet_Base.txt','r') as file1:
    data1=file1.read().splitlines()
with open('Packet_Weight.txt' , 'r') as file2:
    data2=file2.read().splitlines()

#Combine files as Mixer_data
Mixer_data = data1 + data2

#Data chunks into segments of 8
Chunked_data= np.array_split(Mixer_data,8)

#Multiply base by weight 
multiplied_array= [ x * y for x,y in zip(data1,data2)]

#Find min,max,mean // (max minusmean) times min
chunk_results = []
chunk_min = np.min(chunk)
chunk_max = np.max(chunk)
chunk_mean = np.mean(chunk)
chunk_result = (chunk_max - chunk_mean) * chunk_min
chunk_results.append(chunk_result)

#Find sum and round to nearest integer
sum_of_numbers = sum(numbers)
rounded_sum = round(sum_of_numbers)
print(rounded_sum)

#Find the remainder if you divided by 4096.
remainder = rounded_sum % 4096
print (remainder)