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

CONF_CITY_ID = "city_id"
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

# OpenWeatherMapClient = owm_ns.class_("openweathermapclient", cg.Component)
OpenWeatherMapClient = owm_ns.class_(
    "OpenWeatherMapClient", cg.PollingComponent, text_sensor.TextSensor
)

CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(OpenWeatherMapClient),
        cv.Required(CONF_API_KEY): cv.string_strict,
        cv.Optional(CONF_LANG, default="en"): cv.one_of(*LANGUAGES, lower=True),
        cv.Optional(CONF_UNITS, default="standard"): cv.one_of(*OWM_UNITS, lower=True)
        # cv.Optional(CONF_CITY_ID): cv.positive_int
    }
).extend(cv.polling_component_schema("60s"))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await text_sensor.register_text_sensor(var, config)
