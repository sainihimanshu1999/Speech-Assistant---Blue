from PyObjCTools.TestSupport import *

import MediaToolbox


class TestMTFormatNames(TestCase):
    @min_os_level("10.10")
    def test_functions(self):
        self.assertResultIsCFRetained(MediaToolbox.MTCopyLocalizedNameForMediaType)
        self.assertResultIsCFRetained(MediaToolbox.MTCopyLocalizedNameForMediaSubType)


if __name__ == "__main__":
    main()
