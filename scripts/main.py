import json
import random
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

random.seed(time.time())

def green_text(text):
    return f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def red_text(text):
    return f"{Fore.RED}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def blue_text(text):
    return f"{Fore.BLUE}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def yellow_text(text):
    return f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def magenta_text(text):
    return f"{Fore.MAGENTA}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def load_questions(course_code, topic_code):
    filename = f"../materials/{course_code}/{topic_code}"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{red_text(f'❌ Error: lecture{topic_code}.json not found in materials/{course_code}/ directory.')}")
        print(f"{red_text('Please ensure the JSON file exists in the correct location.')}")
        return None
    except json.JSONDecodeError:
        print(f"{red_text(f'❌ Error: Invalid JSON in lecture{topic_code}.json.')}")
        return None

def display_course_selection_menu():
    def get_available_courses():
        import os
        materials_dir = "../materials"
        if not os.path.exists(materials_dir):
            return []
        return [d for d in os.listdir(materials_dir) if os.path.isdir(os.path.join(materials_dir, d))]

    available_courses = get_available_courses()
    if not available_courses:
        print(f"{red_text('❌ No courses available.')}")
        return

    print(f"{blue_text('Available courses:')}")
    for i, course in enumerate(available_courses, 1):
        print(f"  {i}. {course}")

    choice = input(f"{blue_text('Select a course (1-{len(available_courses)}):')} ")
    if not choice.isdigit() or not (0 <= int(choice) <= len(available_courses)):
        print(f"{red_text('❌ Invalid choice. Please try again.')}")
        return

    selected_course = available_courses[int(choice) - 1]
    print(f"{green_text(f'📚 You selected: {selected_course}')}")
    return selected_course

def display_topic_selection_menu(course_code):
    def get_available_topics(course_code):
        import os
        course_dir = f"../materials/{course_code}"
        if not os.path.exists(course_dir):
            return []
        return [f for f in os.listdir(course_dir) if f.endswith('.json')]

    available_topics = get_available_topics(course_code)
    if not available_topics:
        print(f"{red_text('❌ No topics available for this course.')}")
        return

    print(f"{blue_text('Available topics:')}")
    for i, topic in enumerate(available_topics, 1):
        print(f"  {i}. {topic}")

    choice = input(f"{blue_text('Select a topic (1-{len(available_topics)}):')} ")
    if not choice.isdigit() or not (0 <= int(choice) <= len(available_topics)):
        print(f"{red_text('❌ Invalid choice. Please try again.')}")
        return

    selected_topic = available_topics[int(choice) - 1]
    print(f"{green_text(f'📚 You selected: {selected_topic}')}")
    return selected_topic

def display_question(q):
    print(f"\n{blue_text('Question ' + str(q['id']) + ':')} {q['question']}")
    
    is_multiple = isinstance(q['correct'], list)
    if is_multiple:
        print(f"{magenta_text('(Multiple choice - select all correct answers)')}")
    
    options_list = list(q['options'].items())
    # print(f"{magenta_text('[DEBUG] Original order:')} {[item[0] for item in options_list]}")
    
    random.shuffle(options_list)
    # print(f"{magenta_text('[DEBUG] Shuffled order:')} {[item[0] for item in options_list]}")
    
    new_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Support more options
    answer_mapping = {}
    
    for i, (original_label, text) in enumerate(options_list):
        if i < len(new_labels):
            new_label = new_labels[i]
            answer_mapping[new_label] = original_label
            print(f"{yellow_text(new_label + ')')} {text}")
    
    print(magenta_text("-" * 60))
    return answer_mapping, is_multiple

def run_quiz(questions):
    if not questions:
        return
    
    for q in questions:
        answer_mapping, is_multiple = display_question(q)
        user_answer = input(f"{'Your answer (A/B/C/D):'} ").strip().upper()
        
        for string in user_answer:
            if string not in ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h"]:
                print(f"\n{red_text('❌ Invalid answer. Your answer is ' + string + '.')}\n")
                continue
            mapped_answer = answer_mapping[string]
            if mapped_answer == q['correct']:
                print(f"\n{green_text('✓ Correct! Great job.')}")
                print(f"{blue_text('Explanation:')} {q['explanation']}\n")
            else:
                correct_new_label = None
                for new_label, original_label in answer_mapping.items():
                    if original_label == q['correct']:
                        correct_new_label = new_label
                        break
                print(f"\n{red_text('✗ Incorrect.')} {yellow_text('The correct answer is ' + correct_new_label + '.')}")
                print(f"{blue_text('Explanation:')} {q['explanation']}\n")
        
        input(f"{magenta_text('Press Enter to continue to the next question...')}")
    
    print(f"\n{green_text('🎉 Quiz completed! Thanks for practicing.')}")

def main():
    print(f"\n{'='*60}")
    print(f"{green_text('🎓 Welcome to the Economics Quiz Simulator! 🎓')}")
    print(f"{'='*60}")
    
    while True:
        course_code = display_course_selection_menu()
        if not course_code:
            continue
        elif course_code == 0:
            print(f"{yellow_text('👋 Thanks for using the quiz! Goodbye!')}")
            return
        else:
            print(f"{green_text(f'📚 Course: {course_code.upper()}')}")
            topic_code = display_topic_selection_menu(course_code)
            if not topic_code:
                continue
            elif topic_code == 0:
                print(f"{yellow_text('Returning to course selection...')}")
                break
            else:
                print(f"{green_text(f'📚 Topic: {topic_code}')}")
                questions = load_questions(course_code, topic_code)
                if questions:
                    run_quiz(questions)
                else:
                    print(f"{red_text('Could not load questions. Please try again.')}")
                    continue

if __name__ == "__main__":
    main()