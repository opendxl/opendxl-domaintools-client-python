Basic Whois Lookup Example
==========================

This sample invokes and displays the results of a DomainTools "Whois Lookup" via
DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/whois-lookup/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_whois_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_whois_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "name_servers": [
                    "NS1.P09.DYNECT.NET",
                    "NS2.P09.DYNECT.NET",
                    "NS3.P09.DYNECT.NET",
                    "NS4.P09.DYNECT.NET"
                ],
                "record_source": "domaintools.com",
                "registrant": "DOMAINTOOLS, LLC",
                "registration": {
                    "created": "1998-08-02",
                    "expires": "2018-08-01",
                    "registrar": "ENOM, INC.",
                    "statuses": [
                        "clientTransferProhibited"
                    ],
                    "updated": "2017-07-03"
                },
                "whois": {
                    "date": "2017-07-17",
                    "record": "Domain Name: DOMAINTOOLS.COM\nRegistry Domain ID: 1697312_DOMAIN_COM-VRSN\nRegistrar"
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

            # Invoke 'whois' method on service
            resp_dict = client.whois("domaintools.com")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.whois`
method is invoked with a domain name.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the whois query.

From the DomainTools
 `Whois Lookup Documentation <https://www.domaintools.com/resources/api-documentation/whois-lookup/>`_:

    The Whois Lookup API provides the ownership record for a domain name or IP
    address with basic registration details.
