from typing import List, Optional

from pydantic import BaseModel, Field

from application.external.model.keypoint import FrameKeypointDTO


class VideoSimilarityRequest(BaseModel):
    exerciseId: int
    width: int = Field(default=1, ge=1, description="Width must be more than zero")
    height: int = Field(default=1, ge=1, description="Height must be more than zero")
    frames: List[FrameKeypointDTO]
    k: Optional[int] = Field(default=15, ge=1, description="K must be more than zero")
    size: Optional[int] = Field(default=15, ge=1, description="Size must be more than zero")
    index: str
