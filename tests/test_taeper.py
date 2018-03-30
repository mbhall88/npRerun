"""Tests for `taeper` package."""
import unittest
from taeper import taeper


class TestZuluToEpochTime(unittest.TestCase):
    """Test Zulu to Epoch converter function."""
    def test_ExampleFromRead_CorrectTimeInSeconds(self):
        """Simple test case"""
        zulu_time = "2018-01-03T16:45:30Z"
        result = taeper._zulu_to_epoch_time(zulu_time)
        expected = 1514997930.0
        self.assertEqual(result, expected)


class TestExtractTimeFields(unittest.TestCase):
    """Test function that extracts time info from fast5 files"""
    def test_Read9Fast5TestFile_CorrectFieldsExtracted(self):
        """Test fields in read9"""
        test_fast5 = 'tests/data/pass/read9.fast5'
        result = taeper.extract_time_fields(test_fast5)
        expected = {
            'exp_start_time': 1514997930.0,
            'sampling_rate': 4000.0,
            'duration': 19922.0,
            'start_time': 28238530.0
        }
        self.assertDictEqual(result, expected)


class TestCalculateTimestamp(unittest.TestCase):
    """Make sure timestamps are calculated correctly"""
    def test_Read8TimestampIsExactlyCorrect(self):
        test_fast5 = 'tests/data/pass/read8.fast5'
        result = taeper.calculate_timestamp(test_fast5)
        expected = 1515004995.93975  # calculated by hand
        self.assertEqual(result, expected)


class TestScantree(unittest.TestCase):
    """Test scantree functiion"""
    def test_TestOnlyFast5FilesReturned_NoCornerCaseFile(self):
        """Test on tests/data directory"""
        ext = '.fast5'
        path = 'tests'
        result = list(taeper.scantree(path, ext))
        expected = [
            'tests/data/fail/empty.fast5',
            'tests/data/fail/read0.fast5',
            'tests/data/fail/read6.fast5',
            'tests/data/pass/read1.fast5',
            'tests/data/pass/read2.fast5',
            'tests/data/pass/read3.fast5',
            'tests/data/pass/read4.fast5',
            'tests/data/pass/read5.fast5',
            'tests/data/pass/read7.fast5',
            'tests/data/pass/read8.fast5',
            'tests/data/pass/read9.fast5'
            ]
        for x, y in zip(expected, result):
            self.assertEqual(x, y)

    def test_TestCaseExtension_ReturnOnlyCornerCase(self):
        """Test for only corner case"""
        ext = '.case'
        path = 'tests'
        result = list(taeper.scantree(path, ext))
        expected = ['tests/data/corner.case', 'tests/data/fail/corner.case']
        for x, y in zip(expected, result):
            self.assertEqual(x, y)
