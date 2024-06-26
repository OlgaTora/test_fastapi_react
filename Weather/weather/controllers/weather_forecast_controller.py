from datetime import date
from starlette.responses import RedirectResponse
from fastapi import FastAPI

from Weather.weather.models.weather_forecast import WeatherForecast
from Weather.weather.models.weather_forecast_holder import WeatherForecastHolder

app = FastAPI()
_weather_forecast_holder = WeatherForecastHolder()


@app.get('/')
async def index():
    return RedirectResponse(url='/docs')


@app.get('/get-data/', response_model=list[WeatherForecast])
async def get_data(date_from: date, date_to: date):
    list_measures: list = _weather_forecast_holder.get(date_from, date_to)
    return list_measures


@app.post('/add-data/', response_model=bool)
async def add_data(measure_date: date, temperature_c: float):
    result: bool = _weather_forecast_holder.add(measure_date, temperature_c)
    return result


@app.put('/update-data/', response_model=bool)
async def update_data(measure_date: date, temperature_c: float):
    result: bool = _weather_forecast_holder.update(measure_date, temperature_c)
    return result


@app.delete('/delete-data/', response_model=bool)
async def delete_data(measure_date: date):
    result: bool = _weather_forecast_holder.delete(measure_date)
    return result
