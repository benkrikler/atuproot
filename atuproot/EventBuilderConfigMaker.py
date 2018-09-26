import collections
import uproot

EventBuilderConfig = collections.namedtuple(
    'EventBuilderConfig',
    'inputPaths treeName start stop blocksize dataset name'
)

class EventBuilderConfigMaker(object):
    def __init__(self, blocksize):
        self.blocksize = blocksize

        # Cache nevents in each file - getting nevents takes a while
        self._nevents_in_file_cache = {}

    def create_config_for(self, dataset, files, start, length):
        config = EventBuilderConfig(
            inputPaths = files,
            treeName = dataset.tree,
            start = start,
            stop = length,
            blocksize = self.blocksize,
            dataset = dataset,
            name = dataset.name,
        )
        return config

    def file_list_in(self, dataset, maxFiles):
        if maxFiles < 0:
            return dataset.files
        return dataset.files[:min(maxFiles, len(dataset.files))]

    def nevents_in_file(self, path):
        if path in self._nevents_in_file_cache:
            nblocks = self._nevents_in_file_cache[path]
        else:
            # Try to open root file with standard memmap with uproot. Use
            # localsource option if it fails
            try:
                rootfile = uproot.open(path)
            except:
                rootfile = uproot.open(path, localsource=uproot.FileSource.defaults)
            nevents = len(rootfile[self.treeName])
            nblocks = int((nevents-1) / self.blocksize + 1)
            self._nevents_in_file_cache[path] = nblocks
        return nblocks
