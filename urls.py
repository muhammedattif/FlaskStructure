import settings
import importlib

# this function takes api as an input and loads the urls of each app
def load_apps(api):

    # load installed apps
    for app in settings.INSTALLED_APPS:

        path = settings.BASE_DIR + 'apps/' + app + '/urls.py'
        # load urls file for each app as a module
        try:
            module = importlib.machinery.SourceFileLoader('urls.py', path).load_module()
        except:
            # If urls file not exists
            # create a new one
            with open(path, "w") as urls_file:
                # Append 'hello' at the end of file
                urls_file.write("from apps.fawry import views\n")
                urls_file.write("urls = []")

        # set urls routes for each app in RESTFull API object
        for url in module.urls:
            api.add_resource(url[0],url[1])

    return api
