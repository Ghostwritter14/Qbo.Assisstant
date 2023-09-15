import pytest
from unittest.mock import Mock, mock_open, patch
from main import Assistant
from datetime import datetime


def test_create_note():
    assistant = Assistant()

    # Mocking the open function
    m = mock_open()
    with patch('builtins.open', m):
        response = assistant.create_note("This is a test note.")
    assert response == "Note added: This is a test note."
    m.assert_called_once_with(datetime.today().strftime('%Y-%m-%d') + ".txt", 'a')


def test_read_notes():
    assistant = Assistant()

    # Mocking the open function to simulate reading a file
    m = mock_open(read_data="This is a test note.\n")
    with patch('builtins.open', m):
        response = assistant.read_notes()
    assert response == "This is a test note.\n"


def test_get_news():
    assistant = Assistant()

    # Mocking show_news method
    mock_show_news = Mock()
    assistant.news_scraper.show_news = mock_show_news
    response = assistant.get_news()
    assert response == "Here are the latest news."
    mock_show_news.assert_called_once()


def test_ask_chatbot():
    assistant = Assistant()

    # Mocking get_response method
    mock_get_response = Mock(return_value="This is a test response.")
    assistant.chatbot.get_response = mock_get_response
    response = assistant.ask_chatbot("What is a unit test?")
    assert response == "This is a test response."
    mock_get_response.assert_called_once_with("What is a unit test?")
