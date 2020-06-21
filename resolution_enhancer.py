import torch


class ResolutionEnhancer:

    def __init__(self):
        self.model = None   # a model that gets an image and return image in the same size
        self.r = None   # the resolution enhancing factor
        self.patch_size = None

    def enhance(self, image):
        """
        get an image, return image in size larger by factor r.
        """
        pass

    def enhance_n_times(self, image, n):
        """
        perform "enhance" n times.
        """
        pass
