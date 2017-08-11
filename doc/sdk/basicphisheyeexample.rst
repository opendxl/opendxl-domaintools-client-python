Basic PhishEye Example
======================

This sample invokes and displays the results of a DomainTools "PhishEye" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/phisheye/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_phisheye_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_phisheye_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "term": "apple",
                "date": "2016-11-01",
                "domains": [
                    {
                        "domain": "firstexample-apple.com",
                        "tld": "com",
                        "created_date": "2016-10-30",
                        "registrant_email": "somebody@example.com",
                        "name_servers": [
                            "ns1.example.com",
                            "ns2.example.com"
                        ],
                        "registrar_name": "Some Registrar 1",
                        "risk_score": 88
                    },
                    {
                        "domain": "appeltypoexample.com",
                        "tld": "com",
                        "created_date": "2016-10-31",
                        "registrant_email": "somebody2@example.com",
                        "ip_addresses": [
                            {
                                "ip": "192.0.2.100",
                                "country_code": "US"
                            },
                            {
                                "ip": "192.0.2.101",
                                "country_code": "US"
                            }
                        ],
                        "name_servers": [
                            "ns57.domaincontrol.com",
                            "ns58.domaincontrol.com"
                        ],
                        "registrar_name": "GoDaddy.com, LLC",
                        "risk_score": 24
                    },
                    {
                        "domain": "thirdexample-apple.ru",
                        "tld": "ru",
                        "created_date": "2014-09-23",
                        "registrant_email": "somebody3@example.com",
                        "registrar_name": "1API GmbH",
                        "risk_score": 33
                    }
                ]
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

            # Invoke 'phisheye' method on service
            resp_dict = client.phisheye("apple")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.phisheye`
method is invoked with a search term.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the PhishEye query.

From the DomainTools
`PhishEye documentation <https://www.domaintools.com/resources/api-documentation/phisheye/>`_:

        The PhishEye API provides programmatic access to daily monitor results
        from the DomainTools PhishEye product. The PhishEye API is only
        available via our Enterprise Solutions team, and is not included in a
        membership.
