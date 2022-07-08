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
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    CascadingDropdown,
    Dictionary,
    Integer,
    ListOf,
    ListOfStrings,
    RegExp,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
    SNMPCredentials,
)

from cmk.gui.plugins.wato.active_checks import (
    RulespecGroupIntegrateOtherServices,
)

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
            #      ("password",
            #         IndividualOrStoredPassword(
            #            title=_("Password"),
            #            allow_empty=False,)
            #      ),


                  ("hostnamenextcloud",
                     TextAscii(
                        title = _("DNS Hostname or IP address"),
                           default_value = "$HOSTNAME$",
                           allow_empty = True,
                           help = _("You can specify a hostname or IP address different from IP address "
                                    "of the host as configured in your host properties."),
                   )),


                  ("no_cert_check", FixedValue(
                          True,
                          title=_("Disable SSL certificate validation"),
                          totext=_("SSL certificate validation is disabled"),
                              )
                   )],
                      optional_keys=['no_cert_check','hostnamenextcloud']
                        ),
              title=_("Check health state of nextcloud "),
              help=_("This rule selects the ownloud agent instead of the "
                     "Check_MK Agent and allows monitoring of the owncloud "
                     "server using its  API. "
                     "You can configure your connection settings here."),
              )
