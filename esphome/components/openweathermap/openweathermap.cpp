#include "openweathermap.h"
#include "esphome/core/log.h"

namespace esphome
{
  namespace openweathermap
  {

    static const char *const TAG = "openweathermap";

    void OpenWeatherMapClient::dump_config()
    {
      ESP_LOGCONFIG(TAG, "OpenWeatherMap:");

    }

    // void OpenWeatherMapClient::setup(){
    //   ESP_LOGI(TAG, "setup()");
    // }

  } // namespace openweathermap
} // namespace esphome