import runner2, unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usein = runner2.Runner('Усейн', 10)
        self.andrei = runner2.Runner('Андрей', 9)
        self.nik = runner2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        cls.all_results = list(reversed(cls.all_results))
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usein_nik(self):
        tour = runner2.Tournament(90, self.usein, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrei_nik(self):
        tour = runner2.Tournament(90, self.andrei, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_all(self):
        tour = runner2.Tournament(90, self.andrei, self.usein, self.nik)
        result = tour.start()
        self.all_results.append(result)
        last = result[max(result.keys())]
        self.assertTrue(last == "Ник")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rn = runner2.Runner('name')
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rnr = runner2.Runner('name')
        for i in range(10):
            rnr.run()
        self.assertEqual(rnr.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn1 = runner2.Runner('name')
        rn2 = runner2.Runner('name')
        for i in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)

        
        