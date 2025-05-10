import cohere

# Initialize Cohere client with your API key
co = cohere.Client('WOxUi2MYB43qjCA6WkqlhHWbriVlhhYeLwB8aVDC')  # Replace with your actual API key

# Define your input ingredients
ingredients = "chicken, garlic, and tomatoes"

# Create a message prompt
prompt = f"Create a detailed cooking recipe using the following ingredients: {ingredients}"

# Use the chat endpoint instead of generate for 'command-r'
response = co.chat(
    model='command-r',
    message=prompt
)

# Print the generated recipe
print("Recipe:\n")
print(response.text.strip())
