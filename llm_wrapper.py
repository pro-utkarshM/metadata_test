from transformers import AutoTokenizer, AutoModelForCausalLM

class LocalLLMWrapper:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
    
    def generate(self, prompt, max_length=500):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0][:max_length], skip_special_tokens=True)

