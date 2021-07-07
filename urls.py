import settings
import importlib

# this function takes api as an input and loads the urls of each app
def load_apps(api):

    # load installed apps
    for app in settings.INSTALLED_APPS:
        # load urls file for each app as a module
        module = importlib.machinery.SourceFileLoader('urls.py',settings.BASE_DIR + 'apps/' + app + '/urls.py').load_module()

        # set urls routes for each app in RESTFull API object
        for url in module.urls:
            api.add_resource(url[0],url[1])

    return api
