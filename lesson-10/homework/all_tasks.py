#Task 1

import requests

API_KEY = '5796abbde9106b7da4febfae8c44c232s'
CITY_ID = '1215957'
url = f'https://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric&lang=ru'

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if data.get('cod') != 200:
        print(f"Ошибка от API: {data.get('message', 'Неизвестная ошибка')}")
    else:
        city = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']

        print(f"Погода в городе {city}:")
        print(f"🌡️ Температура: {temperature}°C (ощущается как {feels_like}°C)")
        print(f"💧 Влажность: {humidity}%")
        print(f"🔽 Давление: {pressure} гПа")
        print(f"💨 Ветер: {wind_speed} м/с")
        print(f"☀️ Состояние: {weather_description}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP ошибка: {e}")
except requests.exceptions.ConnectionError:
    print("Ошибка подключения. Проверьте интернет.")
except requests.exceptions.Timeout:
    print("Время ожидания истекло.")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")

## Task 2
import requests

BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMzhlMTJmODg2NDcxNjU2N2RlN2Q0NjMyY2ZmMGM4NyIsIm5iZiI6MTc1MTEyMDgxOS4yNjIsInN1YiI6IjY4NWZmYmIzZDdiNDU4MTcyYTdlZDI2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WECKePWuC_xonZNvc-FcDnlVeCx5HL-UttCysK4AHt8"

genres = {
    "action": 28,
    "adventure": 12,
    "animation": 16,
    "comedy": 35,
    "crime": 80,
    "documentary": 99,
    "drama": 18,
    "family": 10751,
    "fantasy": 14,
    "history": 36,
    "horror": 27,
    "music": 10402,
    "mystery": 9648,
    "romance": 10749,
    "science fiction": 878,
    "tv movie": 10770,
    "thriller": 53,
    "war": 10752,
    "western": 37
}

genre_input = input("Введите жанр фильма (на английском, например: comedy, drama, horror): ").strip().lower()

genre_id = genres.get(genre_input)

if not genre_id:
    print("❌ Жанр не найден. Попробуйте ввести один из следующих:")
    for name in genres:
        print("-", name.title())
else:
    url = (
        f"https://api.themoviedb.org/3/discover/movie"
        f"?language=ru&sort_by=popularity.desc&with_genres={genre_id}&include_adult=false&page=1"
    )

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        if 'results' not in data or not data['results']:
            print("❗ Не найдено фильмов по указанному жанру.")
        else:
            print(f"✅ Найдено фильмов: {len(data['results'])}\n")

            for i, movie in enumerate(data['results'][:3], start=1):
                title = movie.get('title', 'Без названия')
                release_date = movie.get('release_date', 'Неизвестно')
                rating = movie.get('vote_average', 'Нет рейтинга')
                overview = movie.get('overview', 'Описание отсутствует')

                print(f"{i}. 🎬 {title} ({release_date}) — ⭐ {rating}")
                print(f"   📝 {overview}\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP ошибка: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Ошибка соединения. Проверь подключение к интернету.")
    except requests.exceptions.Timeout:
        print("⏳ Время ожидания истекло.")
    except requests.exceptions.RequestException as err:
        print(f"❌ Ошибка запроса: {err}")
    except ValueError:
        print("❌ Ошибка разбора JSON.")
    except Exception as e:
        print(f"❌ Неизвестная ошибка: {e}")
