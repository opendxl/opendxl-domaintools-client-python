from __future__ import absolute_import
from __future__ import print_function
import logging
import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxldomaintoolsclient.client import DomainToolsApiClient

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Create the client
with DxlClient(config) as dxl_client:

    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = DomainToolsApiClient(dxl_client)

    # Invoke 'reverse_ip_whois' method on service for a free text query
    resp_dict = client.reverse_ip_whois(query=["google", "search"])

    # Print out the response (convert dictionary to JSON for pretty printing)
    print(("Response for free text query:\n{}".format(
        MessageUtils.dict_to_json(resp_dict, pretty_print=True))))

    # Invoke 'reverse_ip_whois' method on service for an ip query
    resp_dict = client.reverse_ip_whois(ip_address="127.0.0.1")

    # Print out the response (convert dictionary to JSON for pretty printing)
    print(("Response for ip query:\n{}".format(
        MessageUtils.dict_to_json(resp_dict, pretty_print=True))))
