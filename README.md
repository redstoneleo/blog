This is my Django blog App. Demo : https://mathjoy.eu.org/
To include the app in your project, you need to add a reference to its configuration class in the INSTALLED_APPS setting.

    INSTALLED_APPS = [
        ...,
        "blog.apps.BlogConfig",
        ...,
    ]

Also don't forget to edit the project URLconf to reference the URLconf of this App.
