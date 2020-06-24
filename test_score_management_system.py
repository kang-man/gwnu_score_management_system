import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestScoreManagementSystem(unittest.TestCase):

    def setUp(self):
        self.m_open = mock_open(read_data="1556,강석주,80,60,40\n2332,김철수,90,90,90\n2333,김민정,80,80,80")
        
        self.m_write_open = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open.side_effect = [self.m_open.return_value, self.m_w]

    def test_constructor(self):
        cms = ScoreManagementSystem()
        self.assertIsNotNone(cms)

    def test_read(self): #자동차 정보 읽는 함수 
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            self.assertEqual(3, cms.read('score.csv'))

        self.m_open.assert_called_with('score.csv', 'rt', encoding='utf-8')

    def test_sort_1(self):
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,1556,강석주,80,60,40,180,60\n2,2332,김철수,90,90,90,270,90\n3,2333,김민정,80,80,80,240,80', result)
    
    def test_sort_2(self):
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort(order_key="register", order_way="des")
            self.assertEqual('3,2333,김민정,80,80,80,240,80\n2,2332,김철수,90,90,90,270,90\n1,1556,강석주,80,60,40,180,60', result)
    
    def test_sort_3(self):      
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort("avg","asc")
            self.assertEqual('1,1556,강석주,80,60,40,180,60\n3,2333,김민정,80,80,80,240,80\n2,2332,김철수,90,90,90,270,90', result)

    def test_sort_4(self):      
        with patch('score_management_system.open', self.m_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')

            result = cms.sort("avg", "des")
            self.assertEqual('2,2332,김철수,90,90,90,270,90\n3,2333,김민정,80,80,80,240,80\n1,1556,강석주,80,60,40,180,60', result)

    def test_write_1(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv')

        self.m_w.write.assert_called_with("1,1556,강석주,80,60,40,180,60\n2,2332,김철수,90,90,90,270,90\n3,2333,김민정,80,80,80,240,80")


    def test_write_2(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv' , 'register', 'des')

        self.m_w.write.assert_called_with("3,2333,김민정,80,80,80,240,80\n2,2332,김철수,90,90,90,270,90\n1,1556,강석주,80,60,40,180,60")

    def test_write_3(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv' , 'avg', 'asc')

        self.m_w.write.assert_called_with('1,1556,강석주,80,60,40,180,60\n3,2333,김민정,80,80,80,240,80\n2,2332,김철수,90,90,90,270,90')

    def test_write_4(self):
        with patch('score_management_system.open', self.m_write_open):
            cms = ScoreManagementSystem()
            cms.read('score.csv')
            cms.write('result.csv' , 'avg', 'des')

        self.m_w.write.assert_called_with("2,2332,김철수,90,90,90,270,90\n3,2333,김민정,80,80,80,240,80\n1,1556,강석주,80,60,40,180,60")


if __name__ == "__main__":
    unittest.main()