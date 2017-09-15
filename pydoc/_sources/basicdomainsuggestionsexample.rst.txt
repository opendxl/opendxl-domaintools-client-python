Basic Domain Suggestions Example
================================

This sample invokes and displays the results of a DomainTools
"Domain Suggestions" via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/domain-suggestions/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_domain_suggestions_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_domain_suggestions_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "query": "domain tools",
                "status_codes": {
                    "d": "deleted and available again",
                    "e": "on-hold (pending delete)",
                    "g": "on-hold (redemption period)",
                    "h": "on-hold (generic)",
                    "p": "registered and parked or redirected",
                    "q": "never registered before",
                    "w": "registered and active website",
                    "x": "registered and no website"
                },
                "suggestions": [
                    {
                        "domain": "domainfreetools",
                        "status": "qqqqqq"
                    },
                    {
                        "domain": "domainusatools",
                        "status": "qqqqqq"
                    }
                ],
                "tlds": [
                    "COM",
                    "NET",
                    "ORG",
                    "INFO",
                    "BIZ",
                    "US"
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

            # Invoke 'domain_suggestions' method on service
            resp_dict = client.domain_suggestions(["domain", "tools"])

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.domain_suggestions`
method is invoked with a ``list`` of search terms.  If the search only
requires one term, the argument could be specified as a ``str``, for example:

    .. code-block:: python

        resp_dict = client.domain_suggestions("domaintools")

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the domain suggestions query.

From the DomainTools
`Domain Suggestions documentation <https://www.domaintools.com/resources/api-documentation/domain-suggestions/>`_:

    The Domain Suggestions API provides a list of domain names that are similar
    to the words in a query string. It has a bias toward available domains and
    provides suggestions for .com, .net, .org, .info, .biz, and .us top level
    domain names.
