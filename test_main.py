import pytest
from main import app
from httpx import AsyncClient


@pytest.mark.anyio
async def test1():
    async with AsyncClient(app=app, base_url="http://test") as client:
        get_response = await client.get("/")
    assert get_response.status_code == 200
    assert get_response.text == 'HELLO'


@pytest.mark.anyio
async def test2():
    message = "Hello, World"
    async with AsyncClient(app=app, base_url="http://test") as client:
        post_response = await client.post(f"/?message={message}")

    assert post_response.status_code == 200
    assert post_response.json() == {"data": message}