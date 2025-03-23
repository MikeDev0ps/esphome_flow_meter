import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c
from esphome.const import CONF_ID

DEPENDENCIES = ['i2c']
AUTO_LOAD = ['flow_meter_i2c']

flow_ns = cg.esphome_ns.namespace('flow_meter_i2c')
FlowMeter = flow_ns.class_('FlowMeter', cg.Component, i2c.I2CDevice)

PLATFORM_SCHEMA = sensor.POLLING_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(FlowMeter),
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x10))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    sens = await sensor.new_sensor(config)
    cg.add(var.set_flow_sensor(sens))
