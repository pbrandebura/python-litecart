
def test_open_link_in_new_window_country_tab(app):
    app.admin_panel.login_to_admin_panel('admin', 'admin')
    app.admin_panel.navigate_to_countries_tab()
    app.admin_panel.open_add_new_country()
    app.admin_panel.click_on_every_external_url()
