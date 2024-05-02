import os
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import replicate

def index(request):
    data = json.loads(request.body)
    os.environ["REPLICATE_API_TOKEN"]="r8_YK4XFXhbs3885x3WVw2Jc4ZYR0QYoCm4Juzsr"
    [seed, width, height, prompt, negativePrompt] = list(data.values())
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
    return JsonResponse({"data": output})