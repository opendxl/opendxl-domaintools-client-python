Basic Reverse IP Whois Example
==============================

This sample invokes and displays the results of a DomainTools "Reverse IP Whois"
via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/reverse-ip-whois/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the
``sample/basic/basic_reverse_ip_whois_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_reverse_ip_whois_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "has_more_pages": true,
                "page": 1,
                "total_count": 1105,
                "record_count": 1000,
                "records": [
                    {
                        "ip_from": "1.179.248.0",
                        "ip_to": "1.179.255.255",
                        "record_ip": "1.179.249.17",
                        "record_date": "2015-05-15",
                        "server": "whois.apnic.net",
                        "organization": "Static IP address for Google-caching servers",
                        "country": "TH",
                        "range": "1.179.248.0/21"
                    },
                    {
                        "ip_from": "4.3.2.0",
                        "ip_to": "4.3.2.255",
                        "record_ip": "4.3.2.1",
                        "record_date": "2015-05-17",
                        "server": "whois.arin.net",
                        "organization": "Google Inc.",
                        "country": "US",
                        "range": "4.3.2.0/24"
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

            # Invoke 'reverse_ip_whois' method on service for a free text query
            resp_dict = client.reverse_ip_whois(query=["google", "search"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response for free text query:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))

            # Invoke 'reverse_ip_whois' method on service for an ip query
            resp_dict = client.reverse_ip_whois(ip="127.0.0.1")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response for ip query:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.reverse_ip_whois`
method is invoked in two different ways:

* With a ``list`` of free text query terms. If the search only requires one term, the argument could be specified as a ``str``.
* With an ``ip`` address.

Either the free text query terms or an ip address, but not both, must be
specified.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the reverse ip whois query.

From the DomainTools
`Reverse IP Whois Documentation <https://www.domaintools.com/resources/api-documentation/reverse-ip-whois/>`_:

        The Reverse IP Whois API provides a list of IP ranges that are owned by
        an Organization. You can enter an organization’s name and receive a list
        of all of the organization’s currently owned IP ranges.
