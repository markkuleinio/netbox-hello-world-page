from netbox.plugins import PluginMenu, PluginMenuItem

# If you don't need any menu items, just leave this file out

menuitem1 = PluginMenuItem(
    # "hello_world" is defined in urls.py
    link="plugins:netbox_hello_world_page:hello_world",
    link_text="Show me the page!",
)

menu = PluginMenu(
    label="Hello, World!",
    groups=(
        ("Pages", (menuitem1,)),
    ),
    # See the icons in https://pictogrammers.com/library/mdi/
    # (remember to add the "mdi-" prefix)
    icon_class="mdi mdi-human-greeting-variant",
)
