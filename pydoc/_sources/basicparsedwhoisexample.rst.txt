Basic Parsed Whois Example
==========================

This sample invokes and displays the results of a DomainTools "Parsed Whois" via
DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/parsed-whois/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_parsed_whois_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_parsed_whois_example.py

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
                "parsed_whois": {
                    "contacts": {
                        "admin": {
                            "city": "SEATTLE",
                            "country": "US",
                            "email": "MEMBERSERVICES@DOMAINTOOLS.COM",
                            "fax": "12068389056",
                            "name": "DOMAIN ADMINISTRATOR",
                            "org": "DOMAINTOOLS, LLC",
                            "phone": "12068389035",
                            "postal": "98121",
                            "state": "WA",
                            "street": [
                                "2101 4TH AVE",
                                "SUITE 1150"
                            ]
                        },
                        "billing": {
                            "city": "",
                            "country": "",
                            "email": "",
                            "fax": "",
                            "name": "",
                            "org": "",
                            "phone": "",
                            "postal": "",
                            "state": "",
                            "street": []
                        },
                        "registrant": {
                            "city": "SEATTLE",
                            "country": "US",
                            "email": "MEMBERSERVICES@DOMAINTOOLS.COM",
                            "fax": "12068389056",
                            "name": "DOMAIN ADMINISTRATOR",
                            "org": "DOMAINTOOLS, LLC",
                            "phone": "12068389035",
                            "postal": "98121",
                            "state": "WA",
                            "street": [
                                "2101 4TH AVE",
                                "SUITE 1150"
                            ]
                        },
                        "tech": {
                            "city": "SEATTLE",
                            "country": "US",
                            "email": "MEMBERSERVICES@DOMAINTOOLS.COM",
                            "fax": "12068389056",
                            "name": "DOMAIN ADMINISTRATOR",
                            "org": "DOMAINTOOLS, LLC",
                            "phone": "12068389035",
                            "postal": "98121",
                            "state": "WA",
                            "street": [
                                "2101 4TH AVE",
                                "SUITE 1150"
                            ]
                        }
                    },
                    "created_date": "1998-08-02T04:00:00+00:00",
                    "domain": "domaintools.com",
                    "expired_date": "2018-08-01T04:00:00+00:00",
                    "name_servers": [
                        "ns1.p09.dynect.net",
                        "ns2.p09.dynect.net",
                        "ns3.p09.dynect.net",
                        "ns4.p09.dynect.net"
                    ],
                    "other_properties": {
                        "dnssec": "unSigned",
                        "registry_domain_id": "1697312_DOMAIN_COM-VRSN"
                    },
                    "registrar": {
                        "abuse_contact_email": "abuse@enom.com",
                        "abuse_contact_phone": "14252982646",
                        "iana_id": "48",
                        "name": "ENOM, INC.",
                        "url": "www.enom.com",
                        "whois_server": "whois.enom.com"
                    },
                    "statuses": [
                        "clientTransferProhibited https://www.icann.org/epp#clientTransferProhibited"
                    ],
                    "updated_date": "2017-07-03T00:43:03+00:00"
                },
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
                    "record": "Domain Name: DOMAINTOOLS.COM\nRegistry Domain ID: 1697312_DOMAIN_COM-VRSN\nRegistrar WHOIS Server:
                    whois.enom.com\nRegistrar URL: www.enom.com\nUpdated Date: 2017-07-03T00:43:03.00Z\nCreation
                    Date: 1998-08-02T04:00:00.00Z\nRegistrar Registration Expiration Date: 2018-08-01T04:00:00.00Z\nRegistrar:
                    ..."
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

            # Invoke 'parsed_whois' method on service
            resp_dict = client.parsed_whois("domaintools.com")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.parsed_whois`
method is invoked with a hostname.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the parsed whois query.

From the DomainTools
`Parsed Whois documentation <https://www.domaintools.com/resources/api-documentation/parsed-whois/>`_:

        `"The Parsed Whois API provides parsed information extracted from the raw
        Whois record. The API is optimized to quickly retrieve the Whois record,
        group important data together and return a well-structured format. The
        Parsed Whois API is ideal for anyone wishing to search for, index, or
        cross-reference data from one or multiple Whois records."`
