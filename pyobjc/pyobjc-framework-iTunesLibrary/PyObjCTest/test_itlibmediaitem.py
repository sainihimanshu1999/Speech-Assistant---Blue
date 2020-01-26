from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc


class TestITMediaItem(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItem, objc.objc_class)

    def testMethods(self):
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isRatingComputed)

        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.hasArtworkAvailable)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isPurchased)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isCloud)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isDRMProtected)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isVideo)
        self.assertResultIsBOOL(iTunesLibrary.ITLibMediaItem.isUserDisabled)

    def testConstants(self):
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindUnknown, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindSong, 2)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindMovie, 3)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindPodcast, 4)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindAudiobook, 5)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindPDFBooklet, 6)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindMusicVideo, 7)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindTVShow, 8)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindInteractiveBooklet, 9)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindHomeVideo, 12)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindRingtone, 14)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindDigitalBooklet, 15)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindIOSApplication, 16)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindVoiceMemo, 17)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindiTunesU, 18)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindBook, 19)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindPDFBook, 20)
        self.assertEqual(iTunesLibrary.ITLibMediaItemMediaKindAlertTone, 21)

        self.assertEqual(iTunesLibrary.ITLibMediaItemLyricsContentRatingNone, 0)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLyricsContentRatingExplicit, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLyricsContentRatingClean, 2)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeUnknown, 0)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeFile, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeURL, 2)
        self.assertEqual(iTunesLibrary.ITLibMediaItemLocationTypeRemote, 3)
        self.assertEqual(iTunesLibrary.ITLibMediaItemPlayStatusNone, 0)
        self.assertEqual(iTunesLibrary.ITLibMediaItemPlayStatusPartiallyPlayed, 1)
        self.assertEqual(iTunesLibrary.ITLibMediaItemPlayStatusUnplayed, 2)

        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumTitle, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertySortAlbumTitle, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumArtist, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAlbumRating, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumRatingComputed, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertySortAlbumArtist, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumIsGapless, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumIsCompilation, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumDiscCount, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumDiscNumber, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyAlbumTrackCount, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyArtistName, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertySortArtistName, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoIsHD, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoWidth, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoHeight, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoSeries, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVideoSortSeries, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoSeason, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyVideoEpisode, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVideoEpisodeOrder, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyHasArtwork, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyBitRate, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyBeatsPerMinute, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyCategory, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyComments, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyComposer, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortComposer, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyContentRating, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyLyricsContentRating, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyAddedDate, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyModifiedDate, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyDescription, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyIsUserDisabled, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyGenre, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyGrouping, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyIsVideo, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyKind, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyTitle, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySortTitle, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVolumeNormalizationEnergy, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyPlayCount, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyLastPlayDate, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyIsDRMProtected, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyIsPurchased, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyRating, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyRatingComputed, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyReleaseDate, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySampleRate, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySize, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyFileSize, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyUserSkipCount, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertySkipDate, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyStartTime, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyStopTime, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyTotalTime, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyTrackNumber, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyLocationType, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVoiceOverLanguage, unicode
        )
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyVolumeAdjustment, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyYear, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyMediaKind, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyLocation, unicode)
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyArtwork, unicode)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyPlayStatus, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyMovementCount, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyMovementName, unicode)
        self.assertIsInstance(
            iTunesLibrary.ITLibMediaItemPropertyMovementNumber, unicode
        )
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyWork, unicode)

    @expectedFailure
    def testConstants_missing(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaItemPropertyFileType, unicode)


if __name__ == "__main__":
    main()
