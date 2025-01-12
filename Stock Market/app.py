import re
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the financial analysis agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Use tables to display data."],
    show_tool_calls=True,  
    markdown=True, 
    debug_mode=True,
)

# Function to simulate playground-like interaction
def simulate_playground(agent, query):
    try:
        # Regular expression to detect stock symbols like TSLA, AAPL, GOOGL, etc.
        valid_symbols = re.findall(r'\b[A-Z]{1,5}\b', query)  
        if valid_symbols:
            # Get the response from the agent
            response = agent.print_response(query)
            if response is None:
                return "No response generated. Check the query and try again."
            return response  
        else:
            return "No valid stock symbols detected. Please enter valid stock symbols like TSLA, AAPL, or MSFT."
    except Exception as e:
        return f"Error occurred: {str(e)}" 

# Main interaction loop for command-line interface
if __name__ == "__main__":
    print("AI Agent Playground")
    print("Example query: 'Summarize and compare analyst recommendations and fundamentals for ABC and XYZ. Show in tables.'")
    
    while True:
        # Allow the user to enter a query
        user_input = input("Enter your query (or type 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("Exiting the AI Agent Playground.")
            break
        
        # Get the response from the agent
        result = simulate_playground(agent, user_input)
        
        print(f"Response:\n{result}\n")
