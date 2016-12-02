#Compute the mean of car_speeds and assign it to mean_car_speed.
#Compute the mean of earthquake_intensities and assign the result to mean_earthquake_intensities. 
#This value will not be meaningful, because we shouldn't average values on a logarithmic scale this way.
car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]
mean_car_speed = sum(car_speeds) / len(car_speeds)
mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
#Make a line plot with day_numbers on the x axis and snail_crawl_length on the y axis.
#Make a line plot with day_numbers on the x axis and cars_in_parking_lot on the y axis.
plt.plot(day_numbers, snail_crawl_length)
plt.show()

plt.plot(day_numbers, cars_in_parking_lot)
plt.show()

