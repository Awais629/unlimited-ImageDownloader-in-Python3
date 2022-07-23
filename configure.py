"""    ENVIRONMENT SETTINGS    """
BROWSER = "Chrome"  # Options are CHROME or FIREFOX
HEADLESS = True  # Headless doesnt seem to run correctly in Chrome, but works correctly in Firefox
PARSER = "lxml" #lxml is the fastest but there are few different options

'''    VIEWING    '''
VIEW_MODE = "BOX" #BOX, STANDARD, or COMPRESSED
PRINT_ACTIONS = True #See every major action the bot takes
PRINT_SETTINGS = False #Print settings before you start
EXTRA_USER_INFO = True #Print data that match your criteria with the user info

"""    DEBUGGING    """
VERBOSE = False #See more detailed info on what the bot is reading
POTENTIAL_COMPANY = True #This attempts to get the company name a new way that is prone to errors but would only be used when no company is found the normal way
DEBUGGING = True