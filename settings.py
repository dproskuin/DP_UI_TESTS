

class Const:
    EMAIL = "d.proskurin@anchorfree.com"
    PASSWORD = "180122180Vippass!?!?"
    NEW_PASSWORD = "180122180Vippass"
    PANGO_JUNE_03_DESCRIPTION_TEXT = "This project is configured to test Fireshield feature on Prod env. "


class Urls:
    MAIN_URL = "https://developer.anchorfree.com"
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


class Variables:
    """
    Contains visible text variables for some elements. If text was changed in the Front-end, change it here.
    """

    # Landing page
    TOF = "Terms of Service"
    PP = "Privacy Policy"
    DOCUMENTATION = "Pango Developer Documentation"
    EMAIL_PASSWORD_NOT_MATCH = "Email and password do not match"
    FORGOT_PASSWORD_BUTTON = "Forgot password"
    RESET_PASSWORD_BUTTON = "Reset password"

    # User Profile Page
    UAE = "United Arab Emirates"
    ENTER_CURRENT_PASSWORD_MESSAGE = "Enter the current password"
    PASSWORD_CHANGED_SUCCESS = "Your password has been successfully changed"
    CHANGE_PASSWORD_BUTTON = "Change password"
    ACCOUNT_SECURITY_TAB_BUTTON = "Account security"
    SIGN_IN_BUTTON = "Sign In"
    TWO_FACTOR_AUTH = "Two-factor authentication"
    VIEW_PROFILE_BUTTON = "View Profile"

    # Project -> User Tab
    NO_PURCHASES_MESSAGE = "User has no purchases"
    ACCESS_TOKEN_STRING = "Access token"
    NO_SESSIONS_FOUND_MESSAGE = "No sessions have been found for the chosen period"
    SET_LIMIT_BUTTON = "Set limit"

    # Project page
    SEARCH_USERS_BUTTON = "Search users"
    ADD_LOCATION_BUTTON = "Add location"
    SERVER_POOLS = "Server pools for"
    SHOW_FEATURES_BUTTON = "Show features"
    USER_MANAGEMENT = "User management"
    ADD_PROJECT_BUTTON = "Add project"
    COMPANY_NAME_STRING = "Company name"
    LOCATION_LOADING_BUTTON = "Location loading"
    LOCATION_LOADING_MAP = "Location loading map"
    CREATE_PROJECT = "Create project"
