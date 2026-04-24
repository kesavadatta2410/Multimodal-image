import json
import base64
import re
import time
from agent.agent import run_from_bytes


def _is_safe_filename(name: str) -> bool:
    """Allow alphanumerics, dash, underscore, dot, and spaces in filenames."""
    return bool(re.fullmatch(r"[\w\-\. ]+", name))


def _standard_response(task_type: str, result: dict) -> dict:
    """Wrap the raw result in a consistent envelope.
    Fields:
        - task_type: high‑level category of the request
        - confidence: placeholder for model confidence (None if not provided)
        - result: the raw dict returned by the agent
        - reasoning: optional human‑readable explanation (empty for now)
        - meta: ancillary metadata (timestamp)
    """
    return {
        "task_type": task_type,
        "confidence": None,
        "result": result,
        "reasoning": "",
        "meta": {"timestamp": int(time.time())},
    }


def handler(request):
    try:
        body = request.get_json()
        if not isinstance(body, dict):
            raise ValueError("Invalid JSON payload")
        # Validate image
        image_base64 = body.get("image")
        if not image_base64:
            raise ValueError("Missing 'image' field")
        try:
            base64.b64decode(image_base64, validate=True)
        except Exception:
            raise ValueError("Invalid Base64 image data")
        # Validate filename
        filename = body.get("filename", "image.jpg")
        if not _is_safe_filename(filename):
            raise ValueError("Invalid filename")
        # Validate instruction and context length
        instruction = body.get("instruction", "")
        context = body.get("context", "")
        if len(instruction) > 500:
            raise ValueError("Instruction too long (max 500 chars)")
        if len(context) > 500:
            raise ValueError("Context too long (max 500 chars)")
        # Decode image bytes
        image_bytes = base64.b64decode(image_base64)
        raw_result = run_from_bytes(
            image_bytes=image_bytes,
            filename=filename,
            instruction=instruction,
            context=context,
        )
        # Wrap result in standardized envelope
        response_body = _standard_response(task_type="analysis", result=raw_result)
        return {
            "statusCode": 200,
            "body": json.dumps(response_body),
        }
    except ValueError as ve:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(ve)}),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
