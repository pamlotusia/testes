from src.Blog_api import Blog
import requests_mock
import pytest

@pytest.fixture
def mock_get():
    return [
        {'userId': 1, 'Id': 1, 'title': 'Titulo teste 1'
         , 'body': 'Conteudo do blog 1'},
        
        {'userId': 2, 'Id': 2, 'title': 'Titulo teste 2'
         , 'body': 'Teste de conteudo do blog 2'}
    ]
    
def teste_get(mock_get):
    with requests_mock.Mocker() as mocker:
        mocker.get("https://jsonplaceholder.typicode.com/posts", json=mock_get)
        blog = Blog()
        response = blog.get()
        print(type(response), type(mock_get))
        assert response == mock_get
        
def test_get_by_user_id(mock_get: list[dict[str]]):
    user_id = "1"
    expected_post = [post for post in mock_get if str(post['userId']) == user_id]
    with requests_mock.Mocker() as mocker:
        mocker.get(f"https://jsonplaceholder.typicode.com/posts/{user_id}", json=expected_post)
        blog = Blog()
        response = blog.get_by_user_id(user_id)
        assert response == expected_post
    
    
