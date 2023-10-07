from transformers import pipeline

def analysis_data(post):
    model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
    return model(post)
