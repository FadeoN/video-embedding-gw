from typing import List, Optional

from pydantic import BaseModel, Field


class FrameSimilarityDTO(BaseModel):
    score: float
    exerciseId: int
    exerciseName: str
    tag: str
    order: int

    def __hash__(self):
        return hash(f"{self.exerciseId}_{self.tag}")

    def __eq__(self, other):
        return self.exerciseId == other.exerciseId and self.tag == other.tag

class FrameSimilarityResponse(BaseModel):
    frameSimilarities: List[FrameSimilarityDTO]


class SearchFrameVectorRequest(BaseModel):
    vector: List[float]
    k: Optional[int] = Field(default=5, ge=1, description="K must be more than zero")
    size: Optional[int] = Field(default=10, ge=1, description="Size must be more than zero")
    index: str
