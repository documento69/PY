# Simple Python sample about the world

def world_facts():
    # Some facts about the world
    facts = [
        "The Earth is the only planet in our solar system known to support life.",
        "Approximately 71% of Earth's surface is covered by water.",
        "Mount Everest is the highest mountain on Earth, standing at 8,848 meters (29,029 feet).",
        "The world's population is over 8 billion people.",
        "The Amazon Rainforest produces 20% of the world's oxygen.",
        "The Great Wall of China is over 13,000 miles long."
    ]
    
    print("Here are some interesting facts about the world:")
    for fact in facts:
        print(f"- {fact}")

# Call the function
world_facts()
