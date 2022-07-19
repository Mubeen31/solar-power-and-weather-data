import requests
import csv
import time
from datetime import datetime

complete_api_link = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true&metric=true'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data['DailyForecasts'][0])

date_time_0 = api_data['DailyForecasts'][0]['Date']
get_date_time = datetime.strptime(date_time_0, '%Y-%m-%dT%H:%M:%S%z')
dte_0 = get_date_time.strftime('%Y-%m-%d')
sun_rise_date_time_0 = api_data['DailyForecasts'][0]['Sun']['Rise']
get_sun_rise_date_time_0 = datetime.strptime(sun_rise_date_time_0, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_rise_0 = get_sun_rise_date_time_0.strftime('%H:%M')
sun_set_date_time_0 = api_data['DailyForecasts'][0]['Sun']['Set']
get_sun_set_date_time_0 = datetime.strptime(sun_set_date_time_0, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_set_0 = get_sun_set_date_time_0.strftime('%H:%M')
hours_of_sun_0 = api_data['DailyForecasts'][0]['HoursOfSun']
solar_irradiance_0 = api_data['DailyForecasts'][0]['Day']['SolarIrradiance']['Value']
temp_max_0 = api_data['DailyForecasts'][0]['Temperature']['Maximum']['Value']
weather_status_0 = api_data['DailyForecasts'][0]['Day']['IconPhrase']
cloud_cover_0 = api_data['DailyForecasts'][0]['Day']['CloudCover']
real_feel_temp_0 = api_data['DailyForecasts'][0]['RealFeelTemperature']['Maximum']['Value']
uv_index_0 = api_data['DailyForecasts'][0]['AirAndPollen'][5]['Value']
pre_probability_0 = api_data['DailyForecasts'][0]['Day']['PrecipitationProbability']
rain_probability_0 = api_data['DailyForecasts'][0]['Day']['RainProbability']
wind_speed_0 = api_data['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']
wind_direction_0 = api_data['DailyForecasts'][0]['Day']['Wind']['Direction']['Localized']




date_time_1 = api_data['DailyForecasts'][1]['Date']
get_date_time = datetime.strptime(date_time_1, '%Y-%m-%dT%H:%M:%S%z')
dte_1 = get_date_time.strftime('%Y-%m-%d')
sun_rise_date_time_1 = api_data['DailyForecasts'][1]['Sun']['Rise']
get_sun_rise_date_time_1 = datetime.strptime(sun_rise_date_time_1, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_rise_1 = get_sun_rise_date_time_1.strftime('%H:%M')
sun_set_date_time_1 = api_data['DailyForecasts'][1]['Sun']['Set']
get_sun_set_date_time_1 = datetime.strptime(sun_set_date_time_1, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_set_1 = get_sun_set_date_time_1.strftime('%H:%M')
hours_of_sun_1 = api_data['DailyForecasts'][1]['HoursOfSun']
solar_irradiance_1 = api_data['DailyForecasts'][1]['Day']['SolarIrradiance']['Value']
temp_max_1 = api_data['DailyForecasts'][1]['Temperature']['Maximum']['Value']
weather_status_1 = api_data['DailyForecasts'][1]['Day']['IconPhrase']
cloud_cover_1 = api_data['DailyForecasts'][1]['Day']['CloudCover']
real_feel_temp_1 = api_data['DailyForecasts'][1]['RealFeelTemperature']['Maximum']['Value']
uv_index_1 = api_data['DailyForecasts'][1]['AirAndPollen'][5]['Value']
pre_probability_1 = api_data['DailyForecasts'][1]['Day']['PrecipitationProbability']
rain_probability_1 = api_data['DailyForecasts'][1]['Day']['RainProbability']
wind_speed_1 = api_data['DailyForecasts'][1]['Day']['Wind']['Speed']['Value']
wind_direction_1 = api_data['DailyForecasts'][1]['Day']['Wind']['Direction']['Localized']

date_time_2 = api_data['DailyForecasts'][2]['Date']
get_date_time = datetime.strptime(date_time_2, '%Y-%m-%dT%H:%M:%S%z')
dte_2 = get_date_time.strftime('%Y-%m-%d')
sun_rise_date_time_2 = api_data['DailyForecasts'][2]['Sun']['Rise']
get_sun_rise_date_time_2 = datetime.strptime(sun_rise_date_time_2, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_rise_2 = get_sun_rise_date_time_2.strftime('%H:%M')
sun_set_date_time_2 = api_data['DailyForecasts'][2]['Sun']['Set']
get_sun_set_date_time_2 = datetime.strptime(sun_set_date_time_2, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_set_2 = get_sun_set_date_time_2.strftime('%H:%M')
hours_of_sun_2 = api_data['DailyForecasts'][2]['HoursOfSun']
solar_irradiance_2 = api_data['DailyForecasts'][2]['Day']['SolarIrradiance']['Value']
temp_max_2 = api_data['DailyForecasts'][2]['Temperature']['Maximum']['Value']
weather_status_2 = api_data['DailyForecasts'][2]['Day']['IconPhrase']
cloud_cover_2 = api_data['DailyForecasts'][2]['Day']['CloudCover']
real_feel_temp_2 = api_data['DailyForecasts'][2]['RealFeelTemperature']['Maximum']['Value']
uv_index_2 = api_data['DailyForecasts'][2]['AirAndPollen'][5]['Value']
pre_probability_2 = api_data['DailyForecasts'][2]['Day']['PrecipitationProbability']
rain_probability_2 = api_data['DailyForecasts'][2]['Day']['RainProbability']
wind_speed_2 = api_data['DailyForecasts'][2]['Day']['Wind']['Speed']['Value']
wind_direction_2 = api_data['DailyForecasts'][2]['Day']['Wind']['Direction']['Localized']

date_time_3 = api_data['DailyForecasts'][3]['Date']
get_date_time = datetime.strptime(date_time_3, '%Y-%m-%dT%H:%M:%S%z')
dte_3 = get_date_time.strftime('%Y-%m-%d')
sun_rise_date_time_3 = api_data['DailyForecasts'][3]['Sun']['Rise']
get_sun_rise_date_time_3 = datetime.strptime(sun_rise_date_time_3, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_rise_3 = get_sun_rise_date_time_3.strftime('%H:%M')
sun_set_date_time_3 = api_data['DailyForecasts'][3]['Sun']['Set']
get_sun_set_date_time_3 = datetime.strptime(sun_set_date_time_3, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_set_3 = get_sun_set_date_time_3.strftime('%H:%M')
hours_of_sun_3 = api_data['DailyForecasts'][3]['HoursOfSun']
solar_irradiance_3 = api_data['DailyForecasts'][3]['Day']['SolarIrradiance']['Value']
temp_max_3 = api_data['DailyForecasts'][3]['Temperature']['Maximum']['Value']
weather_status_3 = api_data['DailyForecasts'][3]['Day']['IconPhrase']
cloud_cover_3 = api_data['DailyForecasts'][3]['Day']['CloudCover']
real_feel_temp_3 = api_data['DailyForecasts'][3]['RealFeelTemperature']['Maximum']['Value']
uv_index_3 = api_data['DailyForecasts'][3]['AirAndPollen'][5]['Value']
pre_probability_3 = api_data['DailyForecasts'][3]['Day']['PrecipitationProbability']
rain_probability_3 = api_data['DailyForecasts'][3]['Day']['RainProbability']
wind_speed_3 = api_data['DailyForecasts'][3]['Day']['Wind']['Speed']['Value']
wind_direction_3 = api_data['DailyForecasts'][3]['Day']['Wind']['Direction']['Localized']

date_time_4 = api_data['DailyForecasts'][4]['Date']
get_date_time = datetime.strptime(date_time_4, '%Y-%m-%dT%H:%M:%S%z')
dte_4 = get_date_time.strftime('%Y-%m-%d')
sun_rise_date_time_4 = api_data['DailyForecasts'][4]['Sun']['Rise']
get_sun_rise_date_time_4 = datetime.strptime(sun_rise_date_time_4, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_rise_4 = get_sun_rise_date_time_4.strftime('%H:%M')
sun_set_date_time_4 = api_data['DailyForecasts'][4]['Sun']['Set']
get_sun_set_date_time_4 = datetime.strptime(sun_set_date_time_4, '%Y-%m-%dT%H:%M:%S%z')
dte_sun_set_4 = get_sun_set_date_time_4.strftime('%H:%M')
hours_of_sun_4 = api_data['DailyForecasts'][4]['HoursOfSun']
solar_irradiance_4 = api_data['DailyForecasts'][4]['Day']['SolarIrradiance']['Value']
temp_max_4 = api_data['DailyForecasts'][4]['Temperature']['Maximum']['Value']
weather_status_4 = api_data['DailyForecasts'][4]['Day']['IconPhrase']
cloud_cover_4 = api_data['DailyForecasts'][4]['Day']['CloudCover']
real_feel_temp_4 = api_data['DailyForecasts'][4]['RealFeelTemperature']['Maximum']['Value']
uv_index_4 = api_data['DailyForecasts'][4]['AirAndPollen'][5]['Value']
pre_probability_4 = api_data['DailyForecasts'][4]['Day']['PrecipitationProbability']
rain_probability_4 = api_data['DailyForecasts'][4]['Day']['RainProbability']
wind_speed_4 = api_data['DailyForecasts'][4]['Day']['Wind']['Speed']['Value']
wind_direction_4 = api_data['DailyForecasts'][4]['Day']['Wind']['Direction']['Localized']

with open("daily_weather_forecasted_data.csv", "a", newline = '\n') as f:
    writer = csv.writer(f, delimiter = ",")
    writer.writerow([dte_0, dte_sun_rise_0, dte_sun_set_0, hours_of_sun_0, solar_irradiance_0, temp_max_0, weather_status_0, cloud_cover_0,
                     real_feel_temp_0, uv_index_0, pre_probability_0, rain_probability_0,
                     wind_speed_0, wind_direction_0])
    writer.writerow([dte_1, dte_sun_rise_1, dte_sun_set_1, hours_of_sun_1, solar_irradiance_1, temp_max_1, weather_status_1, cloud_cover_1,
                     real_feel_temp_1, uv_index_1, pre_probability_1, rain_probability_1,
                     wind_speed_1, wind_direction_1])
    writer.writerow([dte_2, dte_sun_rise_2, dte_sun_set_2, hours_of_sun_2, solar_irradiance_2, temp_max_2, weather_status_2, cloud_cover_2,
                     real_feel_temp_2, uv_index_2, pre_probability_2, rain_probability_2,
                     wind_speed_2, wind_direction_2])
    writer.writerow([dte_3, dte_sun_rise_3, dte_sun_set_3, hours_of_sun_3, solar_irradiance_3, temp_max_3, weather_status_3, cloud_cover_3,
                     real_feel_temp_3, uv_index_3, pre_probability_3, rain_probability_3,
                     wind_speed_3, wind_direction_3])
    writer.writerow([dte_4, dte_sun_rise_4, dte_sun_set_4, hours_of_sun_4, solar_irradiance_4, temp_max_4, weather_status_4, cloud_cover_4,
                     real_feel_temp_4, uv_index_4, pre_probability_4, rain_probability_4,
                     wind_speed_4, wind_direction_4])
