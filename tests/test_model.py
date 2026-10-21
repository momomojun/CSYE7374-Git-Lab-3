from src import model


def test_generate_text_returns_text(monkeypatch):
    class FakeTokenizer:
        eos_token_id = 0

        def __call__(self, prompt, return_tensors):
            assert prompt == "hello"
            assert return_tensors == "pt"
            return {"input_ids": [1]}

        def decode(self, output_ids, skip_special_tokens):
            return "hello response"

    class FakeModel:
        def generate(self, **kwargs):
            assert kwargs["input_ids"] == [1]
            return [[1, 2]]

    monkeypatch.setattr(model, "load_tokenizer", lambda name: FakeTokenizer())
    monkeypatch.setattr(model, "load_model", lambda name: FakeModel())

    assert model.generate_text("hello") == "hello response"


def test_generate_text_rejects_blank_prompt():
    try:
        model.generate_text(" ")
    except ValueError:
        pass
    else:
        raise AssertionError("blank prompts must be rejected")
