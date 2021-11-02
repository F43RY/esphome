#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace openweathermap {

// static const char *ESPOWM_VERSION = "1.0.0";

// static const uint32_t ESPOWM_POLL_INTERVAL_DEFAULT = 100000;

// static const char SERVERNAME[] = "api.openweathermap.org/data/2.5/weather?";

class OpenWeatherMapClient : public PollingComponent, public text_sensor::TextSensor {
 public:

  void update() override;
  void dump_config() override;

 protected:

};

}  // namespace openweathermap
}  // namespace esphome