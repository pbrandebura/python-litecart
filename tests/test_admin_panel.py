def test_browse_through_admin_menu(app):
    app.admin_panel.login_to_admin_panel('admin', 'admin')
    app.admin_panel.click_on_every_menu_tab()


def test_countries_in_alfabetical_order(app):
    app.admin_panel.login_to_admin_panel('admin', 'admin')
    app.admin_panel.navigate_to_countries_tab()
    list_of_country = app.admin_panel.get_country_list()
    assert list_of_country, sorted(list_of_country)


def test_time_zones_in_alfabetical_order(app):
    app.admin_panel.login_to_admin_panel('admin', 'admin')
    app.admin_panel.navigate_to_countries_tab()
    countries = app.admin_panel.get_countries_with_more_time_zones()
    app.admin_panel.check_if_timezones_in_alfabetical_order(country_code=countries)
