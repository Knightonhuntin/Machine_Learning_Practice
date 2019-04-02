
import json
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.maps.world import World
filename = 'gdp.json'
with open(filename) as f:
	
	gdp_data = json.load(f)
	
#upload the data into an empyt library

cc_gdp_1994 ={}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] ==1994:
		GDP = int(float(gdp_dict['Value']))
		Country_Name = gdp_dict['Country Name']
		code = get_country_code(Country_Name)
		if code:
			cc_gdp_1994[code] = GDP
cc_gdp_2004 ={}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] ==2004:
		GDP = int(float(gdp_dict['Value']))
		Country_Name = gdp_dict['Country Name']
		code = get_country_code(Country_Name)
		if code:
			cc_gdp_2004[code] = GDP




#create a map of the world with gdp
wm_style1 = RotateStyle('#E6ADB3')
wm_style2 = RotateStyle('#008000')
wm1 = World(style = wm_style1)
wm2 = World(style  = wm_style2)

wm1.add('1994 GDP', cc_gdp_1994)

wm2.add('2004 GDP', cc_gdp_2004)
wm1.title = "1994 GDP"
wm2.title = "2004 GDP"

		
wm1.render_to_file('1994_GDP.svg')

wm2.render_to_file('2004_GDP.svg')
















