from __future__ import annotations
from typing import Any, Dict, Optional
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class OccupancySensorAttributes(Attributes):
    is_detected: Optional[bool] = False


class OccupancySensor(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: OccupancySensorAttributes

    def reload(self) -> OccupancySensor:
        data = self.dirigera_client.get(route=f"/devices/{self.id}")
        return OccupancySensor(dirigeraClient=self.dirigera_client, **data)

    def set_name(self, name: str) -> None:
        raise AssertionError("Not implemented")


def dict_to_occupancy_sensor(
    data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub
) -> OccupancySensor:
    return OccupancySensor(dirigeraClient=dirigera_client, **data)
