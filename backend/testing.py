from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load pretrained model and tokenizer from Hugging Face Hub
model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

model.eval()

# Example sentences to classify
sentences = [
    "I love this product, it's amazing!",
    "This is the worst experience I've ever had.",
    "The service was okay, nothing special.",
    "Absolutely fantastic work!",
    "I'm not happy with the delivery.",
]

# Tokenize sentences
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1) + 1  # labels from 1 to 5 for this model

# Display predictions
for sentence, pred in zip(sentences, predictions):
    print(f'Sentence: "{sentence}" --> Predicted Sentiment Score: {pred.item()}')
