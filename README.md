**Archived:** Don't send your students' behavior data to google

# nbgoogleanalytics
Simple [Jupyter Notebook](http://jupyter.org/) extension to inject
[Google Analytics](https://www.google.com/analytics/) tracking code into
Notebooks. Primarily intended for use with a hosted notebook set up,
such as [JupyterHub](https://github.com/jupyterhub/jupyterhub/)

## Privacy

This extension will not load Google Analytics if the user's browser
has [Do Not Track](http://donottrack.us/) enabled. This is by design,
since Google Analytics itself does not respect the Do Not Track header.
Almost all adblockers & privacy addons will also disable Google Analytics.

If you are providing a hosted service that uses this extension, it is
your responsibility to:

  - Ensure that your users know they are being tracked
  - Have a privacy policy that explains to users why they are being tracked,
    what the data is going to be used for, and how they can opt out.k

Don't just not be evil, try actively to be Good!

## Installation

A virtualenv is recommended for using this. Inside a virtualenv, you
can install this extension easily!

```bash
pip install nbgoogleanalytics

jupyter nbextensions install --py --sys-prefix nbgoogleanalytics
```

You can then enable it with:

```bash
jupyter nbextensions enable --py --sys-prefix nbgoogleanalytics
jupyter serverextensions enable --sys-prefix nbgoogleanalytics
```
## Configuration

There's only one configuration parameter, and that's the Google Analytics
Tracking Id. You get it after you set up a Google Analytics *property*, and
it looks something like `UA-NNNNNNN-N`.

You can easily pass that to the extension by passing it as a commandline
parameter.

```bash
jupyter notebook --GoogleAnalytics.tracking_id="UA-NNNNN-N"
```
