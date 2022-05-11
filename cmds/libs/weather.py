import requests

class Get_Weather():
    def get_weather(self, city):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=8a8c21b4c90d307ed5e89744f49cd759&q='
        #city = input("city name:")
        url = api_address + city
        json_data = requests.get(url).json()
        
        weather_main = json_data['weather'][0]['main']
        weather_description = json_data['weather'][0]['description']
        country = json_data['sys']['country']
        name = json_data['name']
        temp = json_data['main']['feels_like'] - 273.15
        humidity = json_data['main']['humidity']

        back_result = ""
        back_result += "國家縮寫：" + country + '\n'
        back_result += "名稱：" + name + '\n'
        back_result += "體感溫度：" + str(int(temp)) + '度\n'
        back_result += "溼度：" + str(int(humidity)) + '%\n'
        back_result += "天氣：" + weather_main + '\n'
        back_result += "詳述：" + weather_description + '\n'


        return back_result