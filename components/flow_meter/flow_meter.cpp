#include "flow_meter.h"

namespace flow_meter_i2c {

static const uint8_t I2C_ADDR = 0x10;

uint8_t crc8(const uint8_t *data, uint8_t len) {
  uint8_t crc = 0;
  for (uint8_t i = 0; i < len; i++) {
    crc ^= data[i];
    for (uint8_t j = 0; j < 8; j++)
      crc = (crc & 0x80) ? (crc << 1) ^ 0x07 : (crc << 1);
  }
  return crc;
}

void FlowMeter::setup() {}
void FlowMeter::update() {
  uint8_t buf[3];
  if (this->read_bytes(buf, 3) == 3 && crc8(buf, 2) == buf[2]) {
    uint16_t flow = ((uint16_t)buf[0] << 8) | buf[1];
    flow_sensor_->publish_state(flow);
  }
}

void Calibration::write_state(float value) {
  uint16_t pulses = (uint16_t)value;
  uint8_t buf[3] = { uint8_t(pulses >> 8), uint8_t(pulses & 0xFF), 0 };
  buf[2] = crc8(buf, 2);
  this->write_byte(0x02);
  this->write_bytes(buf, 3);
  number::Number::publish_state(pulses);
}

}  // namespace flow_meter_i2c
