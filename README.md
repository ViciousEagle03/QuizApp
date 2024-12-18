## Installation

To get the project up and running on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-quiz-app.git
   cd django-quiz-app
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv djangoenv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Load the quiz questions:
   ```bash
   python manage.py load_questions
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

Your app will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).



![Screenshot from 2024-12-19 04-33-27](https://github.com/user-attachments/assets/51943e98-dc2d-4a36-9f7e-0d2989d91352)

![Screenshot from 2024-12-19 04-22-57](https://github.com/user-attachments/assets/53e67059-8bc2-4678-b4aa-61f80e7fc570)

![Screenshot from 2024-12-19 04-29-44](https://github.com/user-attachments/assets/8a00b9c5-11c9-4b2f-9405-a7b4b017544f)




