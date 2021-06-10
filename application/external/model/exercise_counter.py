from enum import Enum

class ExerciseStage(Enum):

    BEGINNING = 1
    END = 2

    def __init__(self, count=0):
        self.count = count
        self.limit = 2

    def isCompleted(self):
        return self.count >= self.limit

    def increaseCount(self):
        self.count += 1

class ExerciseCounter:

    def __init__(self,
                 exerciseId: str):
        self.exerciseId = exerciseId
        self.count = 0
        self.current_stage = ExerciseStage.BEGINNING
        self.isEndPartCompleted = False

    def __next__(self, stage: ExerciseStage):
        if self.current_stage == stage:
            self.current_stage.increaseCount()
            return

        self.nextStage()

    def nextStage(self):
        if self.current_stage.isCompleted():
            if self.current_stage == ExerciseStage.BEGINNING:
                self.current_stage = ExerciseStage.END
                self.count += 1 if self.isEndPartCompleted else 0
            elif self.current_stage == ExerciseStage.END:
                self.current_stage = ExerciseStage.BEGINNING
                self.isEndPartCompleted = True
