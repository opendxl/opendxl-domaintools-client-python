Basic Brand Monitor Example
===========================

This sample invokes and displays the results of a DomainTools "Brand Monitor"
via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/brand-monitor/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_brand_monitor_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_brand_monitor_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "alerts": [],
                "date": "2017-07-17",
                "exclude": [],
                "limit": 3000,
                "new": true,
                "on-hold": true,
                "query": "domaintools",
                "total": 0,
                "utf8": false
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

            # Invoke 'brand monitor' example method on service
            resp_dict = client.brand_monitor("domaintools.com",
                exclude=["auto", "best"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.brand_monitor`
method is invoked with a search term and a ``list`` of domain names to exclude
from the result set.  Note that the ``exclude`` argument is optional.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the brand monitor query.

From the DomainTools
`Brand Monitor documentation <https://www.domaintools.com/resources/api-documentation/brand-monitor/>`_:

        The Brand Monitor API will search across all new domain registrations
        worldwide, and return result sets consisting of domain names that
        contain a customer's brand or monitored word/string. The Brand Monitor
        API looks at country code TLDs and new generic TLDs, as well as the
        usual suspects of .COM, .NET,.ORG, etc.
