Basic Whois History Example
===========================

This sample invokes and displays the results of a DomainTools "Whois History"
via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/whois-history/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_whois_history_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_whois_history_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "history": [
                    {
                        "date": "2001-10-26",
                        "is_private": 0,
                        "whois": {
                            "name_servers": [
                                "DNS1.INTERLAND.NET"
                            ],
                            "record": "Registrant:\nVRW2\n    7770 Regents Road #113/194\n    San Diego, CA 92122\n",
                            "registrant": "VRW2",
                            "registration": {
                                "created": "1998-08-02",
                                "expires": "2002-08-02",
                                "registrar": "NETWORK SOLUTIONS, INC.",
                                "statuses": [
                                    "ACTIVE"
                                ]
                            }
                        }
                    },
                    {
                        "date": "2003-08-25",
                        "is_private": 0,
                        "whois": {
                            "name_servers": [
                                "NS1.XXXNAMESERVERS.COM"
                            ],
                            "record": "Registrant:\n DomainTools.com\n Taman Harapan 884\n Jakarta, XX 11040\n ID\n",
                            "registrant": "DomainTools.com",
                            "registration": {
                                "created": "1998-08-02",
                                "expires": "2004-08-01",
                                "registrar": "TUCOWS, INC.",
                                "statuses": [
                                    "ACTIVE"
                                ]
                            }
                        }
                    }
                ],
                "record_count": 2
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

            # Invoke 'whois_history' method on service
            resp_dict = client.whois_history("domaintools.com")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.whois_history`
method is invoked with a domain name.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the whois query.

From the DomainTools
`Whois History Documentation <https://www.domaintools.com/resources/api-documentation/whois-history/>`_:

    The Whois History API provides a list of historic Whois records for a domain
    name.
