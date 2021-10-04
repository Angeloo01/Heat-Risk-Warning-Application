import math
import requests
from bs4 import BeautifulSoup

heat_index_potential = {}
heat_index_potential[(40, 80)] = 80
heat_index_potential[(40, 82)] = 81
heat_index_potential[(40, 84)] = 83
heat_index_potential[(40, 86)] = 85
heat_index_potential[(40, 88)] = 88
heat_index_potential[(40, 90)] = 91
heat_index_potential[(40, 92)] = 94
heat_index_potential[(40, 94)] = 97
heat_index_potential[(40, 96)] = 101
heat_index_potential[(40, 98)] = 105
heat_index_potential[(40, 100)] = 109
heat_index_potential[(40, 102)] = 114
heat_index_potential[(40, 104)] = 119
heat_index_potential[(40, 106)] = 124
heat_index_potential[(40, 108)] = 130
heat_index_potential[(40, 110)] = 136

heat_index_potential[(45, 80)] = 80
heat_index_potential[(45, 82)] = 82
heat_index_potential[(45, 84)] = 84
heat_index_potential[(45, 86)] = 87
heat_index_potential[(45, 88)] = 89
heat_index_potential[(45, 90)] = 93
heat_index_potential[(45, 92)] = 96
heat_index_potential[(45, 94)] = 100
heat_index_potential[(45, 96)] = 104
heat_index_potential[(45, 98)] = 109
heat_index_potential[(45, 100)] = 114
heat_index_potential[(45, 102)] = 119
heat_index_potential[(45, 104)] = 124
heat_index_potential[(45, 106)] = 130
heat_index_potential[(45, 108)] = 137

heat_index_potential[(50, 80)] = 81
heat_index_potential[(50, 82)] = 83
heat_index_potential[(50, 84)] = 85
heat_index_potential[(50, 86)] = 88
heat_index_potential[(50, 88)] = 91
heat_index_potential[(50, 90)] = 95
heat_index_potential[(50, 92)] = 99
heat_index_potential[(50, 94)] = 103
heat_index_potential[(50, 96)] = 106
heat_index_potential[(50, 98)] = 113
heat_index_potential[(50, 100)] = 118
heat_index_potential[(50, 102)] = 124
heat_index_potential[(50, 104)] = 131
heat_index_potential[(50, 106)] = 137

heat_index_potential[(55, 80)] = 81
heat_index_potential[(55, 82)] = 84
heat_index_potential[(55, 84)] = 86
heat_index_potential[(55, 86)] = 89
heat_index_potential[(55, 88)] = 93
heat_index_potential[(55, 90)] = 97
heat_index_potential[(55, 92)] = 101
heat_index_potential[(55, 94)] = 106
heat_index_potential[(55, 96)] = 112
heat_index_potential[(55, 98)] = 117
heat_index_potential[(55, 100)] = 124
heat_index_potential[(55, 102)] = 130
heat_index_potential[(55, 104)] = 137

heat_index_potential[(60, 80)] = 82
heat_index_potential[(60, 82)] = 84
heat_index_potential[(60, 84)] = 88
heat_index_potential[(60, 86)] = 91
heat_index_potential[(60, 88)] = 95
heat_index_potential[(60, 90)] = 100
heat_index_potential[(60, 92)] = 105
heat_index_potential[(60, 94)] = 110
heat_index_potential[(60, 96)] = 116
heat_index_potential[(60, 98)] = 123
heat_index_potential[(60, 100)] = 129
heat_index_potential[(60, 102)] = 137

heat_index_potential[(65, 80)] = 82
heat_index_potential[(65, 82)] = 85
heat_index_potential[(65, 84)] = 89
heat_index_potential[(65, 86)] = 93
heat_index_potential[(65, 88)] = 98
heat_index_potential[(65, 90)] = 103
heat_index_potential[(65, 92)] = 108
heat_index_potential[(65, 94)] = 114
heat_index_potential[(65, 96)] = 121
heat_index_potential[(65, 98)] = 128
heat_index_potential[(65, 100)] = 136

heat_index_potential[(70, 80)] = 83
heat_index_potential[(70, 82)] = 84
heat_index_potential[(70, 84)] = 90
heat_index_potential[(70, 86)] = 95
heat_index_potential[(70, 88)] = 100
heat_index_potential[(70, 90)] = 105
heat_index_potential[(70, 92)] = 112
heat_index_potential[(70, 94)] = 119
heat_index_potential[(70, 96)] = 126
heat_index_potential[(70, 98)] = 134

heat_index_potential[(75, 80)] = 84
heat_index_potential[(75, 82)] = 88
heat_index_potential[(75, 84)] = 92
heat_index_potential[(75, 86)] = 97
heat_index_potential[(75, 88)] = 103
heat_index_potential[(75, 90)] = 109
heat_index_potential[(75, 92)] = 116
heat_index_potential[(75, 94)] = 124
heat_index_potential[(75, 96)] = 132

heat_index_potential[(80, 80)] = 84
heat_index_potential[(80, 82)] = 89
heat_index_potential[(80, 84)] = 94
heat_index_potential[(80, 86)] = 100
heat_index_potential[(80, 88)] = 106
heat_index_potential[(80, 90)] = 113
heat_index_potential[(80, 92)] = 121
heat_index_potential[(80, 94)] = 129

heat_index_potential[(85, 80)] = 85
heat_index_potential[(85, 82)] = 90
heat_index_potential[(85, 84)] = 96
heat_index_potential[(85, 86)] = 102
heat_index_potential[(85, 88)] = 110
heat_index_potential[(85, 90)] = 117
heat_index_potential[(85, 92)] = 126
heat_index_potential[(85, 94)] = 135

heat_index_potential[(90, 80)] = 86
heat_index_potential[(90, 82)] = 91
heat_index_potential[(90, 84)] = 98
heat_index_potential[(90, 86)] = 105
heat_index_potential[(90, 88)] = 113
heat_index_potential[(90, 90)] = 122
heat_index_potential[(90, 92)] = 131

heat_index_potential[(95, 80)] = 86
heat_index_potential[(95, 82)] = 93
heat_index_potential[(95, 84)] = 100
heat_index_potential[(95, 86)] = 108
heat_index_potential[(95, 88)] = 117
heat_index_potential[(95, 90)] = 127

heat_index_potential[(100, 80)] = 87
heat_index_potential[(100, 82)] = 95
heat_index_potential[(100, 84)] = 103
heat_index_potential[(100, 86)] = 112
heat_index_potential[(100, 88)] = 121
heat_index_potential[(100, 90)] = 132


def get_risk(temp, humidity):
    remnder = temp % 2
    if remnder > 1:
        temp = round(round(temp) / 2) * 2 + 2
    else:
        temp = round(round(temp) / 2) * 2
    remainder = humidity % 5
    if remainder > 2.5:
        humidity = round(humidity / 5) * 5 + 5
    else:
        humidity = round(humidity / 5) * 5
    return heat_index_potential[(humidity, temp)]


def range_checker(temp, humidity):
    print(type(humidity))
    print(type(temp))
    if humidity < 40:
        return -1
    if temp < 80:
        return -1
    if temp > 110:
        return -2
    return 0


def riskLevel(risk):
    if (risk == -1):
        return "Based on the Calculated Risk Index, there is no need to be cautious, the risk associated with heat is low right now."
    if (risk == -2):
        return "Based on the Calculated Risk Index, There is extreme danger associated in spending time outdoors and a high risk of heatstroke, please stay in a well-cooled indoor facility and drink lots of water!"
    if (risk >= 80 and risk <= 90):
        return "Based on the Calculated Risk Index, there is a possibility of fatigue with prolonged heat exposure, take caution when going outside."
    if (risk > 90 and risk <= 103):
        return "Based on the Calculated Risk Index, there is a possibility of heat related illnesses with prolonged heat exposure, go outside only if necessary."
    if (risk > 103 and risk <= 124):
        return "Based on the Calculated Risk Index, there is a likely chance of heatstroke and heat-related illnesses with exposure, do not go outside."
    if (risk > 124):
        return "Based on the Calculated Risk Index, There is extreme danger associated in spending time outdoors and a high risk of heatstroke, please stay in a well-cooled indoor facility and drink lots of water!"


print(get_risk(80.3, 86))


class Weather:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    humidity = ""
    temperature = ""

    @staticmethod
    def set_city(city):
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=Weather.headers)
        print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        Weather.temperature = soup.select('#wob_tm')[0].getText().strip()
        Weather.humidity = soup.select('#wob_hm')[0].getText().strip()
