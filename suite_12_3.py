import runner2, unittest, tests_12_3

test_st = unittest.TestSuite()
test_st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_st)