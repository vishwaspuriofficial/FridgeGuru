from transformers import pipeline
def textGenerator(text):
    print(text[2])
    gen = pipeline('text-generation', model ='EleutherAI/gpt-neo-125M')
    content = f"Hi {text[0]}, here is the top 3 {text[3]} recipes you can make for {text[1]} portions using {text[2]}"
    context = f"Write 3 recipes using {text[2]} for {text[1]} of portions. The preferred food is {text[3]} Format each recipe name as an header and numbered step-by-step instructions following. Make sure the total number of lines for each recipe is less than 6. Assume you can also use salt, pepper and water. "
    output = gen(context, max_length=100, do_sample=True, temperature=0.9)
    print([content]+output)
    return [content]+output

if __name__ == '__main__':
    textGenerator(text)