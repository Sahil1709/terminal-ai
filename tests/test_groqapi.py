import os
import pytest
from unittest.mock import patch, MagicMock
from terai.GroqApi import check_api_key, get_completions

def test_check_api_key_no_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    with pytest.raises(SystemExit):
        check_api_key()

def test_check_api_key_with_key(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test_api_key")
    with patch("terai.GroqApi.Groq") as MockGroq:
        check_api_key()
        MockGroq.assert_called_once_with(api_key="test_api_key")

def test_get_completions(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test_api_key")
    mock_client = MagicMock()
    mock_completion = MagicMock()
    mock_completion.choices[0].message.content = '{"commands": ["ls", "pwd"]}'
    mock_client.chat.completions.create.return_value = mock_completion

    with patch("terai.GroqApi.client", mock_client):
        commands = get_completions("List files and print working directory")
        assert commands == ["ls", "pwd"]

def test_get_completions_empty_response(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test_api_key")
    mock_client = MagicMock()
    mock_completion = MagicMock()
    mock_completion.choices[0].message.content = '{}'
    mock_client.chat.completions.create.return_value = mock_completion

    with patch("terai.GroqApi.client", mock_client):
        commands = get_completions("List files and print working directory")
        assert commands == ["Some error occurred. Please try again."]

def test_get_completions_invalid_json(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test_api_key")
    mock_client = MagicMock()
    mock_completion = MagicMock()
    mock_completion.choices[0].message.content = 'invalid json'
    mock_client.chat.completions.create.return_value = mock_completion

    with patch("terai.GroqApi.client", mock_client):
        commands = get_completions("List files and print working directory")
        assert commands == ["Some error occurred. Please try again."]

# def test_get_completions_no_api_key(monkeypatch):
#     monkeypatch.delenv("GROQ_API_KEY", raising=False)
#     with pytest.raises(SystemExit):
#         get_completions("List files and print working directory")
