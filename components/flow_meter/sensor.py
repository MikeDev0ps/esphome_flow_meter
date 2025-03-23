from esphome.components import flow_meter_i2c
from esphome.const import CONF_ID

PLATFORM_SCHEMA = flow_meter_i2c.CONFIG_SCHEMA

async def to_code(config):
    await flow_meter_i2c.to_code(config)
