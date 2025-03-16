from openai import Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

from app.config import env
from app.services.rag_module.runpod_endpoint import serverless_client


def tulu3_8b(
    temperature: float,
    max_tokens: int,
    messages: list[dict[str]],
) -> Stream[ChatCompletionChunk]:
    client = serverless_client(
        endpoint_id=env.TULU3_ID,
        api_key=env.TULU3_KEY,
    )
    return client.chat.completions.create(
        model="allenai/Llama-3.1-Tulu-3-8B",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,
    )
