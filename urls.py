import settings
import importlib
import os
# this function takes api as an input and loads the urls of each app
def load_apps(api):

    # load installed apps
    for app in settings.INSTALLED_APPS:

        # urls file path
        path = settings.BASE_DIR + 'apps/' + app + '/urls.py'

        # load urls file for each app as a module
        try:
            # check if urls file is exist
            module = importlib.machinery.SourceFileLoader('urls.py', path).load_module()
        except:

            if not os.path.isfile(path):

                # If urls file not exists
                # create a new one
                with open(path, "w") as urls_file:
                    # Append 'hello' at the end of file
                    urls_file.write("from apps.{} import views\n".format(app))
                    urls_file.write("urls = []")
                    urls_file.close()


        # set urls routes for each app in RESTFull API object
        for url in module.urls:
            api.add_resource(url[0],url[1])

    return api
