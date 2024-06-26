from pydantic import BaseModel, computed_field
from datetime import date


class WeatherForecast(BaseModel):
    """Прогноз погоды"""
    date_measure: date
    temperature_c: float  # Температура в градус Цельсия

    @computed_field
    @property
    def temperature_f(self) -> int:  # Температура в градус Форенгейта
        return 32 + int(self.temperature_c / 0.5556)
