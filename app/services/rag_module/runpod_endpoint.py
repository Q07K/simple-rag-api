from openai import OpenAI


def serverless_client(endpoint_id: str, api_key: str) -> OpenAI:
    return OpenAI(
        base_url=f"https://api.runpod.ai/v2/{endpoint_id}/openai/v1",
        api_key=api_key,
    )
