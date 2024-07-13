import random
import json
class player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def get_random_question(used_questions):
    with open(r"C:\Users\The user\Desktop\dev\python\my-first-repo\michael2\json.txt", 'r', encoding='utf-8') as f:
        data = json.load(f)
    available_questions = [q for q in data if json.dumps(q) not in used_questions]
    if not available_questions:
        print("all qustions was qusiut")
        return None
    random_question = random.choice(available_questions)
    used_questions.add(json.dumps(random_question))
    return random_question

def main(player, all_dict_question, set_of_wrong_answers):
    print(all_dict_question['question'])
    print("תשובות שגויות", set_of_wrong_answers)
    print(all_dict_question['options'])
    answer = int(input("תבחר מספר תשובה"))
    if answer in set_of_wrong_answers:
        print("התשובה הזו נוסתה")
    elif answer != int(all_dict_question["correct_answer"]):
        print("טעית")
        return ("you are wrong", answer)
    elif answer == int(all_dict_question["correct_answer"]):
        player.score += 1
        print("תשובה מעולה")
        return "great answer"

players = []
nums_of_players = int(input("כמה שחקנים אתם"))
for i in range(nums_of_players):
    name = input(f"הכנס את השם של שחקן {i + 1} ")
    players.append(player(name))
used_questions = set()
all_dict_question = get_random_question(used_questions)
set_of_wrong_answers = set()
while all_dict_question:
    for i in players:
        MAIN = main(i, all_dict_question, set_of_wrong_answers)
        if MAIN == "great answer":
            all_dict_question = get_random_question(used_questions)
            if not all_dict_question:
                break
            set_of_wrong_answers = set()
        elif MAIN[0] == "you are wrong":
            set_of_wrong_answers.add(MAIN[1])
for i in players:
    print(i.name,i.score)