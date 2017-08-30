import os
from jinja2 import FileSystemLoader, Environment
from staticjinja import make_site

STATICPATH = "static/"

def check_dir_site(site):
    if not os.path.exists(site):
        os.mkdir(site)


if __name__== "__main__":
    name_folder_site = 'site'
    check_dir_site(name_folder_site)
    site = make_site(outpath='site', staticpaths=STATICPATH)
    site.render()