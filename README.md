# Python Message App

A Flask web application that fetches and displays personalized messages based on user personality data retrieved from external APIs. Users can view and accept messages.

## Features

- **Fetch Personality**: Retrieves user personality data using a customer number.
- **Fetch Messages**: Displays customized messages tailored to the user’s personality.
- **Accept Messages**: Allows users to accept messages, with acceptance data sent to an external API.

## Requirements

- **Python**: Version 3.7 or higher
- **Flask** and **Requests**: Python libraries for web handling and HTTP requests

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-message-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd python-message-app
   ```

3. Install dependencies:
   ```bash
   pip install Flask requests
   ```

## Configuration

Update API URLs in `app.py` if different from the defaults:

```python
MESSAGES_API_URL = 'http://localhost:8098/invocations'
PERSONALITY_API_URL = 'http://localhost:8092/invocations'
ACCEPTANCE_API_URL = 'http://localhost:8098/response'
```

## Usage

1. **Run the App**:
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000` in a web browser.


2. **Fetch Messages**:
   - Enter a customer number and click **Fetch Messages** to load messages.


3. **Accept Messages**:
   - Click **Accept** on a message to send acceptance data to the API.

## Troubleshooting

- **API Issues**: Ensure the API servers are running and accessible.
- **Error Logs**: Run Flask in debug mode (`app.run(debug=True)`) to view detailed logs.

## License

This project is licensed under the MIT License.

For questions or issues, please contact [amy@ecosystem.ai](mailto:amy@ecosystem.ai).
