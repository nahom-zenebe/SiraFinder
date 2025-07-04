class User:
    def __init__(self,telegram_id,skills=None,location=None,resume=None):
        self.telegram=telegram
        self.skills=skills or []
        self.location=location
        self.resume=resume

