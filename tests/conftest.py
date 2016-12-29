import pytest

from tldr import create_app


@pytest.fixture(scope='module')
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {
        'TESTING': True,
    }
    app = create_app(__name__, config=settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture
def testapp(app):
    return app.test_client()
