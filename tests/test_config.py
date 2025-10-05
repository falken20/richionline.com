"""
Tests for the config.py module.
"""
import pytest
import config


class TestConfigConstants:
    """Tests for configuration constants."""
    
    def test_title_exists(self):
        """Test that __title__ is defined."""
        assert hasattr(config, '__title__')
        assert isinstance(config.__title__, str)
        assert len(config.__title__) > 0
    
    def test_version_exists(self):
        """Test that __version__ is defined."""
        assert hasattr(config, '__version__')
        assert isinstance(config.__version__, str)
        assert config.__version__ == '1.0.0'
    
    def test_author_exists(self):
        """Test that __author__ is defined."""
        assert hasattr(config, '__author__')
        assert isinstance(config.__author__, str)
        assert config.__author__ == 'Falken'
    
    def test_url_github_exists(self):
        """Test that __url_github__ is defined and valid."""
        assert hasattr(config, '__url_github__')
        assert isinstance(config.__url_github__, str)
        assert config.__url_github__.startswith('https://github.com/')
    
    def test_url_twitter_exists(self):
        """Test that __url_twitter__ is defined and valid."""
        assert hasattr(config, '__url_twitter__')
        assert isinstance(config.__url_twitter__, str)
        assert config.__url_twitter__.startswith('https://twitter.com/')
    
    def test_url_linkedin_exists(self):
        """Test that __url_linkedin__ is defined and valid."""
        assert hasattr(config, '__url_linkedin__')
        assert isinstance(config.__url_linkedin__, str)
        assert config.__url_linkedin__.startswith('https://www.linkedin.com/')
    
    def test_license_exists(self):
        """Test that __license__ is defined."""
        assert hasattr(config, '__license__')
        assert isinstance(config.__license__, str)
        assert 'MIT' in config.__license__
    
    def test_copyright_exists(self):
        """Test that __copyright__ is defined."""
        assert hasattr(config, '__copyright__')
        assert isinstance(config.__copyright__, str)
        assert '©' in config.__copyright__ or '(c)' in config.__copyright__.lower()
    
    def test_features_exists(self):
        """Test that __features__ is defined."""
        assert hasattr(config, '__features__')
        assert isinstance(config.__features__, list)


class TestSetupData:
    """Tests for SETUP_DATA dictionary."""
    
    def test_setup_data_exists(self):
        """Test that SETUP_DATA is defined."""
        assert hasattr(config, 'SETUP_DATA')
        assert isinstance(config.SETUP_DATA, dict)
    
    def test_setup_data_has_title(self):
        """Test that SETUP_DATA contains title."""
        assert 'title' in config.SETUP_DATA
        assert config.SETUP_DATA['title'] == config.__title__
    
    def test_setup_data_has_version(self):
        """Test that SETUP_DATA contains version."""
        assert 'version' in config.SETUP_DATA
        assert config.SETUP_DATA['version'] == config.__version__
    
    def test_setup_data_has_author(self):
        """Test that SETUP_DATA contains author."""
        assert 'author' in config.SETUP_DATA
        assert config.SETUP_DATA['author'] == config.__author__
    
    def test_setup_data_has_url_github(self):
        """Test that SETUP_DATA contains GitHub URL."""
        assert 'url_github' in config.SETUP_DATA
        assert config.SETUP_DATA['url_github'] == config.__url_github__
    
    def test_setup_data_has_url_twitter(self):
        """Test that SETUP_DATA contains Twitter URL."""
        assert 'url_twitter' in config.SETUP_DATA
        assert config.SETUP_DATA['url_twitter'] == config.__url_twitter__
    
    def test_setup_data_has_url_linkedin(self):
        """Test that SETUP_DATA contains LinkedIn URL."""
        assert 'url_linkedin' in config.SETUP_DATA
        assert config.SETUP_DATA['url_linkedin'] == config.__url_linkedin__
    
    def test_setup_data_has_license(self):
        """Test that SETUP_DATA contains license."""
        assert 'license' in config.SETUP_DATA
        assert config.SETUP_DATA['license'] == config.__license__
    
    def test_setup_data_has_copyright(self):
        """Test that SETUP_DATA contains copyright."""
        assert 'copyrigth' in config.SETUP_DATA  # Note: typo in original config
        assert config.SETUP_DATA['copyrigth'] == config.__copyright__
    
    def test_setup_data_has_features(self):
        """Test that SETUP_DATA contains features."""
        assert 'features' in config.SETUP_DATA
        assert config.SETUP_DATA['features'] == config.__features__
    
    def test_setup_data_completeness(self):
        """Test that SETUP_DATA has all expected keys."""
        expected_keys = [
            'title', 'version', 'author', 'url_github', 
            'url_twitter', 'url_linkedin', 'license', 
            'copyrigth', 'features'
        ]
        for key in expected_keys:
            assert key in config.SETUP_DATA, f"Missing key: {key}"
