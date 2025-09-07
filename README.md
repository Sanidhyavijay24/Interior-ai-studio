# Interior-ai-studio
Transform Any Room with AI-Powered Design Fusion - Real Photos + Inspiration Images = Stunning Visualizations


## Core Features Utilized

**Multi-Image Fusion**: Our application's foundation relies on Gemini's ability to seamlessly blend multiple images - combining real room photographs with inspiration images from various design sources. This creates cohesive design transformations that maintain the original room's architecture while incorporating desired aesthetic elements.

**Advanced Image Editing**: Gemini's natural language image editing capabilities enable users to transform spaces with simple text prompts like "add Scandinavian warmth with natural materials." The model maintains realistic lighting, proportions, and perspective while completely reimagining the room's appearance.

**Architectural Consistency**: The model's understanding of spatial relationships ensures transformed rooms retain structural integrity - windows, doors, and room dimensions remain consistent while furniture, colors, and decor are intelligently redesigned.

**Scene Understanding**: Gemini analyzes room layouts, lighting conditions, and existing elements to generate contextually appropriate designs. This prevents unrealistic transformations and ensures proper furniture placement and lighting integration.

**Visual Continuity**: When generating multiple design variations, the model maintains the same viewpoint and architectural features, enabling meaningful before/after comparisons essential for interior design decision-making.

These capabilities collectively enable InteriorAI Studio to bridge the gap between imagination and reality in interior design, making professional-quality room transformations accessible through simple image uploads and text descriptions.


# 🏠 InteriorAI Studio

**Transform Any Room with AI-Powered Design Fusion - Real Photos + Inspiration Images = Stunning Visualizations**

An AI-powered interior design application that uses Google's Gemini 2.5 Flash Image Preview to transform real room photos into stunning design visualizations.

## ✨ Features

- **Room Analysis**: AI analyzes existing rooms to understand layout, style, and improvement areas
- **Style Transformation**: Redesigns rooms while maintaining architectural integrity  
- **Multiple Variations**: Creates different design approaches for the same space
- **Inspiration Fusion**: Combines multiple inspiration images with real room photos
- **Shopping Lists**: Generates actionable shopping guides based on transformations

## 🚀 Quick Start (Kaggle Only)

### Prerequisites
- Kaggle account
- Google AI API key (free)

### Step 1: Get Your API Key
1. Visit [Google AI Studio](https://ai.google.dev/aistudio)
2. Sign up/login with your Google account
3. Click "Get API Key" → "Create API Key"
4. Copy the generated API key (keep it secure!)

### Step 2: Open the Notebook in Kaggle
1. Go to [Kaggle.com](https://www.kaggle.com) and sign in
2. Click "Create" → "New Notebook"
3. Download the `InteriorAI_Studio.ipynb` file from this repository
4. In Kaggle, click "File" → "Upload Notebook"
5. Select the downloaded `.ipynb` file

### Step 3: Add Your API Key to Kaggle Secrets
1. In your Kaggle notebook, click "Add-ons" → "Secrets"
2. Click "Add New Secret"
3. **Name**: `gemini_api_key`
4. **Value**: Paste your API key from Step 1
5. Click "Add"

### Step 4: Run the Notebook
1. Click "Run All" or run cells individually
2. The notebook will automatically:
  - Install required packages
  - Initialize the Gemini client
  - Generate a sample room demonstration
  - Show room analysis and transformations
  - Create shopping lists

## 📸 Using Your Own Room Photos

1. Upload your room photos to Kaggle:
  - Click "Input" → "Upload" in your notebook
  - Select your room images

2. Modify the code to use your images:
```python
# Replace the sample room generation with your uploaded image
your_room_file = "/kaggle/input/your-dataset/your_room_photo.jpg"

# Analyze your room
analysis = analyze_room(your_room_file)

# Transform with different styles
modern_design = redesign_room(your_room_file, "Modern minimalist with white furniture and plants")
cozy_design = redesign_room(your_room_file, "Cozy rustic with warm woods and textures")
