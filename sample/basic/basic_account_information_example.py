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

    # Invoke 'account_information' method on service, in default (dict) output
    # format
    resp_dict = client.account_information()

    # Print out the response
    print("Response in default output format:\n{0}".format(
        MessageUtils.dict_to_json(resp_dict, pretty_print=True)))

    # Invoke 'account_information' method on service, in 'json' output
    resp_json = client.account_information(out_format="json")

    # Print out the response
    print("Response in json output format:\n{0}".format(
        MessageUtils.dict_to_json(MessageUtils.json_to_dict(resp_json),
                                  pretty_print=True)))

    # Invoke 'account_information' method on service, in 'xml' output
    resp_xml = client.account_information(out_format="xml")

    # Print out the response
    print("Response in xml output format:\n{}".format(resp_xml))
