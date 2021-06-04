import json
from typing import List, Optional

import httpx

from application.external.model.keypoint import IndexExerciseVideoRequest, FrameVectorPair
from application.external.model.similarity import SearchFrameVectorRequest, FrameSimilarityResponse
from infrastructure.configuration import APP_OPTIONS


async def index_video(exerciseId: str, exerciseName: str, url: str, tag: str, frameVectorPairs: List[FrameVectorPair], index: Optional[str] = None):
    async with httpx.AsyncClient() as client:
        endpoint = f"{APP_OPTIONS.similarity_api_options.url}/index/exercise"
        request = IndexExerciseVideoRequest(exerciseId=exerciseId,
                                                  exerciseName=exerciseName,
                                                  url=url,
                                                  tag=tag,
                                                  frameVectorPairs=frameVectorPairs,
                                                  index=index)

        return await client.post(endpoint, data=request.json())


async def search_frame_similarity(vector: List[float], index: str, k: int = 5, size: int = 10) -> FrameSimilarityResponse:
    async with httpx.AsyncClient() as client:
        endpoint = f"{APP_OPTIONS.similarity_api_options.url}/search/frame"
        request = SearchFrameVectorRequest(vector=vector,
                                           k=k,
                                           size=size,
                                           index=index)

        response = await client.post(endpoint, data=request.json())

    return FrameSimilarityResponse.parse_raw(response.content)

