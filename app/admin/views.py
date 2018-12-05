from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:blue'>soonyang this is admin</h1>"
