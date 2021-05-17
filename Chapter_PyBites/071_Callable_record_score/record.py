class RecordScore:
    """Class to track a game's maximum score"""
    def __init__(self):
        self.max_score = None # when we initiate this class max_score will be empty
    def __call__(self, score):
        if not self.max_score or score > self.max_score: #in the first call self.max_score gets the value of score, and from now on the max_score gets recorded. 
            self.max_score = score
        return self.max_score

