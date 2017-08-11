Basic Reputation Example
========================

This sample invokes and displays the results of a DomainTools "Reputation" via
DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/reputation/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_reputation_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_reputation_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "domain": "domaintools.com",
                "risk_score": 0
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

            # Invoke 'reputation' method on service
            resp_dict = client.reputation("domaintools.org")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.reputation`
method is invoked with a domain name.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the reputation query.

From the DomainTools
`Reputation Documentation <https://www.domaintools.com/resources/api-documentation/reputation/>`_:

    Provides a risk score for the domain. The Reputation API is only available
    via our Enterprise Solutions team, and is not included in a membership.
