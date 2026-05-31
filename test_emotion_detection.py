import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test dla emocji: Radość (Joy)
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test dla emocji: Gniew (Anger)
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test dla emocji: Niesmak (Disgust)
        result_3 = emotion_detector("I am disaffected with this behavior")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test dla emocji: Smutek (Sadness)
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test dla emocji: Strach (Fear)
        result_5 = emotion_detector("I am really afraid of this")
        self.assertEqual(result_5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()