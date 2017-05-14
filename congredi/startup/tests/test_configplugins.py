class test_config(TimedTestCase):

    def test_config(self):
        """Grab Configuration From File"""
        self.threshold = .4
        newConf = configArr()
        existsConf = configArr()
        assert newConf == existsConf

    def test_bad_config(self):  # test for 38-39
        """corrupt yaml -> blank config IMPLEMENT"""
        self.threshold = .1

    def test_generate_config(self):
        """create config objects NO ASSERT"""
        self.threshold = .1
        config = {}
        config = generateConfig(config)

    def test_write_config(self):
        """writes YAML to file NO ASSERT"""
        self.threshold = .1
        config = generateConfig({})
        writeConfig('.test', config)

    def test_open_test_lacks_keys(self):
        """openTest checks for admins & users NO ASSERT"""
        self.threshold = .1
        openTest('.test')
