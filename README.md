# Pixlab backend for Image Generation

This is a Django application, which generate ai image using [Replicate API](https://replicate.com).
You can see documentation on [here](https://replicate.com/docs])

## Get Started

### 1. Install virtual environment

```
py -m venv env
```

### 2. Install necessary packages

```
pip install -r requirements.txt
```

### 3. Run a server

```
py manage.py runserver
```

#### Code example:

```
output = replicate.run(
    "lucataco/realistic-vision-v5.1:2c8e954decbf70b7607a4414e5785ef9e4de4b8c51d50fb8b8b349160e0ef6bb",
    input={
        "seed": seed,
        "steps": 20,
        "width": width,
        "height": height,
        "prompt": prompt,
        "guidance": 5,
        "scheduler": "EulerA",
        "negative_prompt": negativePrompt
    }
)
```
