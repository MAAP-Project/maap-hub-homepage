"""
jupyterhub_config purely used for testing changes to templates.

See README.md for information on how to test this out.
"""
import pathlib
from oauthenticator.generic import GenericOAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner
import os


HERE = pathlib.Path(__file__).parent

# Add templates from our local checkout to the path JupyterHub searches
# This allows us to override any template present in upstream
# jupyterhub (https://github.com/jupyterhub/jupyterhub/tree/main/share/jupyterhub/templates)
# locally
c.JupyterHub.template_paths = [str(HERE / 'templates')]

# We use this so we can get a 'login' button, instead of a username / password
# field.
c.JupyterHub.authenticator_class = GenericOAuthenticator


# Variables that are passed through to templates!
c.JupyterHub.template_vars = {
    'custom': {
        "redirect_to": None,
        "interface_selector": False,
        "default_url": "/",
        'org': {
            'name': 'The Multi-Mission Algorithm and Analysis Platform (MAAP) Project',
            'logo_url': 'https://maap-project.org/wp-content/uploads/2021/10/nasamaaplogo3.png',
            'url': 'https://maap-project.org/',
        },
        'operated_by': {
            'name': '2i2c',
            'url': 'https://2i2c.org',
            'custom_html': '',
        },
        'funded_by': {
            'name': 'NASA',
            'url': 'https://www.earthdata.nasa.gov/esds',
            'custom_html': '',
        },
        'designed_by': {
            'name': '2i2c',
            'url': 'https://2i2c.org',
            'custom_html': '',
        }
    }
}
