#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/http_request/http_request.h"

namespace esphome {
namespace openweathermap {

// static const char *ESPOWM_VERSION = "1.0.0";

static const uint32_t ESPOWM_POLL_INTERVAL_DEFAULT = 100000;

// static const char* SERVERNAME = "api.openweathermap.org/data/2.5/weather?";
static const std::string OWM_URL = "localhost?";

class CurrentWeatherData : public PollingComponent, public text_sensor::TextSensor {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;

  void set_app_id(const std::string &appid);
  void set_language(const std::string &lang);
  void set_units(const std::string &units);
  void set_city_name(const std::string &cityname);
  void set_city_id(const std::string &cityid);
  void set_coords(const float &latitude, const float &longitude);
  void set_zip_code(const std::string &zipcode);

 protected:
  std::string appid_;
  std::string lang_;
  std::string units_;
  std::string city_name_ = NULL;
  std::string city_id_ = NULL;
  float latitude_ = 1000;
  float longitude_ = 1000;
  std::string zip_code_ = NULL;

private:
  std::string build_url();
};

class OpenWeathermapResponse : public http_request::HttpRequestResponseTrigger {};

class OpenWeathermapRequestComponent : public http_request::HttpRequestComponent {};

}  // namespace openweathermap
}  // namespace esphome