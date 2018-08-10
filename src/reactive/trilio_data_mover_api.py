from charms.reactive import when, when_not, set_flag


@when_not('trilio-data-mover-api.installed')
def install_trilio_data_mover_api():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    set_flag('trilio-data-mover-api.installed')
