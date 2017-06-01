import time
from iterate import solve_hub

start_time = time.time()

# format 'yyyy-mm-dd'
start_date = '2015-01-01'
end_date = '2015-12-31'

# travel rate in miles per minutes 
travel_rate = 50/60.

# length of work day in minutes
day_length = 720

# minutes per truck un/loading on average
handle = 90

# maximum number of trucks to solve for on one day. Likely will not be
# used, but will keep the model from getting stuck on a large day
fleet_upper_bound = 12

# number of possible days on which each drop-off/pick-up can be made
window = 2

# location of the excel file containing all of the demand data
directory_name = '/mnt/c/Users/Sean/Documents/School/Senior Year/GE 494/data/'
file_name = 'Project_Info_Extra_Handles.xlsx'
file_path = directory_name + file_name

chicago_variations = ['Chicago Base', 'Chicago + Milwaukee', 'Chicago + Peoria', 
		'Chicago + Milwaukee and Peoria']

kansas_city_variations = ['KC Base', 'KC + Lincoln', 'KC + Wichita',
		'KC + Lincoln and Wichita'] 

# city name in quotes must match the city name in
# "[city name] coordinates" sheet in excel that we read from 
regions = {
	'Chicago': chicago_variations,
	'Kansas City': kansas_city_variations
}

fixed_parameters = {
	'start_date': start_date,
	'end_date': end_date,
    'travel_rate': travel_rate,
    'day_length': day_length,
    'handle': handle,
    'fleet_upper_bound': fleet_upper_bound,
    'window': window,
    'directory_name': directory_name,
    'file_name': file_name,
    'file_path': file_path 
}

# find the number of equipment haulers and equipment sets needed to satisfy
# demand, as well as the number of miles the fleet of equipment haulers travel
# for each variation of hub
if __name__ == '__main__':
    for region in regions.keys():
    	for variation in regions[region]:
    		solve_variation(fixed_parameters, region, variation)

end_time = time.time()
hours = int((end_time - start_time)/3600)
minutes = int((end_time - start_time)/60) - 60*hours
seconds = int(end_time - start_time) - 60*minutes - 3600*hours

print('runtime --- %s hours, %s minutes, %s seconds' % (hours, minutes, seconds))