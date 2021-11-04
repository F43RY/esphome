import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor

# from esphome import automation
# from esphome.automation import maybe_simple_id
# from esphome.components.output import FloatOutput
from esphome.const import (
    CONF_ID,
    CONF_KEY,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_PERCENT,
    CONF_LAMBDA,
    CONF_TEXT_SENSORS,
)

CONF_BY_CITY_NAME = "api_by_city_name"
CONF_BY_CITY_ID = "api_by_city_id"
CONF_BY_GEO_COORDS = "api_by_coords"
CONF_BY_ZIP_CODE = "api_by_zip_code"
CONF_CITY_ID = "city_id"
CONF_CITY_NAME = "city_name"
CONF_STATE_CODE = "state_code"
CONF_COUNTRY_CODE = "country_code"
CONF_GEO_LAT = "latitude"
CONF_GEO_LON = "longitude"
CONF_ZIP_CODE = "zip_code"
CONF_LANG = "language"
CONF_API_KEY = "appid"
CONF_MODE = "mode"
CONF_UNITS = "units"


owm_ns = cg.esphome_ns.namespace("openweathermap")

LANGUAGES = [
    "af",
    "al",
    "ar",
    "az",
    "bg",
    "ca",
    "cz",
    "da",
    "de",
    "el",
    "en",
    "eu",
    "fa",
    "fi",
    "fr",
    "gl",
    "he",
    "hi",
    "hr",
    "hu",
    "id",
    "it",
    "ja",
    "kr",
    "la",
    "lt",
    "mk",
    "no",
    "nl",
    "pl",
    "pt",
    "pt_br",
    "ro",
    "ru",
    "sv",
    "se",
    "sk",
    "sl",
    "sp",
    "es",
    "sr",
    "th",
    "tr",
    "ua",
    "uk",
    "vi",
    "zh_cn",
    "zh_tw",
    "zu",
]

OWM_UNITS = ["standard", "metric", "imperial",]

CurrentWeatherData = owm_ns.class_(
    "CurrentWeatherData", cg.PollingComponent, text_sensor.TextSensor
)

CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(CurrentWeatherData),
        cv.Required(CONF_API_KEY): cv.string_strict,
        cv.Optional(CONF_LANG, default="en"): cv.one_of(*LANGUAGES, lower=True),
        cv.Optional(CONF_UNITS, default="standard"): cv.one_of(*OWM_UNITS, lower=True),
        cv.Optional(CONF_BY_CITY_NAME): text_sensor.TEXT_SENSOR_SCHEMA.extend({
            cv.Required(CONF_CITY_NAME): cv.string_strict,
            cv.Optional(CONF_STATE_CODE): cv.string_strict,        
            cv.Optional(CONF_COUNTRY_CODE): cv.string_strict
        }),
        cv.Optional(CONF_BY_CITY_ID): text_sensor.TEXT_SENSOR_SCHEMA.extend({
            cv.Required(CONF_CITY_ID): cv.positive_int,
        }),
        cv.Optional(CONF_BY_GEO_COORDS): text_sensor.TEXT_SENSOR_SCHEMA.extend({
            cv.Required(CONF_GEO_LAT): cv.float_,
            cv.Required(CONF_GEO_LON): cv.float_
        }),
        cv.Optional(CONF_BY_ZIP_CODE): text_sensor.TEXT_SENSOR_SCHEMA.extend({
            cv.Required(CONF_ZIP_CODE): cv.string_strict,
            cv.Optional(CONF_COUNTRY_CODE): cv.string_strict                    
        }),
    }
).extend(cv.polling_component_schema("10s"))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_app_id(config[CONF_API_KEY]))
    cg.add(var.set_language(config[CONF_LANG]))
    cg.add(var.set_units(config[CONF_UNITS]))
    await cg.register_component(var, config)
    await text_sensor.register_text_sensor(var, config)
