import json
from difflib import get_close_matches

# LOoad the knowledge base from json
def load_knowledge_base(file_path: str) -> dict: # : shows the path of file and -> shows the return form of file in thius casse dict
    with open(file_path, 'r') as file: #r means read
        data: dict = json.load(file)
    return data

# to save data in json file 
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file: #w means write
        json.dump(data, file, indent=2) #indentation means space/gap    dump means to insert
    #DUMP DATA into the FILE with the space of 2

# To find the Best Match
def find_best_match(user_quetion: str, questions: list[str]) -> str | None :
    matches: list = get_close_matches(user_quetion, questions, n=1, cutoff=0.6 )
    return matches[0] if matches else None

# To get the answer of the question
def get_answer_for_question(question : str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    
# ALL THE INFO THAT CHAT BOT NEED IS DONE NOW WE HAVE TO GIVE HER THE INFO AKA SCRIPT
def chatbot():
    knowledge_base:dict = load_knowledge_base("knowledge_base.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer : str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: i dont know the answer. Can you teach me")
            new_answer: str = input('Type the answer or "skip" to skip')

            if new_answer.lower() != "skip" :
                knowledge_base["questions"].append({"questions": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json")
                print("Bot: Thankyou!<3 i learned a new response")

if __name__ == '__main__':
    chatbot()
