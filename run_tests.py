import unittest

# Discover and run all test cases in the tests directory
if __name__ == "__main__":
    
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')
    
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)


