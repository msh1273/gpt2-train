# gpt2-train

[![Run on Ainize](https://ainize.ai/static/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ainize-bot/gpt2-train)

Auto-generated github repository by [Ainize Teachable NLP](https://ainize.ai/teachable-nlp)

## Health Check
Using `curl` in the terminal:
```
$ curl --request GET 'https://train-3k8pc1oyza1m0s669qpg-gpt2-train-teachable-ainize.endpoint.ainize.ai/ping'
{
  "status": "Healthy"
}
```

## Prediction Test

### Pre-processing for API
To use the API, the sentence must be converted into a vector form.

[Web](https://master-gpt2-text2vec-shyun-comcom.endpoint.ainize.ai/)
or using `curl` in the terminal:
```
$ curl --request POST 'https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/preprocess' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"context": "there is a boy"
	}'

"[8117, 318, 257, 2933]"
```

### Prediction
Using `curl` in the terminal:
```
$ curl --request POST 'https://train-3k8pc1oyza1m0s669qpg-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-en-small-finetune' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "text": [3666, 1438, 318, 14200, 11, 314, 16486, 1850, 287, 13851, 3783],
    "num_samples": 5,
    "length": 8
  }'

[
  [
    3666, 1438, 318, 14200, 11, 314, 16486, 1850, 287, 13851, 3783, 11, 314, 1101, 422, 262, 1294, 11, 523
  ],
  ...,
  [
    3666, 1438, 318, 14200, 11, 314, 16486, 1850, 287, 13851, 3783, 379, 262, 2059, 286, 520, 26414, 11, 543
  ]
]
``` 
