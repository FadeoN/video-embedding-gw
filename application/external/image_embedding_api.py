import json
from typing import List

import httpx

from application.external.model.keypoint import FrameKeypointDTO, VideoEmbeddingRequest, VideoEmbeddingResponse
from infrastructure.configuration import APP_OPTIONS


async def get_video_embeddings(width: int, height: int, frames: List[FrameKeypointDTO]) -> VideoEmbeddingResponse:
    async with httpx.AsyncClient(timeout=APP_OPTIONS.image_embedding_api_options.timeout) as client:
        request = VideoEmbeddingRequest(width=width,
                                        height=height,
                                        frames=frames)
        endpoint = f"{APP_OPTIONS.image_embedding_api_options.url}/video/embedding"
        response = await client.post(endpoint, data=request.json())

    return VideoEmbeddingResponse.parse_raw(response.content)