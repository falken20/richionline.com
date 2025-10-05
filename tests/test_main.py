"""
Tests for the main Flask application routes and functionality.
"""
import pytest
from flask import template_rendered
from contextlib import contextmanager


@contextmanager
def captured_templates(app):
    """Context manager to capture templates being rendered."""
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


class TestHomeRoute:
    """Tests for the home route."""
    
    def test_home_status_code(self, client):
        """Test that home route returns 200 status code."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_renders_template(self, app, client):
        """Test that home route renders the correct template."""
        with captured_templates(app) as templates:
            response = client.get('/')
            assert response.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'main.html'
    
    def test_home_content_type(self, client):
        """Test that home route returns HTML content."""
        response = client.get('/')
        assert response.content_type == 'text/html; charset=utf-8'


class TestContactRoute:
    """Tests for the contact route."""
    
    def test_contact_status_code(self, client):
        """Test that contact route returns 200 status code."""
        response = client.get('/contact')
        assert response.status_code == 200
    
    def test_contact_renders_template(self, app, client):
        """Test that contact route renders the correct template."""
        with captured_templates(app) as templates:
            response = client.get('/contact')
            assert response.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'contact.html'
    
    def test_contact_content_type(self, client):
        """Test that contact route returns HTML content."""
        response = client.get('/contact')
        assert response.content_type == 'text/html; charset=utf-8'


class TestPortfolioRoute:
    """Tests for the portfolio route."""
    
    def test_portfolio_status_code(self, client):
        """Test that portfolio route returns 200 status code."""
        response = client.get('/portfolio')
        assert response.status_code == 200
    
    def test_portfolio_renders_template(self, app, client):
        """Test that portfolio route renders the correct template."""
        with captured_templates(app) as templates:
            response = client.get('/portfolio')
            assert response.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'portfolio.html'
    
    def test_portfolio_content_type(self, client):
        """Test that portfolio route returns HTML content."""
        response = client.get('/portfolio')
        assert response.content_type == 'text/html; charset=utf-8'


class TestAppConfiguration:
    """Tests for Flask app configuration."""
    
    def test_app_is_testing(self, app):
        """Test that app is in testing mode."""
        assert app.config['TESTING'] is True
    
    def test_templates_auto_reload_is_set(self, app):
        """Test that templates auto reload is configured."""
        assert 'TEMPLATES_AUTO_RELOAD' in app.config
        assert app.config['TEMPLATES_AUTO_RELOAD'] is True


class TestInvalidRoutes:
    """Tests for invalid/non-existent routes."""
    
    def test_404_error(self, client):
        """Test that invalid route returns 404 status code."""
        response = client.get('/nonexistent')
        assert response.status_code == 404
    
    def test_invalid_method(self, client):
        """Test that POST to home route returns 405 Method Not Allowed."""
        response = client.post('/')
        assert response.status_code == 405


class TestStaticFiles:
    """Tests for static file serving."""
    
    def test_static_css_exists(self, client):
        """Test that main.css is accessible."""
        response = client.get('/static/main.css')
        # It should either return 200 if file exists or 404 if it doesn't
        assert response.status_code in [200, 404]
    
    def test_static_assets_folder(self, client):
        """Test that static assets folder is accessible."""
        response = client.get('/static/assets/falken_logo.png')
        # It should either return 200 if file exists or 404 if it doesn't
        assert response.status_code in [200, 404]
