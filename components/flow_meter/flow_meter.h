#pragma once
#include "esphome.h"

namespace flow_meter_i2c {

class FlowMeter : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void update() override;
  void set_flow_sensor(sensor::Sensor *sensor) { flow_sensor_ = sensor; }

 protected:
  sensor::Sensor *flow_sensor_{nullptr};
};

class Calibration : public Component, public number::Number, public i2c::I2CDevice {
 public:
  void write_state(float value) override;
};

}  // namespace flow_meter_i2c
