from datetime import date

from Seminar_9.weather.models.weather_forecast import WeatherForecast


class WeatherForecastHolder:
    """Объект на базе класса WeatherForecastHolder будет хранить список показателей по температуре"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._measures: list[WeatherForecast] = []

    def add(self, measure_date: date, temperature_c: float):
        """Добавить новый показатель по температуре"""
        new_measure = WeatherForecast(date_measure=measure_date, temperature_c=temperature_c)
        self._measures.append(new_measure)
        return True

    def update(self, measure_date: date, temperature_c: float):
        """Обновить показатель по температуре"""
        for measure in self._measures:
            if measure.date_measure == measure_date:
                measure.temperature_c = temperature_c
                return True
        return False

    def get(self, date_from: date, date_to: date):
        """Получить показатели по температуре за период"""
        result: list[WeatherForecast] = []
        for measure in self._measures:
            if date_from <= measure.date_measure <= date_to:
                result.append(measure)
        return result

    def delete(self, measure_date: date):
        """Удалить показатель по температуре"""
        for measure in self._measures:
            if measure.date_measure == measure_date:
                self._measures.remove(measure)
                return True
        return False
