import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import number, i2c
from esphome.const import CONF_ID

flow_ns = cg.esphome_ns.namespace('flow_meter_i2c')
Calibration = flow_ns.class_('Calibration', cg.Component, number.Number, i2c.I2CDevice)

NUMBER_PLATFORM_SCHEMA = number.NUMBER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(Calibration),
}).extend(i2c.i2c_device_schema(0x10))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    cg.add(var.set_min_value(config.get('min_value', 100)))
    cg.add(var.set_max_value(config.get('max_value', 10000)))
    cg.add(var.set_step(config.get('step', 1)))
    return var
