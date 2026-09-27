import os
from mem0 import Memory

# Initialize Mem0
try:
    m = Memory()
except Exception as e:
    print(f"Error initializing Mem0: {e}")
    m = None

def main():
    print("========================================")
    print("  Welcome to Mem0 Agentic CLI Memory!   ")
    print("========================================")
    print("Type anything and the agent will remember it. Type 'exit' to quit.\n")

    # Define a unique user ID
    user_id = "default_user"

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Agent: Goodbye! Take care.")
                break
            
            if not user_input.strip():
                continue

            # 1. Store user input into Mem0 memory
            if m:
                m.add(user_input, user_id=user_id)

            # 2. Fetch all memories associated with this user
            relevant_memories = []
            if m:
                memories_data = m.get_all(user_id=user_id)
                if isinstance(memories_data, list):
                    relevant_memories = [mem.get('memory', '') for mem in memories_data]
                elif isinstance(memories_data, dict) and 'results' in memories_data:
                    relevant_memories = [mem.get('memory', '') for mem in memories_data['results']]

            # 3. Simple agent response
            print(f"Agent: I have remembered your input: '{user_input}'")
            
            if relevant_memories:
                print(f"       [Total saved memories: {len(relevant_memories)}]")

        except KeyboardInterrupt:
            print("\nAgent: Goodbye!")
            breaks

if __name__ == "__main__":
    main()