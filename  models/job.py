class JobPost:
    def __init__(self,title,company,link,description,location,tags,source,salary=None):
        self.title=title
        self.company=company
        self.link=link
        self.description=description
        self.location=location
        self.tags=tags
        self.source=source
        self.salary=salary or None

