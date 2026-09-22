import requests


def query_style_sense(
    backend_url: str,
    question: str,
    image_file,
):
    response = requests.post(
        f"{backend_url}/query/image",
        files={
            "image": (
                image_file.name,
                image_file,
                image_file.type,
            )
        },
        data={
            "question": question,
        },
        timeout=120,
    )

    response.raise_for_status()

    return response.json()