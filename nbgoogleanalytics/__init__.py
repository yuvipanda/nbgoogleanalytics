from notebook.services.config import ConfigManager
from traitlets.config import Configurable
from traitlets import Unicode

def _jupyter_server_extension_paths():
    return [{
        'module': 'nbgoogleanalytics',
    }]

def _jupyter_nbextension_paths():
    return [
        {
            # Load this on all the pages!
            "section": "common",
            "dest": "nbgoogleanalytics",
            "src": "static",
            "require": "nbgoogleanalytics/main"
        }
    ]

class GoogleAnalytics(Configurable):
    tracking_id = Unicode(
        None,
        allow_none=True,
        help="""
        The Google Analytics Trackin ID to use.

        Usually in the form of UA-<some-number>-<number>.

        Set to None to disable tracking.
        """,
        config=True
    )

    def setup_config(self):
        # This is apparently a singleton?
        cm = ConfigManager()
        cm.update(
            'common',
            {
                'GoogleAnalytics': {
                    'tracking_id': self.tracking_id
                }
            }
        )

def load_jupyter_server_extension(nbapp):
    ga = GoogleAnalytics(parent=nbapp)
    ga.setup_config()
