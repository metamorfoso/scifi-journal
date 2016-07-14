from pipeline.storage import PipelineMixin
from whitenoise.django import GzipManifestStaticFilesStorage


class SimplePipelineMixin(PipelineMixin):
    def __init__(self, *args, **kwargs):
        super(PipelineMixin, self).__init__()


class GzipManifestPipelineStorage(SimplePipelineMixin,
                                  GzipManifestStaticFilesStorage):
    pass
