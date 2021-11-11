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

#CONF_BY_CITY_NAME = "api_by_city_name"
#CONF_BY_CITY_ID = "api_by_city_id"
CONF_BY_GEO_COORDS = "coords"
#CONF_BY_ZIP_CODE = "api_by_zip_code"
CONF_CITY_ID = "city_id"
CONF_CITY_NAME = "city_name"
#CONF_STATE_CODE = "state_code"
#CONF_COUNTRY_CODE = "country_code"
CONF_GEO_LAT = "latitude"
CONF_GEO_LON = "longitude"
CONF_ZIP_CODE = "zip_code"
CONF_LANG = "language"
CONF_API_KEY = "appid"
CONF_MODE = "mode"
CONF_UNITS = "units"

#DEPENDENCIES = ["http_request"]
AUTO_LOAD = ["json"]

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
'''
CONFIG_SCHEMA_CITY_NAME = cv.Schema({
            cv.Required(CONF_CITY_NAME): cv.string_strict,
})

CONFIG_SCHEMA_CITY_ID = cv.Schema({
            cv.Required(CONF_CITY_ID): cv.string_strict,
})
'''


CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(CurrentWeatherData),
        cv.Required(CONF_API_KEY): cv.All(cv.string_strict, cv.Length(min=32, max=32)),
        cv.Optional(CONF_LANG, default="en"): cv.All(cv.one_of(*LANGUAGES), lower=True),
        cv.Optional(CONF_UNITS, default="standard"): cv.All(cv.one_of(*OWM_UNITS), lower=True),
        cv.Optional(CONF_CITY_NAME): cv.string, #text_sensor.TEXT_SENSOR_SCHEMA.extend({
        cv.Optional(CONF_CITY_ID): cv.positive_int,
        cv.Optional(CONF_BY_GEO_COORDS): cv.Schema({
            cv.Required(CONF_GEO_LAT): cv.float_range,
            cv.Required(CONF_GEO_LON): cv.float_range
        }),
        cv.Optional(CONF_ZIP_CODE): cv.string_strict
    }
).extend(cv.polling_component_schema("10s"))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_app_id(config[CONF_API_KEY]))
    cg.add(var.set_language(config[CONF_LANG]))
    cg.add(var.set_units(config[CONF_UNITS]))
    if CONF_CITY_NAME in config:
        cg.add(var.set_city_name(config[CONF_CITY_NAME]))
    elif CONF_CITY_ID in config:
        cg.add(var.set_city_id(config[CONF_CITY_ID]))
    elif CONF_BY_GEO_COORDS in config:
        cg.add(var.set_coords(config[CONF_GEO_LAT], config[CONF_GEO_LON]))
    elif CONF_ZIP_CODE in config:
        cg.add(var.set_zip_code(config[CONF_ZIP_CODE]))
    await cg.register_component(var, config)
    await text_sensor.register_text_sensor(var, config)
