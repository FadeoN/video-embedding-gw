from typing import Optional


class IndexExerciseVideoCommand:
    def __init__(self,
                 exerciseId: str,
                 exerciseName: str,
                 url: str,
                 tag: str,
                 index: Optional[str] = None,
                 ):
        self.exerciseId = exerciseId
        self.exerciseName = exerciseName
        self.url = url
        self.tag = tag
        self.index = index
