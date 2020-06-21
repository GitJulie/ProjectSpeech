import webbrowser as wb


class WebsitesManagement:
    def __init__(self, name):
        self.name = str(name)
        self.url = self.open_url()

    def open_url(self):
        return wb.get().open_new("https://www.{}.com \n".format(self.name))
