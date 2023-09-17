# import transformers
# import bentoml

# model= "microsoft/phi-1_5"
# task = "text-generation"

# bentoml.transformers.save_model(
#     task,
#     transformers.pipeline(task, model=model, trust_remote_code=True),
#     metadata=dict(model_name=model),
# )


import bentoml, torch, transformers

class PhilRunnable(bentoml.Runnable):
  SUPPORTED_RESOURCES = ("nvidia.com/gpu", "cpu")
  SUPPORTS_CPU_MULTI_THREADING = True

  def __init__(self):
    self.model = bentoml.transformers.load_model("microsoft--phil-1_5", trust_remote_code=True)
    self.tokenizer = bentoml.transformers.load_model("microsoft--phil-1_5-tokenizer", trust_remote_code=True)

  @bentoml.Runnable.method(batchable=False)
  def generate(self, prompt: str) -> str:
    with torch.inference_mode():
      inputs = self.tokenizer(prompt, return_tensors="pt", return_attention_mask=False)
      outputs = self.model.generate(**inputs, max_length=200)
      return self.tokenizer.batch_decode(outputs)[0]