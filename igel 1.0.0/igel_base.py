import contextlib
import json
import logging
import random
import requests
import time

VERSION = '1.0.1'

# Mapping between IGEL response fields to Forescout Connect App properties
IGEL_TO_CT_PROPS_MAP = {
    'unitID': 'connect_igel_unit_id',
    'mac': 'connect_igel_mac',
    'firmwareID': 'connect_igel_firmware_id',
    'last_ip': 'connect_igel_last_ip',
    'deviceAttributes': 'connect_igel_device_attributes',
    'id': 'connect_igel_id',
    'name': 'connect_igel_name',
    'parentID': 'connect_igel_parent_id',
    'movedToBin': 'connect_igel_moved_to_bin',
    'objectType': 'connect_igel_object_type',
    'links': 'connect_igel_links'
}


class IgelAsset:
    def __init__(self, asset_dict):
        self.asset_info = asset_dict


class IgelRequest:
    pass
