Basic PhishEye Term List Example
================================

This sample invokes and displays the results of a DomainTools
"PhishEye Term List" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/phisheye/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the
``sample/basic/basic_phisheye_term_list_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_phisheye_term_list_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "terms": [
                    {
                        "term": "apple",
                        "active": true,
                        "user_monitor_count": 2
                    },
                    {
                        "term": "chevrolet",
                        "active": true,
                        "user_monitor_count": 1
                    },
                    {
                        "term": "yahoo",
                        "active": false,
                        "user_monitor_count": 1
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
            resp_dict = client.phisheye_term_list(True)

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.phisheye_term_list`
method is invoked with a ``bool`` value of
``True``. The ``bool`` value indicates whether or not terms which have been
inactivated in user list should be included in responses. The ``bool`` value
is optional, defaulting to ``False``.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the PhishEye query.

From the DomainTools
`PhishEye Term List Documentation <https://www.domaintools.com/resources/api-documentation/phisheye/>`_:

        `"This provides a list of terms that are set up for this account. The
        PhishEye API is only available via our Enterprise Solutions team, and is
        not included in a membership."`
