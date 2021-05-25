from typing import List, Optional

from application.external.model.keypoint import FrameKeypointDTO


class FindVideoSimilarityCommand:
    def __init__(self,
                 exerciseId: int,
                 width: int,
                 height: int,
                 frames: List[FrameKeypointDTO],
                 index: str,
                 k: Optional[int],
                 size: Optional[int]
                 ):
        self.exerciseId = exerciseId
        self.width = width
        self.height = height
        self.frames = frames
        self.k = k
        self.size = size
        self.index = index
