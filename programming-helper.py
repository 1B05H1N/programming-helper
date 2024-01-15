import os
import sys
from openai import OpenAI

# Ensure the OpenAI API key is set in environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit(1)

client = OpenAI(api_key=api_key)

# Function to generate secure coding guidelines
def get_programming_answer(question, language):
    try:
        # Construct the prompt for OpenAI's GPT-3 model
        prompt = (
            f"Provide an explanation and code example for the following programming question:\n"
            f"Question: {question}\n"
            f"Language: {language}\n"
            # You can add more context or specific questions here if needed.
        )


        # Generating the guidelines using OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are going to help generate secure coding guidelines."},
                {"role": "user", "content": prompt}
            ],
        )
        response_message = response.choices[0].message.content

        # Check if the response is empty
        if not response_message.strip():
            print("Received an empty response from OpenAI. Please try again.")
            return None

        return response_message.strip()
    except Exception as e:
        print(f"Error generating secure coding guidelines: {e}")
        return None
    
def main():
    # Prompt the user for the programming question and language
    question = input("Please enter your programming-related question: ")
    language = input("Please specify the programming language: ")

    # Get the programming-related answer with code examples
    answer = get_programming_answer(question, language)

    if answer:
        # Print the answer to the console
        print("\nProgramming Answer:")
        print(answer)
        print("\n\n")

        # Print or save the answer based on user preference
        output_format = input("Do you want to save the answer to a file? (yes/no): ").lower()
        if output_format == "yes":
            file_name = input("Enter the file name (e.g., answer.txt): ")
            try:
                with open(file_name, 'w') as file:
                    file.write(answer)
                print(f"Answer saved to {file_name}")
            except Exception as e:
                print(f"Error saving the answer to the file: {e}")
        else:
            # Print the answer to the console
            print("\nProgramming Answer:")
            print(answer)

if __name__ == "__main__":
    main()
