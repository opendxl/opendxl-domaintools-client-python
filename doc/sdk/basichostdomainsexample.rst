Basic Host Domains Example
==========================

This sample invokes and displays the results of a DomainTools "Host Domains" via
DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/reverse-ip/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_host_domains_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_host_domains_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "ip_addresses": {
                    "domain_count": 1,
                    "domain_names": [
                        "DAILYCHANGES.COM"
                    ],
                    "ip_address": "64.246.165.240"
                }
            }
        }

The received results are displayed.

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # Create client wrapper
        client = DomainToolsApiClient(dxl_client)

        # Invoke 'host domains' method on service
        resp_dict = client.host_domains("64.246.165.240")

        # Print out the response (convert dictionary to JSON for pretty printing)
        print "Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.host_domains`
method is invoked with a domain name.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the host domains query.

From the DomainTools
`Host Domains documentation <https://www.domaintools.com/resources/api-documentation/reverse-ip/>`_:

    The Reverse IP API provides a list of domain names that share the same
    Internet host (i.e. the same IP address). You can request an IP address
    directly, or you can provide a domain name; if you provide a domain name,
    the API will respond with the list of other domains that share the same IP.
