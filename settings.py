

class Const:
    EMAIL = "d.proskurin@anchorfree.com"
    PASSWORD = "180122180Vippass!?!?"
    NEW_PASSWORD = "180122180Vippass"
    PANGO_JUNE_03_DESCRIPTION_TEXT = "This project is configured to test Fireshield feature on Prod env. "


class Urls:
    MAIN_URL = "https://deploy-preview-122--pango-partner-portal.netlify.app"
    PROFILE_URL = "/profile"
    PANGO_JUNE_03_DASHBOARD = "/dashboard/pango_june03"
    PANGO_JUNE_03_USERS = "/users/pango_june03"
    PANGO_JUNE_03_COUNTRIES = "/network/pango_june03/countries/"
    PANGO_JUNE_03_LOCATIONS = "/network/pango_june03/locations/"
    PANGO_JUNE_03_POOLS = "/network/pango_june03/pools/"
    PANGO_JUNE_03_SETTINGS = "/settings/pango_june03"
    PANGO_JUNE_03_BILLING = "/billing/pango_june03"

    @staticmethod
    def get_user_url(project_name, user_id):
        return f"/user/{project_name}/{user_id}"
