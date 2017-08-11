Basic Domain Search Example
===========================

This sample invokes and displays the results of a DomainTools "Domain Search"
via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/domain-search/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_domain_search_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_domain_search_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "query_info": {
                    "active_only": false,
                    "anchor_left": false,
                    "anchor_right": false,
                    "deleted_only": false,
                    "exclude_query": "",
                    "has_hyphen": true,
                    "has_number": true,
                    "limit": 100,
                    "max_length": 25,
                    "min_length": 1,
                    "page": 1,
                    "total_results": 2
                },
                "results": [
                    {
                        "char_count": 11,
                        "has_active": 1,
                        "has_deleted": 1,
                        "has_hyphen": 0,
                        "has_number": 0,
                        "hashad_tlds": [
                            "asia",
                            "at",
                        ],
                        "sld": "domaintools",
                        "tlds": [
                            "asia",
                            "at",
                        ],
                        "tlds_count": 2
                    },
                    {
                        "char_count": 19,
                        "has_active": 1,
                        "has_deleted": 1,
                        "has_hyphen": 0,
                        "has_number": 0,
                        "hashad_tlds": [
                            "com"
                        ],
                        "sld": "domainbusinesstools",
                        "tlds": [
                            "com"
                        ],
                        "tlds_count": 1
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

            # Invoke 'domain_search' method on service
            resp_dict = client.domain_search(["domain", "tools"], max_length=52,
                                             has_hyphen=False, page=1)

            # Print out the response (convert dictionary to JSON for pretty printing)
            print "Response:\n{0}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.domain_search`
method is invoked with a ``list`` of search terms, a maximum length of ``52``
characters which can appear in the domain name, a value of ``False`` to indicate
that domains with hyphen characters cannot appear in any matching domains, and
that the first page of results should be returned. Note that the only required
argument is the first one, the ``query`` search term(s). If the search only
requires one term, the argument could be specified as a ``str``, for example:

    .. code-block:: python

        resp_dict = client.domain_search("domaintools")


The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the domain search.

From the DomainTools
`Domain Search documentation <https://www.domaintools.com/resources/api-documentation/domain-search/>`_:

    The Domain Search API searches for domain names that match your specific
    search string. Unlike Domain Suggestions, Domain Search finds currently
    registered or previously registered domain names that are either currently
    registered or have been registered in the past under one of the major gTLD's
    (.com, .net, .org, .info, .us, or .biz), many country code TLDs, or the new
    gTLDs.
