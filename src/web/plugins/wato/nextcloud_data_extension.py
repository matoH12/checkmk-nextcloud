#!/usr/bin/env python
#
# file: nextcloud_data_extension.py
#
# created: 22/05/2022
#
# Author: Martin Hasin
# email: martin.hasin@gmail.com
#
#

group = "datasource_programs"
register_rule(group,
              "special_agents:nextcloud_data",
              Dictionary(elements=[
                  ("username", TextAscii(title=_("Username"),
                                         allow_empty=False,
                                         )
                   ),
                  ("password", Password(title=_("Password"),
                                        allow_empty=False,
                                        )
                   ),
                  ("no_cert_check", FixedValue(
                          True,
                          title=_("Disable SSL certificate validation"),
                          totext=_("SSL certificate validation is disabled"),
                              )
                   )],
                      optional_keys=['no_cert_check']
                        ),
              title=_("Check health state of nextcloud "),
              help=_("This rule selects the ownloud agent instead of the "
                     "Check_MK Agent and allows monitoring of the owncloud "
                     "server using its  API. "
                     "You can configure your connection settings here."),
              )
