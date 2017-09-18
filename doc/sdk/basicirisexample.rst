Basic Iris Example
========================

This sample invokes and displays the results of a DomainTools "Iris" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/iris/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_iris_example.py`` script as
follows:

    .. parsed-literal::

        python sample/basic/basic_iris_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "limit_exceeded": false,
                "message": "Enjoy your data.",
                "results_count": 1,
                "results": [
                    {
                        "domain": "domaintools.com",
                        "whois_url": "https://whois.domaintools.helium/domaintools.com",
                        "adsense": "",
                        "alexa": 2346,
                        "google_analytics": 76641,
                        "admin_contact": {
                            "name": "DOMAIN ADMINISTRATOR",
                            "org": "DOMAINTOOLS, LLC",
                            "street": "2101 4TH AVE,SUITE 1150",
                            "city": "SEATTLE",
                            "state": "WA",
                            "postal": "98121",
                            "country": "us",
                            "phone": "12068389035",
                            "fax": "12068389056",
                            "email": [
                               "memberservices@domaintools.com"
                            ]
                        },
                        "billing_contact": {
                            "name": "",
                            "org": "",
                            "street": "",
                            "city": "",
                            "state": "",
                            "postal": "",
                            "country": "",
                            "phone": "",
                            "fax": "",
                            "email": []
                        },
                        "registrant_contact": {
                            "name": "DOMAIN ADMINISTRATOR",
                            "org": "DOMAINTOOLS, LLC",
                            "street": "2101 4TH AVE,SUITE 1150",
                            "city": "SEATTLE",
                            "state": "WA",
                            "postal": "98121",
                            "country": "us",
                            "phone": "12068389035",
                            "fax": "12068389056",
                            "email": [
                                "memberservices@domaintools.com"
                            ]
                        },
                        "technical_contact": {
                            "name": "DOMAIN ADMINISTRATOR",
                            "org": "DOMAINTOOLS, LLC",
                            "street": "2101 4TH AVE,SUITE 1150",
                            "city": "SEATTLE",
                            "state": "WA",
                            "postal": "98121",
                            "country": "us",
                            "phone": "12068389035",
                            "fax": "12068389056",
                            "email": [
                                "memberservices@domaintools.com"
                            ]
                        },
                        "create_date": "1998-08-02",
                        "expiration_date": "2017-08-01",
                        "email_domain": [
                            "domaintools.com",
                            "enom.com"
                        ],
                        "soa_email": [
                            "postmaster@domaintools.com"
                        ],
                        "ssl_email": [],
                        "additional_whois_email": [
                            "abuse@enom.com"
                        ],
                        "ip": [
                            {
                                "address": "199.30.228.112",
                                "asn": [
                                    17318
                                ],
                                "country_code": "us",
                                "isp": "Domaintools LLC"
                            }
                        ],
                        "mx": [
                            {
                                "host": "aspmx3.googlemail.com",
                                "domain": "googlemail.com",
                                "ip": [
                                    "64.233.185.26"
                                ],
                                "priority": 10
                            },
                            {
                                "host": "aspmx4.googlemail.com",
                                "domain": "googlemail.com",
                                "ip": [
                                    "173.194.205.27"
                                ],
                                "priority": 10
                            }
                        ],
                        "name_server": [
                            {
                                "host": "ns1.p09.dynect.net",
                                "domain": "dynect.net",
                                "ip": [
                                    "208.78.70.9"
                                ]
                            },
                                {
                                "host": "ns4.p09.dynect.net",
                                "domain": "dynect.net",
                                "ip": [
                                    "204.13.251.9"
                                ]
                            }
                        ],
                        "redirect": "",
                        "redirect_domain": "",
                        "registrant_name": "DOMAIN ADMINISTRATOR",
                        "registrant_org": "DOMAINTOOLS, LLC",
                        "registrar": "ENOM, INC",
                        "registrar_status": [
                            "clientTransferProhibited"
                        ],
                        "risk_score": 0,
                        "spf_info": "v=spf1 ip4:199.30.228.70 mx a:relay.nameintel.com include:mail.zendesk.com include:_spf.google.com include:mktomail.com ~all",
                        "ssl_country": "",
                        "ssl_hash": "",
                        "ssl_org": "",
                        "tld": "com",
                        "website_response": 200
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

            # Invoke 'iris' method on service for a domain query
            resp_dict = client.iris(domain=["domaintools.com", "domaintools.net"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response for domain query:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))

            # Invoke 'iris' method on service for a query by registrant and nameserver
            resp_dict = client.iris(registrant="fred", nameserver="domainparkingserver.net")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response for query by registrant and nameserver:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.iris`
method is invoked in two different ways:

* With a ``list`` of domains.  If the search only requires one term, the argument could be specified as a ``str``.
* With a ``registrant`` and a ``nameserver``.

At least one search term -- ``domain``, ``ip``, ``email``, ``nameserver``,
``registrar``, ``registrant``, and/or ``registrant_org`` -- must be specified.
Arguments are combined into a logical AND query where each domain returned
matches all of the supplied argument values.

The final step is to display the contents of the returned dictionaries (``dict``)
which contains the results of the iris queries.

From the DomainTools
`Iris documentation <https://www.domaintools.com/resources/api-documentation/iris/>`_:

    `"The Iris Pivot API enables bulk enrichment of a list of domains with parsed
    domain and infrastructure profiles sourced from the Iris database. It also
    provides a multivariate search across several of the most commonly-used Iris
    data fields. Queries to the Iris Pivot API deduct from the same Iris query
    allocation assigned to a user's Enterprise Membership for qualified Iris
    customers."`
