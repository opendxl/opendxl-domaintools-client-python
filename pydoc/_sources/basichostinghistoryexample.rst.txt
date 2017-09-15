Basic Hosting History Example
=============================

This sample invokes and displays the results of a DomainTools "Hosting History"
via DXL.

For more information see:
    https://www.domaintools.com/resources/api-documentation/hosting-history/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_hosting_history_example.py`` script as follows:

    .. parsed-literal::

        python sample/basic/basic_hosting_history_example.py

The output should appear similar to the following:

    .. code-block:: json

        {
            "response": {
                "domain_name": "domaintools.com",
                "ip_history": [
                    {
                        "action": "N",
                        "action_in_words": "New",
                        "actiondate": "2004-05-03",
                        "domain": "DOMAINTOOLS.COM",
                        "post_ip": "63.247.77.156",
                        "pre_ip": null
                    },
                    {
                        "action": "C",
                        "action_in_words": "Change",
                        "actiondate": "2015-04-02",
                        "domain": "DOMAINTOOLS.COM",
                        "post_ip": "199.30.228.112",
                        "pre_ip": "8.247.70.160"
                    }
                ],
                "nameserver_history": [
                    {
                        "action": "T",
                        "action_in_words": "Transfer",
                        "actiondate": "2002-04-14",
                        "domain": "DOMAINTOOLS.COM",
                        "post_mns": "Xxxnameservers.com",
                        "pre_mns": "Interland.net"
                    },
                    {
                        "action": "T",
                        "action_in_words": "Transfer",
                        "actiondate": "2004-11-25",
                        "domain": "DOMAINTOOLS.COM",
                        "post_mns": "Host.org",
                        "pre_mns": "Xxxnameservers.com"
                    }
                ],
                "registrar_history": [
                    {
                        "date_created": "1998-08-02",
                        "date_expires": "2003-08-01",
                        "date_lastchecked": "2003-06-28",
                        "date_updated": "2002-04-12",
                        "domain": "DOMAINTOOLS.COM",
                        "registrar": "Tucows",
                        "registrartag": "Tucows"
                    },
                    {
                        "date_created": "1998-08-02",
                        "date_expires": "2017-08-01",
                        "date_lastchecked": "2014-08-15",
                        "date_updated": "2014-07-24",
                        "domain": "DOMAINTOOLS.COM",
                        "registrar": "eNom.com",
                        "registrartag": "ENOM, INC."
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

            # Invoke 'hosting_history' method on service
            resp_dict = client.hosting_history("domaintools.com")

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.hosting_history`
method is invoked with a domain name.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the hosting history query.

From the DomainTools
`Hosting History documentation <https://www.domaintools.com/resources/api-documentation/hosting-history/>`_:

        The Hosting History API provides a list of changes that have occurred in
        a Domain Name's registrar, IP address, and name servers. IP and name
        server events include the value before and after the change and indicate
        the type of action that triggered the event.
