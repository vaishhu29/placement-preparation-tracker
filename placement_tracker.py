import json
import os


class PlacementTracker:

    def __init__(self):

        self.topics = {
            "Python": {
                "Progress": 0,
                "Attempted": 0,
                "Correct": 0
            },
            "SQL": {
                "Progress": 0,
                "Attempted": 0,
                "Correct": 0
            },
            "DSA": {
                "Progress": 0,
                "Attempted": 0,
                "Correct": 0
            },
            "Aptitude": {
                "Progress": 0,
                "Attempted": 0,
                "Correct": 0
            },
            "OOP": {
                "Progress": 0,
                "Attempted": 0,
                "Correct": 0
            }
        }

        self.load_data()

    # Save data into JSON file
    def save_data(self):

        with open("placement_data.json", "w") as file:
            json.dump(self.topics, file, indent=4)

        print("Data saved successfully!")

    # Load data from JSON file
    def load_data(self):

        if os.path.exists("placement_data.json"):

            with open("placement_data.json", "r") as file:
                self.topics = json.load(file)

    # View all topics
    def view_topics(self):

        print("=" * 40)
        print("           TOPIC DETAILS")
        print("=" * 40)

        for topic, data in self.topics.items():

            attempted = data["Attempted"]
            correct = data["Correct"]
            wrong = attempted - correct

            if attempted > 0:
                accuracy = (correct / attempted) * 100
            else:
                accuracy = 0

            print("\n", topic)
            print("Progress  :", data["Progress"], "%")
            print("Attempted :", attempted)
            print("Correct   :", correct)
            print("Wrong     :", wrong)
            print("Accuracy  :", round(accuracy, 2), "%")

    # Update progress
    def update_progress(self):

        tname = input("Enter topic: ")

        if tname not in self.topics:
            print("Invalid topic")
            return

        try:
            progress = int(input("Enter progress: "))

        except ValueError:
            print("Invalid input! Please enter a number.")
            return

        if progress < 0 or progress > 100:
            print("Progress must be between 0 and 100.")
            return

        self.topics[tname]["Progress"] = progress

        self.save_data()

        print("Progress updated successfully!")

    # Update question performance
    def question_performance(self):

        tname = input("Enter topic: ")

        if tname not in self.topics:
            print("Invalid topic")
            return

        try:
            attempted = int(input("Enter questions attempted: "))
            correct = int(input("Enter correct answers: "))

        except ValueError:
            print("Invalid input! Please enter numbers.")
            return

        if attempted <= 0:
            print("Attempted questions must be greater than 0.")
            return

        if correct < 0 or correct > attempted:
            print("Invalid number of correct answers.")
            return

        self.topics[tname]["Attempted"] = attempted
        self.topics[tname]["Correct"] = correct

        self.save_data()

        wrong = attempted - correct
        accuracy = (correct / attempted) * 100

        print("Performance updated successfully!")
        print("Wrong Answers:", wrong)
        print("Accuracy:", round(accuracy, 2), "%")

    # Calculate overall progress
    def overall_progress(self):

        total = 0

        for data in self.topics.values():
            total += data["Progress"]

        average = total / len(self.topics)

        print("Overall Progress:", round(average, 2), "%")

    # Find weakest topic
    def weakest_topic(self):

        weakest = ""
        lowest = 101

        for topic, data in self.topics.items():

            if data["Progress"] < lowest:
                lowest = data["Progress"]
                weakest = topic

        print("Weakest Topic:", weakest)
        print("Progress:", lowest, "%")

    # Dashboard
    def dashboard(self):

        print("=" * 40)
        print("        PLACEMENT DASHBOARD")
        print("=" * 40)

        for topic, data in self.topics.items():

            attempted = data["Attempted"]
            correct = data["Correct"]
            wrong = attempted - correct

            if attempted > 0:
                accuracy = (correct / attempted) * 100
            else:
                accuracy = 0

            print("\n" + topic)
            print("Progress  :", data["Progress"], "%")
            print("Attempted :", attempted)
            print("Correct   :", correct)
            print("Wrong     :", wrong)
            print("Accuracy  :", round(accuracy, 2), "%")

        print("\n" + "-" * 40)

        total = 0

        for data in self.topics.values():
            total += data["Progress"]

        overall = total / len(self.topics)

        weakest = ""
        lowest = 101

        for topic, data in self.topics.items():

            if data["Progress"] < lowest:
                lowest = data["Progress"]
                weakest = topic

        print("Overall Progress :", round(overall, 2), "%")
        print("Weakest Topic    :", weakest)

        print("-" * 40)

    # Study recommendation
    def study_recommendation(self):

        weakest = ""
        lowest = 101

        for topic, data in self.topics.items():

            if data["Progress"] < lowest:
                lowest = data["Progress"]
                weakest = topic

        data = self.topics[weakest]

        attempted = data["Attempted"]
        correct = data["Correct"]

        if attempted > 0:
            accuracy = (correct / attempted) * 100
        else:
            accuracy = 0

        print("=" * 40)
        print("       STUDY RECOMMENDATION")
        print("=" * 40)

        print("Focus Topic :", weakest)
        print("Progress    :", lowest, "%")
        print("Accuracy    :", round(accuracy, 2), "%")

        if lowest < 40:

            print("Recommendation: Focus strongly on", weakest)
            print("Target: Practice at least 20 questions.")

        elif lowest < 70:

            print("Recommendation: Give more practice to", weakest)
            print("Target: Practice at least 15 questions.")

        else:

            print("Recommendation: Revise", weakest)
            print("Target: Practice at least 10 questions.")

    # Main menu
    def run(self):

        while True:

            print("\n" + "=" * 40)
            print("      PLACEMENT PREPARATION TRACKER")
            print("=" * 40)

            print("1. Dashboard")
            print("2. View Topics")
            print("3. Update Progress")
            print("4. Overall Progress")
            print("5. Weakest Topic")
            print("6. Update Question Performance")
            print("7. Study Recommendation")
            print("8. Exit")

            try:
                choice = int(input("Enter your choice: "))

            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 1:

                self.dashboard()

            elif choice == 2:

                self.view_topics()

            elif choice == 3:

                self.update_progress()

            elif choice == 4:

                self.overall_progress()

            elif choice == 5:

                self.weakest_topic()

            elif choice == 6:

                self.question_performance()

            elif choice == 7:

                self.study_recommendation()

            elif choice == 8:

                print("Thank you for using Placement Preparation Tracker!")
                break

            else:

                print("Invalid choice! Please select 1-8.")


# Create object
tracker = PlacementTracker()

# Start program
tracker.run()