from apps.dashboard.urls import urls as dashboard_urls
from apps.user.urls import urls as user_urls

import itertools

# this function takes api as an input and loads the urls of each app
def load_urls(api):

    urls = list(itertools.chain(

            dashboard_urls,
            user_urls
    ))

    #load urls of each app
    for url in urls:
        api.add_resource(url[0],url[1])

    return api
