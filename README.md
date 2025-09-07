# Interior-ai-studio
Transform Any Room with AI-Powered Design Fusion - Real Photos + Inspiration Images = Stunning Visualizations


## Core Features Utilized

**Multi-Image Fusion**: Our application's foundation relies on Gemini's ability to seamlessly blend multiple images - combining real room photographs with inspiration images from various design sources. This creates cohesive design transformations that maintain the original room's architecture while incorporating desired aesthetic elements.

**Advanced Image Editing**: Gemini's natural language image editing capabilities enable users to transform spaces with simple text prompts like "add Scandinavian warmth with natural materials." The model maintains realistic lighting, proportions, and perspective while completely reimagining the room's appearance.

**Architectural Consistency**: The model's understanding of spatial relationships ensures transformed rooms retain structural integrity - windows, doors, and room dimensions remain consistent while furniture, colors, and decor are intelligently redesigned.

**Scene Understanding**: Gemini analyzes room layouts, lighting conditions, and existing elements to generate contextually appropriate designs. This prevents unrealistic transformations and ensures proper furniture placement and lighting integration.

**Visual Continuity**: When generating multiple design variations, the model maintains the same viewpoint and architectural features, enabling meaningful before/after comparisons essential for interior design decision-making.

These capabilities collectively enable InteriorAI Studio to bridge the gap between imagination and reality in interior design, making professional-quality room transformations accessible through simple image uploads and text descriptions.


🏠 InteriorAI Studio - Setup & Usage Guide
Prerequisites

Kaggle account
Google AI API key (free at https://ai.studio/banana)

Step 1: Get Your API Key

Visit https://ai.studio/banana
Sign up/login with Google account
Create new API key
Copy the key (keep it secure!)

Step 2: Setup on Kaggle

Go to Kaggle.com
Create new notebook
Copy the code from the GitHub .py file
Paste it into a new Kaggle notebook

Step 3: Add API Key to Kaggle Secrets

In your Kaggle notebook, click "Add-ons" → "Secrets"
Click "Add New Secret"
Name: gemini_api_key
Value: Paste your API key from Step 1
Click "Add"

Step 4: Run the Code

Click "Run All" in Kaggle notebook
Wait for packages to install
The code will automatically:

Generate a sample room
Analyze the room
Create design transformations
Generate shopping lists



Step 5: Try Your Own Images

Upload your room photos to Kaggle
Replace sample_room_file with your image path
Modify design prompts in the redesign_room() calls
Run specific cells to test different styles

Example Usage:
python# Analyze your room
analysis = analyze_room("your_room_photo.jpg")

# Transform with different styles
modern_designs = redesign_room("your_room_photo.jpg", "Modern minimalist with white furniture and plants")
cozy_designs = redesign_room("your_room_photo.jpg", "Cozy rustic with warm woods and soft textures")

# Generate shopping list
shopping_list = generate_shopping_list("your_room_photo.jpg", modern_designs[0])
API Limits (Free Tier)

20 images per minute
200 requests per day
Add delays between requests if needed

Troubleshooting

API Error: Check your API key in secrets
Rate Limit: Wait 1-2 minutes between generations
No Images: Verify your API key has image generation enabled

Ready to Transform! 🎨
Once setup is complete, you'll have a fully functional AI interior designer that can transform any room photo into stunning design visualizations!
