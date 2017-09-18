Basic Account Information Example
=================================

This sample invokes and displays the results of a DomainTools
"Account Information" via DXL. This sample also demonstrates how to request
each of the different output formats that the DomainTools service supports:
``dict`` (Python dictionary), ``json``, and ``xml``.

For more information see:
    https://www.domaintools.com/resources/api-documentation/account-information/

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* The DomainTools API DXL service is running (see `DomainTools API DXL Service <https://github.com/opendxl/opendxl-domaintools-service-python>`_)

Running
*******

To run this sample execute the ``sample/basic/basic_account_information_example.py``
script as follows:

    .. parsed-literal::

        python sample/basic/basic_account_information_example.py

The output for the ``dict`` and ``json`` formats should appear similar to the
following:

    .. code-block:: json

        {
            "response": {
                "account": {
                    "active": true,
                    "api_username": "username"
                },
                "products": [
                    {
                        "absolute_limit": null,
                        "expiration_date": null,
                        "id": "account-information",
                        "per_minute_limit": "5",
                        "per_month_limit": "100000",
                        "usage": {
                            "month": "0",
                            "today": "0"
                        }
                    },
                    {
                        "absolute_limit": "10000",
                        "expiration_date": "2017-07-18",
                        "id": "parsed-whois",
                        "per_minute_limit": "120",
                        "per_month_limit": null,
                        "usage": {
                            "month": "0",
                            "today": "0"
                        }
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

            # Invoke 'account_information' method on service, in default (dict) output format
            resp_dict = client.account_information()

            # Print out the response
            print("Response in default output format:\n{}".format(
                MessageUtils.dict_to_json(resp_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxldomaintoolsclient.client.DomainToolsApiClient` instance is created
which will be used to invoke remote commands on the DomainTools API DXL
service.

Next, the
:func:`dxldomaintoolsclient.client.DomainToolsApiClient.account_information`
method is invoked.

The final step is to display the contents of the returned dictionary (``dict``)
which contains the results of the account information for the API user that
the DomainTools DXL service uses.

The sample code also demonstrates how to request to receive the response in the
other formats that the DomainTools service supports (``json`` and ``xml``):

    .. code-block:: python

        # Invoke 'account_information' method on service, in 'json' output
        resp_json = client.account_information(out_format="json")

        # Print out the response
        print("Response in json output format:\n{}".format(
            MessageUtils.dict_to_json(MessageUtils.json_to_dict(resp_json),
                                      pretty_print=True)))

        # Invoke 'account_information' method on service, in 'xml' output
        resp_xml = client.account_information(out_format="xml")

        # Print out the response
        print("Response in xml output format:\n{}".format(resp_xml))


For each of the response formats other than ``dict``, the response type is a
``str``. For example, the printed ``str`` content for the ``xml`` format should
look similar to the following:

    .. code-block:: xml

        <?xml version="1.0"?>
        <whoisapi>
            <response>
                <account>
                    <api_username>username</api_username>
                    <active>1</active>
                </account>
                <products>
                    <id>account-information</id>
                    <per_month_limit>100000</per_month_limit>
                    <per_minute_limit>5</per_minute_limit>
                    <absolute_limit/>
                    <usage>
                        <today>12</today>
                        <month>202</month>
                    </usage>
                    <expiration_date>2017-09-30</expiration_date>
                </products>
                <products>
                    <id>parsed-whois</id>
                    <per_month_limit/>
                    <per_minute_limit>120</per_minute_limit>
                    <absolute_limit>10000</absolute_limit>
                    <usage>
                        <today>0</today>
                        <month>4</month>
                    </usage>
                    <expiration_date>2017-09-30</expiration_date>
                </products>
            </response>
        </whoisapi>


From the DomainTools
`Account Information documentation <https://www.domaintools.com/resources/api-documentation/account-information/>`_:

        `"The Account Information API provides a quick and easy way to get a snapshot of
        API product usage for an account. Usage is broken down by day and by month."`
