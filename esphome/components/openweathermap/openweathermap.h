#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace openweathermap {

// static const char *ESPOWM_VERSION = "1.0.0";

// static const uint32_t ESPOWM_POLL_INTERVAL_DEFAULT = 100000;

// static const char SERVERNAME[] = "api.openweathermap.org/data/2.5/weather?";

class CurrentWeatherData : public PollingComponent, public text_sensor::TextSensor {
 public:

  void setup() override;
  void update() override;
  void dump_config() override;
  void set_app_id(const std::string &appid);
  void set_language(const std::string &lang);
  void set_units(const std::string &units);

 protected:
 std::string appid_;
 std::string lang_;
 std::string units_;
};

}  // namespace openweathermap
}  // namespace esphome