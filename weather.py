import requests
api_key = '4fdc0b27204fdd921469e360ca6ede8c'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
city = input('Enter city: ')
url = f'{base_url}q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()
if response.status_code == 200:
    main_data = ['main']
    weather_data = data['weather'][0]

    temp = main_data['temp']
    desc = main_data['descriprion']

    print(f'The temp is {temp} {desc}')
else:
    print(f'Error:{data['message']}')



