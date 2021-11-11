#include "openweathermap.h"
#include "esphome/core/log.h"

namespace esphome {
namespace openweathermap {

static const char *const TAG = "openweathermap";

void CurrentWeatherData::dump_config() { ESP_LOGCONFIG(TAG, "OpenWeatherMap:"); }

void CurrentWeatherData::setup() {
  ESP_LOGCONFIG(TAG, "Setting up OpenWeatherMap client...");
  OpenWeathermapRequestComponent request;

  request.set_url(this->build_url());
  request.set_method("GET");
}

std::string CurrentWeatherData::build_url() { 
  std::string url = OWM_URL + "appid=" + this->appid_ + "&units=" + this->units_ + "&lang=" + this->lang_; 
  if (this->city_name_.length() > 0){
    url += "&q=" + city_name_;
  }else if(this->city_id_.length() > 0){
    url += "&id=" + city_id_;
  }else if(this->latitude_ != 1000 && this->longitude_ != 1000){
    url += "&lat=" + std::to_string(latitude_) + "&lon=" + std::to_string(longitude_);
  }else if(this->city_name_.length() > 0){
    url += "&zip=" + zip_code_;
  }
  return url;
}

void CurrentWeatherData::update() {
  ESP_LOGD(TAG, "API Call to fetch update");
  ESP_LOGD(TAG, "Call with following params: %s - lang: %s", this->appid_.c_str(), this->lang_.c_str());
}

void CurrentWeatherData::set_app_id(const std::string &appid) { this->appid_ = appid; }
void CurrentWeatherData::set_language(const std::string &lang) { this->lang_ = lang; }
void CurrentWeatherData::set_units(const std::string &units) { this->units_ = units; }

void CurrentWeatherData::set_city_name(const std::string &city_name) {this->city_name_ = city_name;}
void CurrentWeatherData::set_city_id(const std::string &city_id) {this->city_id_ = city_id;}
void CurrentWeatherData::set_coords(const float &latitude, const float &longitude) {this->latitude_ = latitude; this->longitude_ = longitude;}
void CurrentWeatherData::set_zip_code(const std::string &zip_code) {this->zip_code_ = zip_code;}

}  // namespace openweathermap
}  // namespace esphome