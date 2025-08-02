import solara

# Define the navigation structure
pages = [
    {"label": "Getting Started", "path": "/getting-started"},
    {"label": "Components", "path": "/components"},
    {"label": "Reference", "path": "/reference"},
]

@solara.component
def Page():
    # Get the current path
    current_path = solara.use_route().path

    # Sidebar with navigation
    with solara.SideBar():
        solara.Markdown("# Docs")
        for page in pages:
            solara.Link(page["label"], page["path"], classes="my-2")

    # Routing to pages
    if current_path == "/getting-started":
        import pages.getting_started as getting_started
        getting_started.Page()
    elif current_path == "/components":
        import pages.components as components
        components.Page()
    elif current_path == "/reference":
        import pages.reference as reference
        reference.Page()
    else:
        solara.Markdown("# Welcome to the Mini Solara Docs\n\nSelect a page from the sidebar.")