Basic Reverse Name Server Example
=================================

This sample invokes and displays the results of a DomainTools "Reverse Name
Server" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/reverse-name-server/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the
``sample/basic/basic_reverse_name_server_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_reverse_name_server_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "name_server": {
                    "hostname": "domaintools.net",
                    "primary": 159,
                    "secondary": 0,
                    "total": 159
                },
                "primary_domains": [
                    "aveneparis.com",
                    "aveneskin.com",
                    "aveneskinshop.com",
                    "avenetherapy.com",
                    "blank-nameserver.com",
                    "bulk-check.com"
                ],
                "secondary_domains": []
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

            # Invoke 'reverse_name_server' method
            resp_dict = client.reverse_name_server("domaintools.net", 35)

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.reverse_name_server`
method is invoked with a domain name and a ``limit`` for the maximum size of the
domain list to be returned. Note that the ``limit`` argument is optional.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the reverse name server query.

From the DomainTools
`Reverse Name Server Documentation <https://www.domaintools.com/resources/api-documentation/reverse-name-server/>`_:

        The Reverse Name Server API provides a list of domain names that share
        the same primary or secondary name server.
