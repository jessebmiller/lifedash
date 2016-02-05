from components import ( 
    render,
    Today,
)

from datetime import date
import unittest


class TestComponents(unittest.TestCase):

    def setUp(self):
        self.today = Today(
            date=date(year=2016, month=2, day=5),
            weather="Mockingly cloudy",
            temp=22,
        )

    def tearDown(self):
        pass

    def test_today(self):
        expected = """ 
    <div class="today">
      <time datetime="2016-02-05">Friday February 05 2016</time>
      <span class="weather">Mockingly cloudy</span>
      <span class="temp">22</span>
    </div>
    """
        self.assertEqual(render(self.today), expected)

    def test_can_pass(self):
        assert True
