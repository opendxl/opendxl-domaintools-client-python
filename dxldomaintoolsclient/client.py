from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class DomainToolsApiClient(Client):
    """
    The "DomainTools API DXL Python Client Library" client wrapper class.
    """

    #: The DXL service type for the DomainTools API
    _SERVICE_TYPE = "/opendxl-domaintools/service/domaintools"

    #: The "account information" DXL request topic
    _REQ_TOPIC_ACCOUNT_INFO = "{0}/account_information".format(_SERVICE_TYPE)
    #: The "brand monitor" DXL request topic
    _REQ_TOPIC_BRAND_MONITOR = "{0}/brand_monitor".format(_SERVICE_TYPE)
    #: The "domain profile" DXL request topic
    _REQ_TOPIC_DOMAIN_PROFILE = "{0}/domain_profile".format(_SERVICE_TYPE)
    #: The "domain search" DXL request topic
    _REQ_TOPIC_DOMAIN_SEARCH = "{0}/domain_search".format(_SERVICE_TYPE)
    #: The "domain suggestions" DXL request topic
    _REQ_TOPIC_DOMAIN_SUGGESTIONS = "{0}/domain_suggestions".format(
        _SERVICE_TYPE)
    #: The "hosting history" DXL request topic
    _REQ_TOPIC_HOSTING_HISTORY = "{0}/hosting_history".format(_SERVICE_TYPE)
    #: The "ip monitor" DXL request topic
    _REQ_TOPIC_IP_MONITOR = "{0}/ip_monitor".format(_SERVICE_TYPE)
    #: The "ip registrant monitor" DXL request topic
    _REQ_TOPIC_IP_REGISTRANT_MONITOR = "{0}/ip_registrant_monitor".format(
        _SERVICE_TYPE)
    #: The "iris" DXL request topic
    _REQ_TOPIC_IRIS = "{0}/iris".format(_SERVICE_TYPE)
    #: The "name server monitor" DXL request topic
    _REQ_TOPIC_NAME_SERVER_MONITOR = "{0}/name_server_monitor".format(
        _SERVICE_TYPE)
    #: The "parsed whois" DXL request topic
    _REQ_TOPIC_PARSED_WHOIS = "{0}/parsed_whois".format(_SERVICE_TYPE)
    #: The "phisheye" DXL request topic
    _REQ_TOPIC_PHISHEYE = "{0}/phisheye".format(_SERVICE_TYPE)
    #: The "phisheye term list" DXL request topic
    _REQ_TOPIC_PHISHEYE_TERM_LIST = "{0}/phisheye_term_list".format(
        _SERVICE_TYPE)
    #: The "registrant monitor" DXL request topic
    _REQ_TOPIC_REGISTRANT_MONITOR = "{0}/registrant_monitor".format(
        _SERVICE_TYPE)
    #: The "reputation" DXL request topic
    _REQ_TOPIC_REPUTATION = "{0}/reputation".format(_SERVICE_TYPE)
    #: The "reverse ip" DXL request topic
    _REQ_TOPIC_REVERSE_IP = "{0}/reverse_ip".format(_SERVICE_TYPE)
    #: The "host domains" DXL request topic
    _REQ_TOPIC_HOST_DOMAINS = "{0}/host_domains".format(_SERVICE_TYPE)
    #: The "reverse ip whois" DXL request topic
    _REQ_TOPIC_REVERSE_IP_WHOIS = "{0}/reverse_ip_whois".format(_SERVICE_TYPE)
    #: The "reverse name server" DXL request topic
    _REQ_TOPIC_REVERSE_NAME_SERVER = "{0}/reverse_name_server".format(
        _SERVICE_TYPE)
    #: The "reverse whois" DXL request topic
    _REQ_TOPIC_REVERSE_WHOIS = "{0}/reverse_whois".format(_SERVICE_TYPE)
    #: The "whois" DXL request topic
    _REQ_TOPIC_WHOIS = "{0}/whois".format(_SERVICE_TYPE)
    #: The "whois history" DXL request topic
    _REQ_TOPIC_WHOIS_HISTORY = "{0}/whois_history".format(_SERVICE_TYPE)

    #: The query request parameter
    _PARAM_QUERY = "query"
    #: The exclude request parameter
    _PARAM_EXCLUDE = "exclude"
    #: The domain status request parameter
    _PARAM_DOMAIN_STATUS = "domain_status"
    #: The days back request parameter
    _PARAM_DAYS_BACK = "days_back"
    #: The exclude query request parameter
    _PARAM_EXCLUDE_QUERY = "exclude_query"
    #: The max length query request parameter
    _PARAM_MAX_LENGTH = "max_length"
    #: The min length request parameter
    _PARAM_MIN_LENGTH = "min_length"
    #: The has hyphen request parameter
    _PARAM_HAS_HYPHEN = "has_hyphen"
    #: The has number request parameter
    _PARAM_HAS_NUMBER = "has_number"
    # The active only request parameter
    _PARAM_ACTIVE_ONLY = "active_only"
    # The deleted only request parameter
    _PARAM_DELETED_ONLY = "deleted_only"
    #: The anchor left request parameter
    _PARAM_ANCHOR_LEFT = "anchor_left"
    #: The anchor right request parameter
    _PARAM_ANCHOR_RIGHT = "anchor_right"
    #: The page request parameter
    _PARAM_PAGE = "page"
    #: The search type request parameter
    _PARAM_SEARCH_TYPE = "search_type"
    #: The server request parameter
    _PARAM_SERVER = "server"
    #: The country request parameter
    _PARAM_COUNTRY = "country"
    #: The org request parameter
    _PARAM_ORG = "org"
    #: The include total count request parameter
    _PARAM_INCLUDE_TOTAL_COUNT = "include_total_count"
    #: The domain request parameter
    _PARAM_DOMAIN = "domain"
    #: The ip request parameter
    _PARAM_IP = "ip"
    #: The email request parameter
    _PARAM_EMAIL = "email"
    #: The nameserver request parameter
    _PARAM_NAMESERVER = "nameserver"
    #: The registrar request parameter
    _PARAM_REGISTRAR = "registrar"
    #: The registrant request parameter
    _PARAM_REGISTRANT = "registrant"
    #: The registrant org request parameter
    _PARAM_REGISTRANT_ORG = "registrant_org"
    #: The include inactive request parameter
    _PARAM_INCLUDE_INACTIVE = "include_inactive"
    #: The limit request parameter
    _PARAM_LIMIT = "limit"
    #: The terms request parameter
    _PARAM_TERMS = "terms"
    #: The scope request parameter
    _PARAM_SCOPE = "scope"
    #: The mode request parameter
    _PARAM_MODE = "mode"
    #: The include reasons request parameter
    _PARAM_INCLUDE_REASONS = "include_reasons"

    @staticmethod
    def _add_string_param_by_name(req_dict, param_name, param_value,
                                  delimiter=""):
        """
        Adds the specified parameter to the dictionary as a string. If the
        param_value is a list, tuple, or set, the elements from the param_value
        are flattened into a string, with each element delimited by the value
        in the delimiter parameter.

        :param req_dict: The dictionary
        :param param_name: The name of the parameter
        :param param_value: The value for the parameter
        :param delimiter: The string to delimit flattened elements with
        """
        if param_value is not None:
            req_dict[param_name] = \
                delimiter.join(param_value) \
                if (isinstance(param_value, (list, tuple, set))) \
                else str(param_value)

    @staticmethod
    def _add_boolean_param_by_name(req_dict, param_name, param_value):
        """
        Adds the specified boolean parameter to the dictionary

        :param req_dict: The dictionary
        :param param_name: The name of the parameter
        :param param_value: The value for the parameter
        :raises ValueError: if the param_value cannot be coerced into a boolean
        """
        if param_value is not None:
            param_value_as_lowercase_string = str(param_value).lower()
            if param_value_as_lowercase_string not in ("true", "false"):
                raise ValueError("%s must be true or false, found: %s" %
                                 (param_name, param_value))
            req_dict[param_name] = param_value_as_lowercase_string

    @staticmethod
    def _add_query_param(req_dict, query, delimiter=""):
        """
        Adds the specified query parameter to the dictionary. If the
        param_value is a list, tuple, or set, the elements from the param_value
        are flattened into a string, with each element delimited by the value
        in the delimiter parameter.

        :param req_dict: The dictionary
        :param query: The query value
        :param delimiter: The string to delimit flattened elements with
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_QUERY, query, delimiter)

    @staticmethod
    def _add_exclude_param(req_dict, exclude):
        """
        Adds the specified exclude parameter to the dictionary. If the
        param_value is a list, tuple, or set, the elements from the param_value
        are flattened into a string, with each element delimited by a pipe
        character.

        :param req_dict: The dictionary
        :param exclude: The exclude value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_EXCLUDE, exclude, "|")

    @staticmethod
    def _add_domain_status_param(req_dict, domain_status):
        """
        Adds the specified domain_status parameter to the dictionary

        :param req_dict: The dictionary
        :param domain_status: The domain_status value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_DOMAIN_STATUS, domain_status)

    @staticmethod
    def _add_days_back_param(req_dict, days_back):
        """
        Adds the specified days_back parameter to the dictionary

        :param req_dict: The dictionary
        :param days_back: The days_back value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_DAYS_BACK, days_back)

    @staticmethod
    def _add_exclude_query_param(req_dict, exclude_query):
        """
        Adds the specified exclude_query parameter to the dictionary. If the
        param_value is a list, tuple, or set, the elements from the param_value
        are flattened into a string, with each element delimited by a space
        character.

        :param req_dict: The dictionary
        :param exclude_query: The exclude_query value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_EXCLUDE_QUERY, exclude_query,
            " ")

    @staticmethod
    def _add_page_param(req_dict, page):
        """
        Adds the specified page parameter to the dictionary

        :param req_dict: The dictionary
        :param page: The page value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_PAGE, page)

    @staticmethod
    def _add_server_param(req_dict, server):
        """
        Adds the specified server parameter to the dictionary

        :param req_dict: The dictionary
        :param server: The server value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_SERVER, server)

    @staticmethod
    def _add_country_param(req_dict, country):
        """
        Adds the specified country parameter to the dictionary

        :param req_dict: The dictionary
        :param country: The country value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_COUNTRY, country)

    @staticmethod
    def _add_include_total_count_param(req_dict, include_total_count):
        """
        Adds the specified include_total_count parameter to the dictionary

        :param req_dict: The dictionary
        :param include_total_count: The include_total_count value
        """
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_INCLUDE_TOTAL_COUNT,
            include_total_count)

    @staticmethod
    def _add_ip_param(req_dict, ip_address):
        """
        Adds the specified ip parameter to the dictionary

        :param req_dict: The dictionary
        :param ip_address: The ip value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_IP, ip_address)

    @staticmethod
    def _add_limit_param(req_dict, limit):
        """
        Adds the specified limit parameter to the dictionary

        :param req_dict: The dictionary
        :param limit: The limit value
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_LIMIT, limit)

    @staticmethod
    def _add_domain_param(req_dict, domain, delimiter=""):
        """
        Adds the specified domain parameter to the dictionary. If the
        param_value is a list, tuple, or set, the elements from the param_value
        are flattened into a string, with each element delimited by the value
        in the delimiter parameter.

        :param req_dict: The dictionary
        :param domain: The domain value
        :param delimiter: The string to delimit flattened elements with
        """
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_DOMAIN, domain, delimiter)

    def _invoke_service(self, req_dict, topic, out_format):
        """
        Invokes the DomainTools DXL service.

        :param req_dict: Dictionary containing request information
        :param topic: The DomainTools DXL topic to invoke
        :param out_format: The format in which the response output should be
            rendered.  Available formats include ``dict``, ``json``, and
            ``xml``. For ``dict``, the return type is a Python dictionary. For
            the other formats, the return type is a ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """

        # Create the DXL request message
        request = Request(topic)

        # Set the output format for the request. If the caller requested "dict"
        # as the output format, use "json" to simplify the conversion of the
        # output into a Python dictionary.
        req_dict_with_format = dict(req_dict)
        req_dict_with_format["format"] = "json" \
            if out_format == "dict" else out_format

        # Set the payload on the request message (Python dictionary to JSON
        # payload)
        MessageUtils.dict_to_json_payload(request, req_dict_with_format)

        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)

        # If the caller requested "dict" as the output format, convert the JSON
        # payload in the DXL response message to a Python dictionary and return
        # it. Otherwise, just decode the raw payload per whatever other format
        # was requested and return it.
        return MessageUtils.json_payload_to_dict(response) \
            if out_format == "dict" else \
            MessageUtils.decode_payload(response)

    def account_information(self, out_format="dict"):
        """
        Retrieve information for the DomainTools API user account. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#account-information>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/account-information/>`__
        documentation for more information.

        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}

        return self._invoke_service(req_dict, self._REQ_TOPIC_ACCOUNT_INFO,
                                    out_format)

    def brand_monitor(self, query, exclude=None, domain_status=None,
                      days_back=None, out_format="dict"):
        """
        Retrieves information for domains which match a customer's brand or
        monitored word/string. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#brand-monitor>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/brand-monitor/>`__
        documentation for more information.

        :param query: One or more domain search terms.
        :type query: str or list(str) or tuple(str) or set(str)
        :param exclude: [``optional``] : Domain names with these words will be
            excluded from the result set.
        :type exclude: str or list(str) or tuple(str) or set(str)
        :param str domain_status: [``optional``] : Scope of the domain names to
            search. By default, the API will search both new domain names and
            domain names which are now on-hold (pending delete). To narrow your
            search to only one of these status codes, set this parameter to
            either ``new`` or ``on-hold``.
        :param int days_back: [``optional``] : Use this parameter in
            exceptional circumstances where you need to search domains
            registered prior to the current date.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, "|")
        self._add_exclude_param(req_dict, exclude)
        self._add_domain_status_param(req_dict, domain_status)
        self._add_days_back_param(req_dict, days_back)

        return self._invoke_service(req_dict, self._REQ_TOPIC_BRAND_MONITOR,
                                    out_format)

    def domain_profile(self, query, out_format="dict"):
        """
        Retrieves a profile for the specified domain name. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#domain-profile>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/domain-profile/>`__
        documentation for more information.

        :param str query: Domain name for which to retrieve profile
            information.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """

        req_dict = {}
        self._add_query_param(req_dict, query)

        return self._invoke_service(req_dict, self._REQ_TOPIC_DOMAIN_PROFILE,
                                    out_format)

    def domain_search(self, query, exclude_query=None, max_length=None,
                      min_length=None, has_hyphen=None, has_number=None,
                      active_only=None, deleted_only=None, anchor_left=None,
                      anchor_right=None, page=None, out_format="dict"):
        """
        Retrieves information for domains which match a search string. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#domain-search>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/domain-search/>`__
        documentation for more information.

        :param query: One or more domain search terms.
        :type query: str or list(str) or tuple(str) or set(str)
        :param exclude_query: [``optional``] : Domain names with these words
            will be excluded from the result set.
        :type exclude_query: str or list(str) or tuple(str) or set(str)
        :param int max_length: [``optional``] : Limit the maximum domain
            character count.
        :param int min_length: [``optional``] : Limit the minimum domain
            character count.
        :param bool has_hyphen: [``optional``] : Return results with hyphens
            in the domain name.
        :param bool has_number: [``optional``] : Return results with numbers
            in the domain name.
        :param bool active_only: [``optional``] : Return only domains which
            are currently registered.
        :param bool deleted_only: [``optional``] : Return only domains
            previously registered but not currently registered.
        :param bool anchor_left: [``optional``] : Return only domains that
            start with the query term.
        :param bool anchor_right: [``optional``] : Return only domains that
            end with the query term.
        :param int page: [``optional``] : Sets the page of results to retrieve
            from the server.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, " ")
        self._add_exclude_query_param(req_dict, exclude_query)
        self._add_page_param(req_dict, page)

        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_MAX_LENGTH, max_length)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_MIN_LENGTH, min_length)

        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_HAS_HYPHEN, has_hyphen)
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_HAS_NUMBER, has_number)
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_ACTIVE_ONLY, active_only)
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_DELETED_ONLY, deleted_only)
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_ANCHOR_LEFT, anchor_left)
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_ANCHOR_RIGHT, anchor_right)

        return self._invoke_service(req_dict, self._REQ_TOPIC_DOMAIN_SEARCH,
                                    out_format)

    def domain_suggestions(self, query, out_format="dict"):
        """
        Retrieves list of domain names which are similar to words in the
        supplied ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#domain-suggestions>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/domain-suggestions/>`__
        documentation for more information.

        :param str query: Domain name for which to retrieve suggestions.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, " ")

        return self._invoke_service(req_dict,
                                    self._REQ_TOPIC_DOMAIN_SUGGESTIONS,
                                    out_format)

    def hosting_history(self, query, out_format="dict"):
        """
        Retrieves a list of changes which have occurred in a domain name's
        registrar, IP address, and name servers. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#hosting-history>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/hosting-history/>`__
        documentation for more information.

        :param str query: Domain name to retrieve hosting history for.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)

        return self._invoke_service(req_dict, self._REQ_TOPIC_HOSTING_HISTORY,
                                    out_format)

    def ip_monitor(self, query, days_back=None, page=None, out_format="dict"):
        """
        Retrieves activity for monitored domains which match the ip address
        supplied in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#ip-monitor>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/ip-monitor/>`__
        documentation for more information.

        :param str query: IP address to query. For example: ``65.55.53.233``.
        :param int days_back: [``optional``] : Use this parameter in
            exceptional circumstances where you need to search domains
            registered prior to the current date.
        :param int page: [``optional``] : Sets the page of results to retrieve
            from the server.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)
        self._add_days_back_param(req_dict, days_back)
        self._add_page_param(req_dict, page)

        return self._invoke_service(req_dict, self._REQ_TOPIC_IP_MONITOR,
                                    out_format)

    def ip_registrant_monitor(self, query, days_back=None,
                              search_type=None, server=None, country=None,
                              org=None, page=None, include_total_count=None,
                              out_format="dict"):
        """
        Retrieves information for IP ranges which match one of the terms in the
        supplied ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#ip-registrant-monitor>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/ip-registrant-monitor/>`__
        documentation for more information.

        :param query: One or more free text query terms.
        :type query: str or list(str) or tuple(str) or set(str)
        :param int days_back: [``optional``] : Use this parameter in
            exceptional circumstances where you need to search domains
            registered prior to the current date.
        :param str search_type: [``optional``] : Type of changes to return.
            Valid options are ``all``, ``additions``, ``removals``, and
            ``modifications``.  Defaults to ``all``.
        :param str server: [``optional``] : Limits results to ranges from a
            particular Whois server.
        :param str country: [``optional``] : Limits results to IP addresses
            allocated to an entity with a particular country. Valid options are
            ISO 3166-1 two character country codes.
        :param str org: [``optional``] : Limits results to a particular
            organization.
        :param int page: [``optional``] : Sets the page of results to retrieve
            from the server.
        :param bool include_total_count: [``optional``] : Return the total
            number of results for a query. This should typically be used only
            for the first page of a large result set.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, " ")
        self._add_days_back_param(req_dict, days_back)
        self._add_page_param(req_dict, page)
        self._add_server_param(req_dict, server)
        self._add_country_param(req_dict, country)
        self._add_include_total_count_param(req_dict, include_total_count)

        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_SEARCH_TYPE, search_type)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_ORG, org)

        return self._invoke_service(req_dict,
                                    self._REQ_TOPIC_IP_REGISTRANT_MONITOR,
                                    out_format)

    def iris(self, domain=None, ip_address=None, email=None, nameserver=None,
             registrar=None, registrant=None, registrant_org=None,
             out_format="dict"):
        """
        Retrieves Iris pivot engine domain data for any provided search terms,
        ANDed together. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#iris>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/iris/>`__
        documentation for more information.

        :param domain: [``optional``] : One or more domains.
        :type domain: str or list(str) or tuple(str) or set(str)
        :param str ip_address: [``optional``] : A single full IP address - for
            example: ``65.55.53.233`` - that will be matched to the A record
            for a domain name.
        :param str email: [``optional``] : A single email address. The results
            will match email addresses in the Admin, Billing, Registrant, and
            Technical Contacts, along with SSL, Whois Records, and DNS/SOA
            records.
        :param str nameserver: [``optional``] : The exact name of the server
            you wish to query.
        :param str registrar: [``optional``] : Word search on the domain
            registrar.
        :param str registrant: [``optional``] : Word search on the Whois
            registrant field.
        :param str registrant_org: [``optional``] : Word search on the Whois
            registrant organization field.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_domain_param(req_dict, domain, ",")
        self._add_ip_param(req_dict, ip_address)

        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_EMAIL, email)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_NAMESERVER, nameserver)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_REGISTRAR, registrar)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_REGISTRANT, registrant)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_REGISTRANT_ORG,
            registrant_org)

        return self._invoke_service(req_dict, self._REQ_TOPIC_IRIS, out_format)

    def name_server_monitor(self, query, days_back=None, page=None,
                            out_format="dict"):
        """
        Retrieves activity for monitored Name Servers which match the hostname
        supplied in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#name-server-monitor>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/name-server-monitor/>`__
        documentation for more information.

        :param str query: Hostname of the Name Server to query. For example:
            ``dynect.net``.
        :param int days_back: [``optional``] : Use this parameter in
            exceptional circumstances where you need to search domains
            registered prior to the current date.
        :param int page: [``optional``] : Sets the page of results to retrieve
            from the server.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)
        self._add_days_back_param(req_dict, days_back)
        self._add_page_param(req_dict, page)

        return self._invoke_service(req_dict,
                                    self._REQ_TOPIC_NAME_SERVER_MONITOR,
                                    out_format)

    def parsed_whois(self, query, out_format="dict"):
        """
        Retrieves parsed information extracted from the raw Whois record for
        the domain supplied in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#parsed-whois>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/parsed-whois/>`__
        documentation for more information.

        :param str query: Hostname of the Name Server to query. For example:
            ``dynect.net``.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)

        return self._invoke_service(req_dict, self._REQ_TOPIC_PARSED_WHOIS,
                                    out_format)

    def phisheye(self, query, days_back=None, out_format="dict"):
        """
        Retrieves daily monitor results from the DomainTools PhishEye product
        for the term supplied in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#phisheye-domain-list>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/phisheye/>`__
        documentation for more information.

        :param str query: Term for which the day's domains are desired.
        :param int days_back: [``optional``] : Use this parameter in
            exceptional circumstances where you need to search domains
            registered prior to the current date.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)
        self._add_days_back_param(req_dict, days_back)

        return self._invoke_service(req_dict, self._REQ_TOPIC_PHISHEYE,
                                    out_format)

    def phisheye_term_list(self, include_inactive=None, out_format="dict"):
        """
        Retrieves a list of terms setup for the DomainTools PhishEye product
        for this account. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#phisheye-term-list>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/phisheye/>`__
        documentation for more information.

        :param bool include_inactive: [``optional``] : Use this parameter to
            display terms that may have been inactivated in users' lists.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_INCLUDE_INACTIVE,
            include_inactive)

        return self._invoke_service(req_dict,
                                    self._REQ_TOPIC_PHISHEYE_TERM_LIST,
                                    out_format)

    def registrant_monitor(self, query, exclude=None, days_back=None,
                           limit=None, out_format="dict"):
        """
        Retrieves information from the ownership (Whois) records of domain
        names for search terms specified in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#registrant-monitor>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/registrant-monitor/>`__
        documentation for more information.

        :param query: One or more search terms.
        :type query: str or list(str) or tuple(str) or set(str)
        :param exclude: [``optional``] : Whois records with these words will be
            excluded from the result set.
        :type exclude: str or list(str) or tuple(str) or set(str)
        :param int days_back: [``optional``] : Use this parameter in
            exceptional circumstances where you need to search domains
            registered prior to the current date.
        :param int limit: [``optional``] : Limit the number of matched domain
            names that are returned in your result set.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, "|")
        self._add_exclude_param(req_dict, exclude)
        self._add_days_back_param(req_dict, days_back)
        self._add_limit_param(req_dict, limit)

        return self._invoke_service(req_dict,
                                    self._REQ_TOPIC_REGISTRANT_MONITOR,
                                    out_format)

    def reputation(self, query, include_reasons=None, out_format="dict"):
        """
        Retrieves reputation information for the domain specified in the
        ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#reputation>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/reputation/>`__
        documentation for more information.

        :param str query: Input domain for which the risk score is desired.
        :param bool include_reasons: [``optional``] : Return a list of reasons
            for the risk score determination.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)
        DomainToolsApiClient._add_boolean_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_INCLUDE_REASONS,
            include_reasons)

        return self._invoke_service(req_dict, self._REQ_TOPIC_REPUTATION,
                                    out_format)

    def reverse_ip(self, domain, limit=None, out_format="dict"):
        """
        Retrieves a list of containers which share the same domain name. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#reverse-ip>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/reverse-ip/>`__
        documentation for more information.

        :param str domain: Domain name for which the list of containers is
            desired.
        :param int limit: [``optional``] : Limit the number of matched domain
            names that are returned in your result set.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_domain_param(req_dict, domain)
        self._add_limit_param(req_dict, limit)

        return self._invoke_service(req_dict, self._REQ_TOPIC_REVERSE_IP,
                                    out_format)

    def host_domains(self, ip_address, limit=None, out_format="dict"):
        """
        Retrieves a list of containers which share the same IP address. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#host-domains>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/reverse-ip/>`__
        documentation for more information.

        :param str ip_address: IP address for which the list of containers is
            desired.
        :param int limit: [``optional``] : Limit the number of matched domain
            names that are returned in your result set.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_ip_param(req_dict, ip_address)
        self._add_limit_param(req_dict, limit)

        return self._invoke_service(req_dict, self._REQ_TOPIC_HOST_DOMAINS,
                                    out_format)

    def reverse_ip_whois(self, query=None, ip_address=None, country=None,
                         server=None, include_total_count=None, page=None,
                         out_format="dict"):
        """
        Retrieves a list of IP ranges that are owned by an Organization. Either
        a ``query`` or an ``ip_address`` parameter must be specified, but not
        both. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#reverse-ip-whois>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/reverse-ip-whois/>`__
        documentation for more information.

        :param query: [``optional``] : One or more search terms. The query
            terms have the following rules:
            +term: Term must be included in the results.
            -term: Term must not be included in the results.
            term*: Term as a prefix must be included in the results.
            No modifiers: The search performed is a phrase search.
            For example: if you provide a query of ``google inc`` then only
            results that include both items in the order provided will be
            included.
        :type query: str or list(str) or tuple(str) or set(str)
        :param str ip_address: [``optional``] : Returns the most recent cached
            ip whois record for the allocated range the ip address is in.
        :param str country: [``optional``] : Limits results to IP addresses
            allocated to an entity with a particular country. Valid options are
            ISO 3166-1 two character country codes.
        :param str server: [``optional``] : Limits results to ranges from a
            particular Whois server.
        :param bool include_total_count: [``optional``] : Return the total
            number of results for a query. This should typically be used only
            for the first page of a large result set.
        :param int page: [``optional``] : Sets the page of results to retrieve
            from the server.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, " ")
        self._add_ip_param(req_dict, ip_address)
        self._add_country_param(req_dict, country)
        self._add_server_param(req_dict, server)
        self._add_include_total_count_param(req_dict, include_total_count)
        self._add_page_param(req_dict, page)

        return self._invoke_service(req_dict, self._REQ_TOPIC_REVERSE_IP_WHOIS,
                                    out_format)

    def reverse_name_server(self, query, limit=None, out_format="dict"):
        """
        Retrieves a list of the domain names that share the same primary or
        secondary name server. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#reverse-name-server>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/reverse-name-server/>`__
        documentation for more information.

        :param str query: Domain name or a name server to query.
        :param int limit: [``optional``] : Limit the number of matched domain
            names that are returned in your result set.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)
        self._add_limit_param(req_dict, limit)

        return self._invoke_service(req_dict,
                                    self._REQ_TOPIC_REVERSE_NAME_SERVER,
                                    out_format)

    def reverse_whois(self, query, exclude=None, scope=None, mode=None,
                      out_format="dict"):
        """
        Retrieves a list of the domain names that share the same Registrant
        Information. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#reverse-whois>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/reverse-whois/>`__
        documentation for more information.

        :param query: One or more terms to search for in the Whois record.
        :type query: str or list(str) or tuple(str) or set(str)
        :param exclude: [``optional``] : Domain names with Whois records that
            match these terms will be excluded from the result set.
        :type exclude: str or list(str) or tuple(str) or set(str)
        :param str scope: [``optional``] : Use ``current`` to include only
            current Whois records or ``historic`` to include both current and
            historic Whois records in the results. The default is ``current``.
        :param str mode: [``optional``] : Use ``quote`` to only list the size
            and retail price of the query if you have per-domain pricing access
            or ``purchase`` to include the complete list of domain names that
            match the query.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query, "|")
        self._add_exclude_param(req_dict, exclude)

        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_SCOPE, scope)
        DomainToolsApiClient._add_string_param_by_name(
            req_dict, DomainToolsApiClient._PARAM_MODE, mode)

        return self._invoke_service(req_dict, self._REQ_TOPIC_REVERSE_WHOIS,
                                    out_format)

    def whois(self, query, out_format="dict"):
        """
        Retrieves the most recent Whois record for the domain name or IP
        address provided in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#whois-lookup>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/whois-lookup/>`__
        documentation for more information.

        :param str query: Domain name or IP address to query.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)

        return self._invoke_service(req_dict, self._REQ_TOPIC_WHOIS,
                                    out_format)

    def whois_history(self, query, out_format="dict"):
        """
        Retrieves a list of historic Whois records for the domain name provided
        in the ``query`` parameter. See
        `DXL service method <https://github.com/opendxl/opendxl-domaintools-service-python/wiki/Service-Methods#whois-history>`__
        and `DomainTools API <https://www.domaintools.com/resources/api-documentation/whois-history/>`__
        documentation for more information.

        :param str query: Domain name to query.
        :param str out_format: [``optional``] : The format in which the
            response output should be rendered.  Available formats include
            ``dict``, ``json``, and ``xml``. For ``dict``, the return type is a
            Python dictionary. For the other formats, the return type is a
            ``unicode``.
        :return: Response data.
        :rtype: dict or unicode
        """
        req_dict = {}
        self._add_query_param(req_dict, query)

        return self._invoke_service(req_dict, self._REQ_TOPIC_WHOIS_HISTORY,
                                    out_format)
