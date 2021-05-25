from typing import List, Optional

from pydantic.main import BaseModel
from pydantic.networks import HttpUrl


class FrameVectorPair(BaseModel):
    order: int
    vector: List[float]


class VideoEmbeddingResponse(BaseModel):
    frameVectorPairs: List[FrameVectorPair]


class KeypointDTO(BaseModel):
    name: str
    score: float
    x: float
    y: float


class FrameKeypointDTO(BaseModel):
    keypoints: List[KeypointDTO]


class VideoEmbeddingRequest(BaseModel):
    width: int
    height: int
    frames: List[FrameKeypointDTO]


class IndexExerciseVideoRequest(BaseModel):
    exerciseId: int
    exerciseName: str
    url: str
    tag: str
    frameVectorPairs: List[FrameVectorPair]
    index: Optional[str] = None


class VideoKeypointResponse(BaseModel):
    width: int
    height: int
    frames: List[FrameKeypointDTO]


class PredictVideoPoseRequest(BaseModel):
    url: HttpUrl