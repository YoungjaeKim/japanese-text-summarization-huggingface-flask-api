from flask import Flask, request
from transformers import AutoTokenizer, BartForConditionalGeneration

app = Flask(__name__)

# Load pre-trained model and tokenizer
model = BartForConditionalGeneration.from_pretrained('ku-nlp/bart-large-japanese')
tokenizer = AutoTokenizer.from_pretrained('ku-nlp/bart-large-japanese')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    file = request.files['file']
    lines = file.read().decode('utf-8').splitlines()

    summaries = []
    for text in lines:
        # Tokenize the text
        inputs = tokenizer(text, max_length=1024, return_tensors='pt')

        # Generate summary
        summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=5, early_stopping=True)
        summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]

        summaries.append(summary[0])

    return {"summaries": summaries}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
