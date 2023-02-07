import dvc.api


DVCFS_URL = "git@github.com:gchaperon/myfs-data"


class MyFileSystem(dvc.api.DVCFileSystem):
    @staticmethod
    def _get_kwargs_from_urls(bit):
        return dict(url=DVCFS_URL)
