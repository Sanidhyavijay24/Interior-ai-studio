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

## 🚀 Quick Start

### Prerequisites
- Kaggle account
- Google AI API key (free at https://ai.studio/banana)

### Setup Instructions

1. **Get Your API Key**
  - Visit https://ai.studio/banana
  - Sign up/login with Google account
  - Create new API key
  - Copy the key (keep it secure!)

2. **Setup on Kaggle**
  - Go to [Kaggle.com](https://www.kaggle.com)
  - Create new notebook
  - Copy the code from `interior_ai_studio.py`
  - Paste it into your Kaggle notebook

3. **Add API Key to Kaggle Secrets**
  - In your Kaggle notebook, click **"Add-ons"** → **"Secrets"**
  - Click **"Add New Secret"**
  - Name: `gemini_api_key`
  - Value: Paste your API key from Step 1
  - Click **"Add"**

4. **Run the Code**
  - Click **"Run All"** in Kaggle notebook
  - Wait for packages to install
  - The code will automatically generate demo transformations

### Try Your Own Images

```python
# Analyze your room
analysis = analyze_room("your_room_photo.jpg")

# Transform with different styles
modern_designs = redesign_room("your_room_photo.jpg", "Modern minimalist with white furniture and plants")
cozy_designs = redesign_room("your_room_photo.jpg", "Cozy rustic with warm woods and soft textures")

# Generate shopping list
shopping_list = generate_shopping_list("your_room_photo.jpg", modern_designs[0])
