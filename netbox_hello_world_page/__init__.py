from netbox.plugins import PluginConfig

from .version import __version__

class HelloWorldPageConfig(PluginConfig):
    name = "netbox_hello_world_page"
    verbose_name = "Hello World page"
    description = "An example NetBox plugin"
    version = __version__
    author = "Markku Leiniö"
    # base_url is what comes after /plugins/ in the URL
    base_url = "helloworld"
    required_settings = []
    default_settings = {}

config = HelloWorldPageConfig
