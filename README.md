# Bookstore Django Application

This is a simple Django web application for managing a bookstore. It allows users to view a list of books and their details.

## Installation

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed pip.
- You have installed virtualenv.

Follow these steps to install the application:

1. Clone the repository.
   ```shell
   git clone https://github.com/princessemmaaa/bookstore.git
   ```
2. Navigate to the project directory.
   ```shell
   cd bookstore
   ```
3. Create a virtual environment and activate it.
   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required packages.
   ```shell
   pip3 install -r requirements.txt
   ```
5. Apply the migrations.
   ```shell
   python3 manage.py migrate
   ```
6. Run the development server.
   ```shell
   python3 manage.py runserver
   ```

The application will be available at `http://localhost:8000`.

## Usage

Here are some of the things you can do with this application:

- View the list of books at `http://localhost:8000/books`.
- View the details of a specific book at `http://localhost:8000/books/<book_id>`.

## Contributing

If you want to contribute to this project, please create a new issue or open a pull request.

## License

This project is licensed under the MIT License.

## Contact

If you want to contact me, you can reach me at <loveydoveymedia@gmail.com>.
