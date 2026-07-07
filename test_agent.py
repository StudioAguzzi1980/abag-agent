"""
Tests for the ABAG AI Business Advisor Agent.
"""

import importlib
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


REPO_ROOT = Path(__file__).parent


def _import_agent():
    """Import the agent module, re-importing fresh each time."""
    if "agent" in sys.modules:
        del sys.modules["agent"]
    sys.path.insert(0, str(REPO_ROOT))
    return importlib.import_module("agent")


class TestSystemPrompt:
    def test_system_prompt_file_exists(self):
        assert (REPO_ROOT / "system_prompt.txt").exists()

    def test_load_system_prompt_returns_string(self):
        agent = _import_agent()
        prompt = agent.load_system_prompt()
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_system_prompt_contains_abag_identity(self):
        agent = _import_agent()
        prompt = agent.load_system_prompt()
        assert "ABAG" in prompt or "American Business Advisory Group" in prompt

    def test_system_prompt_contains_mission(self):
        agent = _import_agent()
        prompt = agent.load_system_prompt()
        assert "Italy" in prompt or "Europe" in prompt

    def test_system_prompt_contains_specializations(self):
        agent = _import_agent()
        prompt = agent.load_system_prompt()
        specializations = [
            "Market entry",
            "Tax",
            "Banking",
        ]
        for keyword in specializations:
            assert keyword in prompt, f"Expected '{keyword}' in system prompt"

    def test_system_prompt_contains_linkedin_guidelines(self):
        agent = _import_agent()
        prompt = agent.load_system_prompt()
        assert "LinkedIn" in prompt

    def test_system_prompt_no_invented_rules_disclaimer(self):
        agent = _import_agent()
        prompt = agent.load_system_prompt()
        assert "uncertain" in prompt or "invent" in prompt


class TestCreateClient:
    def test_create_client_raises_without_api_key(self):
        agent = _import_agent()
        with patch.dict("os.environ", {}, clear=True):
            if "OPENAI_API_KEY" in __import__("os").environ:
                pytest.skip("OPENAI_API_KEY is set in environment")
            with pytest.raises(ValueError, match="OPENAI_API_KEY"):
                agent.create_client()

    def test_create_client_succeeds_with_api_key(self):
        agent = _import_agent()
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key-123"}):
            client = agent.create_client()
            assert client is not None


class TestGetSingleResponse:
    def _make_mock_response(self, content: str):
        mock_response = MagicMock()
        mock_response.choices[0].message.content = content
        return mock_response

    def test_get_single_response_calls_openai(self):
        agent = _import_agent()
        expected = "ABAG advisor response."
        mock_response = self._make_mock_response(expected)

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            with patch("agent.OpenAI") as mock_openai_cls:
                mock_client = MagicMock()
                mock_openai_cls.return_value = mock_client
                mock_client.chat.completions.create.return_value = mock_response

                result = agent.get_single_response("Hello")

        assert result == expected

    def test_get_single_response_sends_system_prompt(self):
        agent = _import_agent()
        mock_response = self._make_mock_response("OK")

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            with patch("agent.OpenAI") as mock_openai_cls:
                mock_client = MagicMock()
                mock_openai_cls.return_value = mock_client
                mock_client.chat.completions.create.return_value = mock_response

                agent.get_single_response("Tell me about Italy.")

                call_kwargs = mock_client.chat.completions.create.call_args
                messages = call_kwargs.kwargs["messages"]
                system_messages = [m for m in messages if m["role"] == "system"]
                assert len(system_messages) == 1
                assert (
                    "ABAG" in system_messages[0]["content"]
                    or "American Business" in system_messages[0]["content"]
                )

    def test_get_single_response_includes_user_message(self):
        agent = _import_agent()
        mock_response = self._make_mock_response("Response")
        user_msg = "How do I form a company in Italy?"

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            with patch("agent.OpenAI") as mock_openai_cls:
                mock_client = MagicMock()
                mock_openai_cls.return_value = mock_client
                mock_client.chat.completions.create.return_value = mock_response

                agent.get_single_response(user_msg)

                call_kwargs = mock_client.chat.completions.create.call_args
                messages = call_kwargs.kwargs["messages"]
                user_messages = [m for m in messages if m["role"] == "user"]
                assert len(user_messages) == 1
                assert user_messages[0]["content"] == user_msg

    def test_get_single_response_uses_default_model(self):
        agent = _import_agent()
        mock_response = self._make_mock_response("Response")

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            with patch("agent.OpenAI") as mock_openai_cls:
                mock_client = MagicMock()
                mock_openai_cls.return_value = mock_client
                mock_client.chat.completions.create.return_value = mock_response

                agent.get_single_response("Hello")

                call_kwargs = mock_client.chat.completions.create.call_args
                model = call_kwargs.kwargs.get("model")
                assert model == "gpt-4o"

    def test_get_single_response_accepts_custom_model(self):
        agent = _import_agent()
        mock_response = self._make_mock_response("Response")

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            with patch("agent.OpenAI") as mock_openai_cls:
                mock_client = MagicMock()
                mock_openai_cls.return_value = mock_client
                mock_client.chat.completions.create.return_value = mock_response

                agent.get_single_response("Hello", model="gpt-4-turbo")

                call_kwargs = mock_client.chat.completions.create.call_args
                model = call_kwargs.kwargs.get("model")
                assert model == "gpt-4-turbo"
