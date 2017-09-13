Basic IP Monitor Example
========================

This sample invokes and displays the results of a DomainTools "IP Monitor" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/ip-monitor/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_ip_monitor_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_ip_monitor_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "alerts": [],
                "date": "2017-07-18",
                "ip_address": "75.55.53.233",
                "limit": 1000,
                "page": 1,
                "page_count": 0,
                "total": "0"
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

            # Invoke 'ip_monitor' method on service
            resp_dict = client.ip_monitor("77.55.53.233")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.ip_monitor`
method is invoked with an IP address.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the ip monitor query.

From the DomainTools
`IP Monitor documentation <https://www.domaintools.com/resources/api-documentation/ip-monitor/>`_:

    The IP Monitor API searches the daily activity of all our monitored TLDs on
    any given IP address. New, Deleted and Transferred domains records can be
    queried up to 6 days in the past.
