# GenGameForge API

Welcome to the GenGameForge API documentation! This API allows you to leverage AI-powered content generation to enhance your game development process.

## API Endpoints

### Generate Character

Generate a character for your game.

- **Endpoint:** `/generate/character`
- **HTTP Method:** POST
- **Request Format:** JSON
- **Request Body:**
  ```json
  {
    "params": { ... }
  }
- **Response Format:** JSON
- **Response Body:**
  ```json
  {
    "message": "Character generated successfully.",
    "item": { /* Placeholder for generated character */ }
  }

### Generate Item

Generate an item for your game.

- **Endpoint:** `/generate/item`
- **HTTP Method:** POST
- **Request Format:** JSON
- **Request Body:**
  ```json
  {
    "params": { ... }
  }
- **Response Format:** JSON
- **Response Body:**
  ```json
  {
    "message": "Item generated successfully.",
    "item": { /* Placeholder for generated item */ }
  }

## Getting Started

To start using the GenGameForge API, follow these steps:

1. Clone the GenGameForge repository to your local machine.
2. Navigate to the `api` directory.
3. Install the required dependencies (you can list them here).
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Access the API at `http://127.0.0.1:5000/`.

## Examples

For usage examples and integration scenarios, check out the [`examples`](../examples/) directory.