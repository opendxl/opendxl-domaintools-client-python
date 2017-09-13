Basic Reverse Whois Example
===========================

This sample invokes and displays the results of a DomainTools "Reverse Whois"
via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/reverse-whois/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_reverse_whois_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_reverse_whois_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "domain_count": {
                    "current": 338,
                    "historic": 449
                },
                "report_price": {
                    "current": 299,
                    "historic": 299
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

            # Invoke 'reverse_whois' method on service
            resp_dict = client.reverse_whois(["DomainTools LLC", "Seattle"],
                                             exclude=["Dont", "Want", "This", "One"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.reverse_whois`
method is invoked with a ``list`` of search terms and a ``list`` of words which
cannot appear in any Whois record returned in the result set. Note that the
``exclude`` argument is optional. If the search only requires one term, each
argument could be specified as a ``str``, for example:

    .. code-block:: python

        # Invoke 'reverse_whois' method on service
        resp_dict = client.reverse_whois("DomainTools LLC")


The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the reverse whois query.

From the DomainTools
`Reverse Whois Documentation <https://www.domaintools.com/resources/api-documentation/reverse-whois/>`_:

    The Reverse Whois API provides a list of domain names that share the same
    Registrant Information.
