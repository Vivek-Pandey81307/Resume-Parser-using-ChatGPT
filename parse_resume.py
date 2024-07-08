import openai

def parse_resume_to_json(resume_text):
    prompt = f"""
    You are an AI assistant. Your task is to parse the following resume content and output it in JSON format. The JSON should have keys such as 'Name', 'Contact Information', 'Summary', 'Experience', 'Education', 'Skills', and 'Projects'. Here is the resume content:

    {resume_text}

    Output the JSON format of this resume.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message['content']

# Example usage
resume_text = """
John Doe
Email: john.doe@example.com
Phone: +123456789
LinkedIn: linkedin.com/in/johndoe

Summary:
Highly skilled software developer with over 5 years of experience in full stack development, specializing in Python and JavaScript frameworks. Adept at problem-solving and leading projects from conception to deployment.

Experience:
Software Developer, TechCorp, 2019 - Present
- Developed and maintained web applications using React and Node.js.
- Led a team of 5 developers in Agile methodology.

Junior Developer, WebSolutions, 2017 - 2019
- Assisted in the development of e-commerce platforms.
- Implemented RESTful APIs and integrated third-party services.

Education:
B.Sc. in Computer Science, University of Tech, 2013 - 2017

Skills:
- Programming Languages: Python, JavaScript, C++
- Frameworks: React, Node.js, Django
- Tools: Git, Docker, Jenkins

Projects:
- Project A: Developed a machine learning model to predict customer churn.
- Project B: Created a mobile app for task management using React Native.
"""

parsed_json = parse_resume_to_json(resume_text)
print(parsed_json)
