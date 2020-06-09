"""Файл для хранения JSON-схемы."""


SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": "W5",
            "status": "В обработке"
        }
    ],
    "required": [
        "id",
        "status"
    ],
    "additionalProperties": False,
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "string",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "W5"
            ]
        },
        "status": {
            "$id": "#/properties/status",
            "type": "string",
            "title": "The status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "В обработке"
            ]
        }
    }
}