### Setup

```
conda create -n algo python=3.10 -y
conda activate algo
pip install -r requirements.txt
```

### Model Evaluation

Run zero-shot evaluation with LLMs like [Gemini Pro](https://ai.google.dev/tutorials/python_quickstart?hl=en)
or [GPT-4(V)](https://platform.openai.com/docs/guides/vision)

The currently supported model names are `[gemini_vision, openai_vision]`

```
# Run evaluation on the "wheel_of_fortune" puzzle with Gemini Pro Vision
python main.py evaluate_multi_choice data/wheel_of_fortune.json --model_name gemini_vision
[13:45<00:00,  8.25s/it, score=0.24]

# Run evaluation on the "wheel_of_fortune" puzzle with GPT-4V
python main.py evaluate_multi_choice data/wheel_of_fortune.json --model_name openai_vision
[31:15<00:00, 18.76s/it, score=0.29]

# Run evaluation on the "wheel_of_fortune" puzzle with LLaVA
python main.py evaluate_multi_choice data/wheel_of_fortune.json --model_name llava
[21:33<00:00, 12.94s/it, score=0.27]
```

### API Setup

Gemini Pro (multimodal): Please create a file named `gemini_vision_info.json`

```
{"engine": "gemini-pro-vision", "key": "your_api_key"}
```

GPT-4V (multimodal): Please create a file named `openai_vision_info.json`

```
{"engine": "gpt-4-vision-preview", "key": "your_api_key"}
```