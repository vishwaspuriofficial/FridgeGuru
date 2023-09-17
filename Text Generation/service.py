import bentoml

# text_generator_runner = bentoml.models.get("text-generation").to_runner()
# svc = bentoml.Service("text-generation", runners=[text_generator_runner])

# @svc.api(input=bentoml.io.Text(), output=bentoml.io.Text())
# def generate(instruction: str) -> str:
#     result = text_generator_runner.predict.run(instruction)

#     return result

from meals import PhilRunnable

phil_runner = bentoml.Runner(PhilRunnable)

svc = bentoml.Service("phil-service", runners=[phil_runner])

@svc.api(input=bentoml.io.Text(), output=bentoml.io.Text())
def inference(prompt: str) -> str:
  return phil_runner.generate.run(prompt)