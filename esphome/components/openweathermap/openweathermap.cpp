#include "openweathermap.h"
#include "esphome/core/log.h"

namespace esphome {
namespace openweathermap {

static const char *const TAG = "openweathermap";

void CurrentWeatherData::dump_config() { ESP_LOGCONFIG(TAG, "OpenWeatherMap:"); }

void CurrentWeatherData::setup(){
  ESP_LOGCONFIG(TAG, "Setting up OpenWeatherMap client...");
}

void CurrentWeatherData::update() { 

  ESP_LOGD(TAG, "API Call to fetch update"); 
  ESP_LOGD(TAG, "Call with following params: %s - lang: %s", this->appid_.c_str(), this->lang_.c_str()); 
}

void CurrentWeatherData::set_app_id(const std::string &appid){ this->appid_ = appid;}
void CurrentWeatherData::set_language(const std::string &lang){this->lang_ = lang;}
void CurrentWeatherData::set_units(const std::string &units){this->units_ = units;}

}  // namespace openweathermap
}  // namespace esphome