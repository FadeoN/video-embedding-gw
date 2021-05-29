import os


class PoseEstimationApiOptions(object):
    def __init__(self,
                 url: str,
                 timeout: int = 1200):
        self.url = url
        self.timeout = timeout


class ImageEmbeddingApiOptions(object):
    def __init__(self,
                 url: str,
                 timeout: int = 1200):
        self.url = url
        self.timeout = timeout


class SimilarityApiOptions(object):
    def __init__(self,
                 url: str):
        self.url = url


class AppOptions(object):
    def __init__(self):

        self.project_name = "video-embedding-gw"
        if os.getenv("PROFILE") == "PROD":
            self.similarity_api_options = SimilarityApiOptions("http://165.22.67.71:5000")
            self.image_embedding_api_options = ImageEmbeddingApiOptions("http://165.22.67.71:5004")
            self.pose_estimation_api_options = PoseEstimationApiOptions("http://165.22.67.71:5001")

        else:
            self.similarity_api_options = SimilarityApiOptions("http://localhost:5000")
            self.image_embedding_api_options = ImageEmbeddingApiOptions("http://localhost:5004")
            self.pose_estimation_api_options = PoseEstimationApiOptions("http://localhost:5001")

APP_OPTIONS = AppOptions()
