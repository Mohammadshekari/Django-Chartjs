# Django + Chart.js Project

This is a very simple Django project designed to use Chart.js for creating dynamic charts and collect data directly from
Django views without any extra requirements.

<img src="https://github.com/Mohammadshekari/Django-Chartjs/blob/main/screenshots/img.png?raw=true" width="600">

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Django 3.x or later

## Installation

Follow these steps to get the app up and running on your local machine.

### Backend Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Mohammadshekari/Django-Chartjs.git
   cd django-chartjs
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```
7. Navigate to `http://127.0.0.1:8000` in your web browser.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Chart.js](https://www.chartjs.org/)

---

Happy coding! 🎉