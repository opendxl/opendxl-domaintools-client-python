Basic Registrant Monitor Example
================================

This sample invokes and displays the results of a DomainTools
"Registrant Monitor" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/registrant-monitor/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the
``sample/basic/basic_registrant_monitor_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_registrant_monitor_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "alerts": [
                    {
                        "created": "2013-08-11",
                        "current_owner": "DOMAIN PRIVACY SERVICE FBO REGISTRANT",
                        "domain": "ourwindingroad.com",
                        "last_owner": "DOMAIN PRIVACY SERVICE FBO REGISTRANT",
                        "match_type": "removed",
                        "modified": "2017-08-12"
                    },
                    {
                        "created": "2017-08-13",
                        "current_owner": "Sherlock Tools",
                        "domain": "tatabrothers.com",
                        "last_owner": "",
                        "match_type": "added",
                        "modified": "2017-08-13"
                    }
                ],
                "date": "2017-08-14",
                "exclude": "not|mydomaintools",
                "limit": 3000,
                "query": "domain|tools",
                "total": 34
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

            # Invoke 'registrant_monitor' method on service
            resp_dict = client.registrant_monitor(["domain", "tools"],
                                                  exclude=["not", "mydomaintools"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.registrant_monitor`
method is invoked with a ``list`` of search terms and a ``list`` of words which
cannot appear in any Whois record returned in the result set. Note that the
``exclude`` argument is optional. If the search only requires one term, each
argument could be specified as a ``str``, for example:

    .. code-block:: python

        # Invoke 'registrant_monitor' method on service
        resp_dict = client.registrant_monitor("domaintools")


The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the registrant monitor query.

From the DomainTools
`Registrant Monitor Documentation <https://www.domaintools.com/resources/api-documentation/registrant-monitor/>`_:

    The Registrant Monitor API searches the ownership (Whois) records of domain
    names for specific search terms. The product is ideal for monitoring
    specific domain owners (such as "DomainTools LLC") to be alerted whenever
    their information appears in a newly-registered domain name.
