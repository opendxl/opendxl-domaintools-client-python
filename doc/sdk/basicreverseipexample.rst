Basic Reverse IP Example
========================

This sample invokes and displays the results of a DomainTools "Reverse IP" via
DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/reverse-ip/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_reverse_ip_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_reverse_ip_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "ip_addresses": {
                    "domain_count": 3,
                    "domain_names": [
                        "DOMAINTOOLS.COM",
                        "WHOISAPI.COM",
                        "WHOISSUGGEST.COM"
                    ],
                    "ip_address": "199.30.228.112"
                }
            }
        }

The received results are displayed.

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = DomainToolsApiClient(dxl_client)

            # Invoke 'reverse_ip' method on service
            resp_dict = client.reverse_ip("domaintools.com")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.reverse_ip`
method is invoked with a domain name.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the reverse IP query.

From the DomainTools
`Reverse IP Documentation <https://www.domaintools.com/resources/api-documentation/reverse-ip/>`_:

        `"The Reverse IP API provides a list of domain names that share the same
        Internet host (i.e. the same IP address). You can request an IP address
        directly, or you can provide a domain name; if you provide a domain
        name, the API will respond with the list of other domains that share the
        same IP."`