# Code Generation Using Fine-Tuned T5 Model

This project showcases a **Streamlit-based application** that generates Python code snippets from user queries using a **fine-tuned T5 model**. The app provides an interactive interface for users to input natural language queries and receive accurate code snippets with a 95% success rate.

---

## Features

- **Natural Language to Code**: Generates Python code from user-provided queries using a fine-tuned T5 model.
- **Interactive User Interface**: Built with Streamlit for real-time input, output, and syntax highlighting.
- **Model Fine-Tuning**: The T5 model has been fine-tuned on domain-specific datasets for improved query understanding and code generation.
- **Performance Optimization**: Fast and efficient code generation with optimized tokenization and inference pipelines.

---

## Technologies Used

- **Python**
- **Streamlit**: For building the web application interface.
- **Hugging Face Transformers**: For utilizing and fine-tuning the T5 model.
- **PyTorch**: For deep learning model inference.

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SatchalPatil/Simple-Code-Generator.git
   cd Simple-Code-Generator

   pip install -r requirements.txt
   
   streamlit run app.py
## Example Usage
![Screenshot 2025-01-12 121221](https://github.com/user-attachments/assets/b6ec8e23-1099-4e92-ba5f-c2ba0639a130)

![Screenshot 2025-01-12 121022](https://github.com/user-attachments/assets/1f62a020-ed48-4893-91ed-1b717debaf40)

## Model Training
- The T5 model was fine-tuned on a dataset of Python coding tasks and queries.
- Fine-tuning was performed using the Hugging Face library and PyTorch.

## Contributing
- Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.


