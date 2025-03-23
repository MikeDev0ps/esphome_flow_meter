import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor, number
from esphome.const import CONF_ID, CONF_UPDATE_INTERVAL

DEPENDENCIES = ['i2c']
AUTO_LOAD = ['flow_meter_i2c']

flow_ns = cg.esphome_ns.namespace('flow_meter_i2c')
FlowMeter = flow_ns.class_('FlowMeter', cg.Component, i2c.I2CDevice)
Calibration = flow_ns.class_('Calibration', cg.Component, number.Number, i2c.I2CDevice)

CONFIG_SCHEMA = sensor.POLLING_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(FlowMeter),
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x10))

NUMBER_PLATFORM_SCHEMA = number.NUMBER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(Calibration),
}).extend(i2c.i2c_device_schema(0x10))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    sens = await sensor.new_sensor(config)
    cg.add(var.set_flow_sensor(sens))

async def to_number_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    cg.add(var.set_min_value(config.get('min_value', 100)))
    cg.add(var.set_max_value(config.get('max_value', 10000)))
    cg.add(var.set_step(config.get('step', 1)))
    return var

BUILD_FLAGS = ['-Iinclude']
