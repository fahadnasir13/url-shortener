# Import required libraries
from flask import Flask, request, jsonify  # Flask handles web routes & JSON
from flask_pymongo import PyMongo  # For connecting Flask to MongoDB
from datetime import datetime  # To store timestamps
import string, random  # Used to generate random short codes
import os  # Access environment variables
from dotenv import load_dotenv  # Load variables from .env file

# Load MongoDB URI and any other config from the .env file
load_dotenv()

# Create a new Flask app
app = Flask(__name__)

# Set up MongoDB connection
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/urlshortener")

# Connect Flask app to MongoDB using PyMongo
mongo = PyMongo(app)

# Point to the collection inside MongoDB where short URLs will be stored
urls_collection = mongo.db.urls

# Utility: Generate a random 6-character short code (like a1B2c3)
def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0–9
    return ''.join(random.choices(characters, k=length))



# Route: Create a new short URL
@app.route("/shorten", methods=["POST"])
def create_short_url():
    # Get the data sent in JSON format from client
    data = request.get_json()
    
    # Extract the original URL from JSON
    original_url = data.get("url")

    # Validate: If no URL was sent, return error
    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    # Generate a unique short code that doesn’t exist in DB
    shortcode = generate_shortcode()
    while urls_collection.find_one({"shortCode": shortcode}):
        shortcode = generate_shortcode()

    # Get current timestamp
    now = datetime.utcnow()

    # Create MongoDB document
    new_url = {
        "url": original_url,         # the full URL to store
        "shortCode": shortcode,      # the shortened code
        "createdAt": now,            # when it was created
        "updatedAt": now,            # last updated (same for now)
        "accessCount": 0             # how many times accessed
    }

    # Insert document into MongoDB
    result = urls_collection.insert_one(new_url)

    # Add the MongoDB ID to the response
    new_url["id"] = str(result.inserted_id)

    # Return the new URL info and 201 Created status
    return jsonify(new_url), 201
@app.route("/")
def homepage():
    return app.send_static_file("index.html")

# Route: Retrieve the original URL from a short code
@app.route("/shorten/<shortcode>", methods=["GET"])
def get_original_url(shortcode):
    # Find the document in MongoDB where shortCode matches
    url_data = urls_collection.find_one({"shortCode": shortcode})

    # If not found, return 404 Not Found
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404

    # Increase the accessCount by 1
    urls_collection.update_one(
        {"shortCode": shortcode},
        {"$inc": {"accessCount": 1}}
    )

    # Prepare response by converting MongoDB's _id to string
    url_data["id"] = str(url_data["_id"])
    del url_data["_id"]  # remove raw ObjectId from response

    return jsonify(url_data), 200


# Route: Update the original URL for a short code
@app.route("/shorten/<shortcode>", methods=["PUT"])
def update_short_url(shortcode):
    # Get the new data from the request body
    data = request.get_json()
    updated_url = data.get("url")

    # Validate: Must have a new URL
    if not updated_url:
        return jsonify({"error": "URL is required"}), 400

    # Find and update the document in one step
    result = urls_collection.find_one_and_update(
        {"shortCode": shortcode},  # Find this short code
        {"$set": {
            "url": updated_url,
            "updatedAt": datetime.utcnow()
        }},
        return_document=True  # Return updated document
    )

    # If shortCode not found
    if not result:
        return jsonify({"error": "Short URL not found"}), 404

    # Clean the result for JSON response
    result["id"] = str(result["_id"])
    del result["_id"]

    return jsonify(result), 200



# Route: Delete a short URL
@app.route("/shorten/<shortcode>", methods=["DELETE"])
def delete_short_url(shortcode):
    # Try to delete the document from MongoDB
    result = urls_collection.delete_one({"shortCode": shortcode})

    # If nothing was deleted (shortCode not found)
    if result.deleted_count == 0:
        return jsonify({"error": "Short URL not found"}), 404

    # Return 204 No Content (successful deletion, no body)
    return '', 204
# Route: Get statistics for a short URL
@app.route("/shorten/<shortcode>/stats", methods=["GET"])
def get_url_stats(shortcode):
    # Find the document in MongoDB by shortCode
    url_data = urls_collection.find_one({"shortCode": shortcode})

    # If not found, return 404
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404

    # Convert MongoDB ObjectId for clean JSON output
    url_data["id"] = str(url_data["_id"])
    del url_data["_id"]

    return jsonify(url_data), 200
from flask import redirect

@app.route("/r/<shortcode>")
def redirect_to_url(shortcode):
    url_data = urls_collection.find_one({"shortCode": shortcode})
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404

    # Increment access count
    urls_collection.update_one({"shortCode": shortcode}, {"$inc": {"accessCount": 1}})
    return redirect(url_data["url"])


if __name__ == "__main__":
    app.run(debug=True)




    # Route: Redirect from short URL to original URL
from flask import redirect

@app.route("/r/<shortcode>")
def redirect_to_url(shortcode):
    url_data = urls_collection.find_one({"shortCode": shortcode})
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404
    # Increment accessCount
    urls_collection.update_one({"shortCode": shortcode}, {"$inc": {"accessCount": 1}})
    return redirect(url_data["url"])
