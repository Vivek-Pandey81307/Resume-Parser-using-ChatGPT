# Resume Parser using ChatGPT

This project uses OpenAI's GPT-4 to parse resumes and output them in JSON format.

## How to Use

1. Install the necessary packages:
    ```
    pip install openai
    ```

2. Add your OpenAI API key:
    ```python
    import openai

    openai.api_key = 'your-api-key'
    ```

3. Run the script with your resume text:
    ```python
    resume_text = """
    Your resume text here.
    """
    parsed_json = parse_resume_to_json(resume_text)
    print(parsed_json)
    ```

## Example Resume Text

