# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatan Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East Coast'], ['The Caribbean', 'Yucatan Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatan Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

#list of dollar values of damages for each hurricane converted to float values
damages_floats=[]

#converts value in list of damages to a float by stripping "M" or "B", converting string to float and then multiplying by corresponding value depending on which letter was stripped from string, then appends to new list. if no damages were recorded, 'No damages recorded' appended to new list
def damages_update(damages):
    abrv = {"M":1000000, "B":1000000000}
    for value in damages:
        lettercheck = 0
        for letter in list(abrv.keys()):
            if letter in value:
                stripped_value = float(value.strip(letter))
                newvalue = stripped_value * abrv[letter]
                damages_floats.append(newvalue)
                lettercheck += 1
        if lettercheck == 0:
            damages_floats.append(value)

            

damages_update(damages)
#print(damages_floats)


# write your construct hurricane dictionary function here:

#dict of hurricanes where key is name, and value is a dict containing various info about the hurricane
hurricane_dict = {}

#iterates through range of indexes corresponding with number of hurricanes data has been provided for. updates hurricane_dict with key:value pair where key is the name of the hurricane at the current index, and value is a dict containing all data provided on the hurricane with damages entered as float values unless no data had been recorded
def construct_dict():
    for i in range(len(names)):
        hurricane_dict.update({names[i]:{'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':max_sustained_winds[i], 'Areas Affected':areas_affected[i], 'Damage':damages_floats[i], 'Deaths':deaths[i]}})

construct_dict()
#print(hurricane_dict)


# write your construct hurricane by year dictionary function here:

#dict of hurricanes where key is year of occurence, and value is a list containing dicts with data for each hurricane that occured in that year
hurricane_year_dict = {}

#iterates through the dicts stored as values in hurricane_dict, checks if the value for 'Year' in those dicts is currently a key in hurricane_year_dict. if not, creates a new key for the value contained in 'Year' with the dict corresponding to the current iteration stored inside a list as the value. if a matching key is found, appends the dict corresponding to the current iteration to the existing list that is stored as a value
def hurricanes_by_year():
    for i in hurricane_dict.values():
        if i['Year'] not in hurricane_year_dict:
            hurricane_year_dict[i['Year']] = [i]
        else:
            hurricane_year_dict[i['Year']].append(i)


hurricanes_by_year()
#print(hurricane_year_dict)

# write your count affected areas function here:

#dict where keys are areas affected by hurricanes and values are number of times area has been affected by hurricanes
affected_areas_dict = {}

#iterates through a list of tuples containing the name of the hurricane, and a dict containing information about the hurricane, and then iterates through the 'Areas Affected' key of the dict in each tuple, updating a new dict where keys are the areas affected by hurricanes with similar areas of close proximity combined into single keys, and values are the number of times that area has been affected by hurricanes
def count_affected_areas():
    for i in hurricane_dict.items():
        for area in i[1]['Areas Affected']:
            if area not in affected_areas_dict and area == 'South Florida':
                affected_areas_dict['Florida'] += 1
            elif 'Virgin Islands' in area:
                if 'Virgin Islands' not in affected_areas_dict:
                    affected_areas_dict['Virgin Islands'] = 1
                else:
                    affected_areas_dict['Virgin Islands'] += 1
            elif area not in affected_areas_dict and 'Panhandle' not in area:
                affected_areas_dict[area] = 1
            elif area in affected_areas_dict:
                affected_areas_dict[area] += 1
            elif area not in affected_areas_dict and 'Panhandle' in area:
                affected_areas_dict['United States Gulf Coast'] += 1
   
count_affected_areas()
#print(affected_areas_dict)

# write your find most affected area function here:







# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
