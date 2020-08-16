from datetime import datetime, timedelta
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

def damages_update(damages):
    
    abrv = {"M":1000000, "B":1000000000}

    for i in damages:
        lettercheck = 0

        #converts value in list of damages to a float by stripping "M" or "B", converting string to float and then multiplying by corresponding value depending on which letter was stripped from string, then appends to new list.             
        for letter in list(abrv.keys()):
            if letter in i:
                stripped_value = float(i.strip(letter))
                newvalue = stripped_value * abrv[letter]
                damages_floats.append(newvalue)
                lettercheck += 1

        #if no damages were recorded, 'Damages not recorded' appended to new list        
        if lettercheck == 0:
            damages_floats.append(i)

            

damages_update(damages)
#print(damages_floats)


# write your construct hurricane dictionary function here:

#dict of hurricanes where key is name, and value is a dict containing various info about the hurricane
hurricane_dict = {}


def construct_dict():

    #iterates through range of indexes corresponding with number of hurricanes data has been provided for. updates hurricane_dict with key:value pair where key is the name of the hurricane at the current index, and value is a dict containing all data provided on the hurricane with damages entered as float values unless no data had been recorded    
    for i in range(len(names)):
        hurricane_dict.update({names[i]:{
            'Name':names[i], 
            'Month':months[i], 
            'Year':years[i], 
            'Max Sustained Wind':max_sustained_winds[i], 
            'Areas Affected':areas_affected[i], 
            'Damage ($USD)':damages_floats[i], 
            'Deaths':deaths[i]}})

construct_dict()
#print(hurricane_dict)


# write your construct hurricane by year dictionary function here:

#dict of hurricanes where key is year of occurence, and value is a list containing dicts with data for each hurricane that occured in that year
hurricane_year_dict = {}

def hurricanes_by_year():

    #iterates through the dicts stored as values in hurricane_dict, checks if the value for 'Year' in those dicts is currently a key in hurricane_year_dict. if not, creates a new key for the value contained in 'Year' with the dict corresponding to the current iteration stored inside a list as the value. 
    #if a matching key is found, appends the dict corresponding to the current iteration to the existing list that is stored as a value    
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

def count_affected_areas():

    #iterates through a list of tuples containing the name of the hurricane, and a dict containing information about the hurricane
    for i in hurricane_dict.items():
        
        #iterates through the 'Areas Affected' key of the dict in each tuple, updating a new dict where keys are the areas affected by hurricanes with similar areas of close proximity combined into single keys, and values are the number of times that area has been affected by hurricanes    
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

#dict where the key is the name of the most affected area, and the value is a dict containing key value pairs corresponding to the number of hurricanes, and the average days between hurricanes)
most_affected_area = {}

def most_affected():
    
    currenthighnum = 0
    currenthigharea = 0
    
    #iterates through list of tuples containing area names, and number of times affected, and saves highest number and corresponding area to new variables
    for i in list(affected_areas_dict.items()):
        if i[1] > currenthighnum:
            currenthighnum = i[1]
            currenthigharea = i[0]
 
    
    yearlist = []
    monthlist = []
    
    #iterates through list of tuples each containing years of hurricanes, and a list containing dicts containing information regarding hurricanes that occured that year
    for i in list(hurricane_year_dict.items()):
    
        #checks the dict in each tuple to see if the saved high area is contained in areas affected, and if true, appends the year and month of hurricane to a new list    
        for info in i[1]:
            if currenthigharea in info['Areas Affected']:
                yearlist.append(i[0])
                monthlist.append(info['Month'])

    
    datelist = []
    deltalist = []
    average = 0
    
    #iterates through range corresponding to number of hurricanes the area was affected by
    #saves month and year to new variable as a string, parses string using strptime to create a datetime object and appends to new list
    for num in range(len(yearlist)):
        stringformat = monthlist[num] + " " + str(yearlist[num])
        dateobj = (datetime.strptime(stringformat, "%B %Y"))
        datelist.append(dateobj)
    
    #iterates through datelist with range one less than number of hurricanes, subtracts datetime one index forward from current index to retrieve timedelta between each hurricane
    #converts timedelta datetime object to string, cleans data and then converts string to int and appends to new list
    for num in range(len(datelist) - 1):
        deltalist.append(int(str(datelist[num + 1] - datelist[num]).strip("0:").strip(" days, ")))
    
    #calculates average delta in days between each hurricane that has affected the area and saves the value to a new variable
    for delta in deltalist:
        average += delta
    average = average / len(deltalist)
    
    #updates dict where key is most affected area, and value is dict containing number of hurricanes in period, and average days between hurricanes
    most_affected_area[currenthigharea] = {'Hurricanes from 1924 to 2018':currenthighnum, 'Days Between Hurricanes':average} 


most_affected()
#print(most_affected_area)

# write your greatest number of deaths function here:

#dict where the key is labelled 'Most Deaths' and value is a dict containing info about the hurricane that caused the most deaths
most_deaths_caused = {}

def most_deaths():

    deathhigh = 0
    
    #iterates through a list of tuples where keys are hurricane names, and values are dicts containing hurricane info
    #compares the value stored in the key 'Deaths' in each dict and compares it to the current highest value recorded
    #if value in current iteration is greater than value in variable, updates variable to value in current iteration and updates variable containing name to name of hurricane corresponding to current iteration
    for i in list(hurricane_dict.items()):
        if i[1]['Deaths'] > deathhigh:  
            deathhigh = i[1]['Deaths']
            deathinfo = i[1]

    #updates dict to contain a key labelled 'Most Deaths' and a value that is a dict containing info about the hurricane that caused the most deaths
    most_deaths_caused['Most Deaths'] = deathinfo


most_deaths()
#print(most_deaths_caused)

# write your catgeorize by mortality function here:

mortality_scale = {
    0:[0, 99],
    1:[100, 499],
    2:[500, 999],
    3:[1000, 9999],
    4:[10000, 999999999999]}

#dict containing keys that are increasing ratings of mortality, and values that contain dicts containing info about the hurricanes that have been given the corresponding mortality rating
mortality_ratings = {0:[],1:[],2:[],3:[],4:[]}

def rank_by_mortality():

    #iterates through a list of tuples where keys are hurricane names, and values are dicts containing hurricane info
    for i in list(hurricane_dict.items()):
        
        #iterates through range defined by number of tiers in mortality scale
        #checks if the value for deaths at the current iteration of hurricane dict is within the inclusive range contained in the list in each value of mortality scale
        #once rating in mortality scale is identified, appends a dict where key is name of hurricane, and value is dict containing hurricane info to the list contained in the value of the key in mortality ratings corresponding to the rating given to the hurricane
        for num in range(len(list(mortality_scale.values()))):
            if i[1]['Deaths'] >= mortality_scale[num][0] and i[1]['Deaths'] <= mortality_scale[num][1]:
                mortality_ratings[num].append({i[0]:i[1]})
                
rank_by_mortality()
#print(mortality_ratings)


# write your greatest damage function here:

#dict where the key is labelled 'Most Damaging Hurricane ($USD)' and value is a dict containing info about the hurricane that caused the most damage
greatest_damage_dict = {}

def greatest_damage():

    damagehigh = 0

    #iterates through a list of tuples where keys are hurricane names, and values are dicts containing hurricane info
    #compares the value stored in the key 'Damage' in each dict and compares it to the current highest value recorded
    #if value in current iteration is greater than value in variable, updates variable to value in current iteration and updates variable containing name to name of hurricane corresponding to current iteration
    for i in list(hurricane_dict.items()):
        if i[1]['Damage ($USD)'] == 'Damages not recorded':
            continue
        if i[1]['Damage ($USD)'] > damagehigh:
            damagehigh = i[1]['Damage ($USD)']
            damageinfo = i[1]

    #adds key in greatest damage dict labelled 'Most Damaging Hurricane ($USD)' with a value that is a dict containing info about the hurricane that caused the most damage
    greatest_damage_dict['Most Damaging Hurricane ($USD)']=damageinfo


greatest_damage()
#print(greatest_damage_dict)





# write your catgeorize by damage function here:
