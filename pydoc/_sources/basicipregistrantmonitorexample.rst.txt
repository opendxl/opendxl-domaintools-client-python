Basic IP Registrant Monitor Example
===================================

This sample invokes and displays the results of a DomainTools
"IP Registrant Monitor" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/ip-registrant-monitor/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the
``sample/basic/basic_ip_registrant_monitor_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_ip_registrant_monitor_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "record_count": 99,
                "modified": [],
                "page": 1,
                "added": [
                    {
                        "ip_to": "51.255.100.255",
                        "organization": "INTERNAL USAGE",
                        "record_ip": "51.255.100.255",
                        "record_date": "2016-01-05",
                        "range": "51.255.100.224/27",
                        "ip_from": "51.255.100.224",
                        "server": "whois.ripe.net",
                        "country": "FR"
                    },
                    {
                        "ip_to": "51.254.170.239",
                        "organization": "PrivateCloud id -831",
                        "record_ip": "51.254.170.224",
                        "record_date": "2016-01-05",
                        "range": "51.254.170.224/28",
                        "ip_from": "51.254.170.224",
                        "server": "whois.ripe.net",
                        "country": "FR"
                    }
                ],
                "removed": [
                    {
                        "ip_to": "46.105.155.183",
                        "record_ip": "46.105.155.177",
                        "record_date": "2015-03-09",
                        "range": "46.105.155.176/29",
                        "ip_from": "46.105.155.176",
                        "organization": "usertestro",
                        "server": "whois.ripe.net",
                        "country": "FR"
                    },
                    {
                        "ip_to": "37.59.91.175",
                        "record_ip": "37.59.91.163",
                        "record_date": "2015-02-13",
                        "range": "37.59.91.160/28",
                        "ip_from": "37.59.91.160",
                        "organization": "SP&PS",
                        "server": "whois.ripe.net",
                        "country": "FR"
                    }
                ],
                "has_more_pages": false,
                "date": "2016-01-06",
                "query": "ovh"
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

            # Invoke 'ip_registrant_monitor' method on service
            resp_dict = client.ip_registrant_monitor(["domain", "tools"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.ip_registrant_monitor`
method is invoked with a ``list`` of search terms.  If the search only
requires one term, the argument could be specified as a ``str``, for example:

    .. code-block:: python

        resp_dict = client.ip_registrant_monitor("domaintools")


The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the ip registrant monitor query.

From the DomainTools
`IP Registrant Monitor documentation <https://www.domaintools.com/resources/api-documentation/ip-registrant-monitor/>`_:

    The IP Registrant Monitor API searches the ownership (Whois) records of
    domain names for specific search terms. The product is ideal for monitoring
    specific domain owners (such as "DomainTools LLC") to be alerted whenever
    their information appears in a newly-registered domain name. The API will
    also alert you to domains that no longer match a specific term.
