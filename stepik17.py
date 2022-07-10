"""AI is creating summary for
"""


class Video:
    """Representation of a video"""

    def __init__(self):
        self.name = ""

    def create(self, name):
        """Create a video object"""
        self.name = name

    def play(self):
        """Play a video"""
        print(f"воспроизведение видео {self.name}")


class YouTube:
    """AI is creating summary for"""

    videos = []

    @classmethod
    def add_video(cls, video):
        """AI is creating summary for add_video

        Args:
            video ([type]): [description]
        """
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        """AI is creating summary for play"""
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
#YouTube.play(0)
#YouTube.play(1)
