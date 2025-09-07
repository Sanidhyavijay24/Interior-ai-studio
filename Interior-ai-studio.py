# 🏠 VIRTUAL INTERIOR DESIGNER - NANO BANANA HACKATHON
# Transform any room with AI-powered design visualization
# Competition: https://www.kaggle.com/competitions/banana

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║  VIRTUAL INTERIOR DESIGNER - Gemini 2.5 Flash Image Preview              ║
║  Real room + inspiration images = stunning design visualizations         ║
║  Win your share of $400,000+ in prizes!                                  ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

print("🏠 Starting Virtual Interior Designer...")
print("=" * 80)

# ============================================================================
# SECTION 1: IMPORTS AND SETUP
# ============================================================================

import os
import sys
import time
import mimetypes
from datetime import datetime
from PIL import Image
from io import BytesIO
from IPython.display import display, Markdown, HTML

print("✅ Standard libraries imported")

# Install required packages
print("\n📦 Installing required packages...")
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "-q", "google-genai>=1.32.0", "Pillow"])
print("✅ Packages installed")

# Import Google Gemini
from google import genai
from google.genai import types
print("✅ Google Gemini SDK imported")

# ============================================================================
# SECTION 2: API KEY CONFIGURATION
# ============================================================================

print("\n" + "=" * 80)
print("🔑 CONFIGURING API KEY")
print("=" * 80)

try:
    from kaggle_secrets import UserSecretsClient
    user_secrets = UserSecretsClient()
    GOOGLE_API_KEY = user_secrets.get_secret("gemini_api_key")
    if GOOGLE_API_KEY:
        print("✅ API key loaded from Kaggle secrets")
    else:
        raise ValueError("No API key found")
except Exception as e:
    print(f"❌ Error loading API key: {e}")
    print("\n📝 INSTRUCTIONS:")
    print("1. Get your FREE API key at: https://ai.studio/banana")
    print("2. In Kaggle, go to 'Add-ons' -> 'Secrets'")
    print("3. Add a new secret named 'gemini_api_key' with your API key")
    raise

# ============================================================================
# SECTION 3: INITIALIZE CLIENT
# ============================================================================

print("\n" + "=" * 80)
print("🚀 INITIALIZING CLIENT")
print("=" * 80)

client = genai.Client(api_key=GOOGLE_API_KEY)
MODEL_ID = "gemini-2.5-flash-image-preview"
MODEL_TEXT = "gemini-2.5-flash"

print(f"✅ Client initialized")
print(f"📷 Image Model: {MODEL_ID}")

# ============================================================================
# SECTION 4: HELPER FUNCTIONS
# ============================================================================

print("\n" + "=" * 80)
print("🛠️ SETTING UP HELPER FUNCTIONS")
print("=" * 80)

def save_image(data, filename):
    """Save binary image data to file"""
    with open(filename, "wb") as f:
        f.write(data)
    print(f"💾 Saved: {filename}")
    return filename

def display_image(image_data):
    """Display image from binary data"""
    try:
        image = Image.open(BytesIO(image_data))
        print(f"📷 Image: {image.size[0]}x{image.size[1]} pixels")
        display(image)
        return image
    except Exception as e:
        print(f"⚠️ Could not display image: {e}")
        return None

def extract_images_from_response(response, prefix="design"):
    """Extract and save all images from API response"""
    saved_files = []
    
    if not response or not hasattr(response, 'candidates'):
        return saved_files
    
    for candidate in response.candidates:
        if hasattr(candidate, 'content') and candidate.content:
            if hasattr(candidate.content, 'parts'):
                for i, part in enumerate(candidate.content.parts):
                    if hasattr(part, 'inline_data') and part.inline_data:
                        if hasattr(part.inline_data, 'data') and part.inline_data.data:
                            timestamp = datetime.now().strftime("%H%M%S")
                            filename = f"{prefix}_{timestamp}_{i}.png"
                            save_image(part.inline_data.data, filename)
                            display_image(part.inline_data.data)
                            saved_files.append(filename)
    
    return saved_files

print("✅ Helper functions ready")

# ============================================================================
# SECTION 5: CORE INTERIOR DESIGN FUNCTIONS
# ============================================================================

print("\n" + "=" * 80)
print("🏠 VIRTUAL INTERIOR DESIGNER CORE FUNCTIONS")
print("=" * 80)

def analyze_room(room_image_path):
    """Analyze the current room to understand layout, lighting, and style"""
    print(f"🔍 Analyzing room: {room_image_path}")
    
    try:
        room_image = Image.open(room_image_path)
        
        analysis_prompt = """Analyze this room image and provide:
1. Room type (living room, bedroom, kitchen, etc.)
2. Current style (modern, traditional, minimalist, etc.)
3. Key furniture pieces present
4. Lighting conditions (natural light, artificial, etc.)
5. Color scheme
6. Room dimensions estimate (small, medium, large)
7. Architectural features (windows, doors, ceiling height, etc.)
8. Areas that need improvement

Be detailed and specific for interior design purposes."""
        
        response = client.models.generate_content(
            model=MODEL_TEXT,
            contents=[analysis_prompt, room_image]
        )
        
        analysis = response.text if response else "Analysis failed"
        print("✅ Room analysis complete!")
        print(f"📝 Analysis:\n{analysis}")
        return analysis
        
    except Exception as e:
        print(f"❌ Room analysis failed: {e}")
        return None

def redesign_room(room_image_path, style_prompt, budget_level="medium"):
    """Main function to redesign a room with AI"""
    print(f"🎨 Redesigning room with style: {style_prompt}")
    print(f"💰 Budget level: {budget_level}")
    
    try:
        room_image = Image.open(room_image_path)
        
        # Create comprehensive redesign prompt
        redesign_prompt = f"""Transform this room with the following design vision: {style_prompt}

DESIGN REQUIREMENTS:
- Maintain the room's basic layout and architectural features
- Keep realistic proportions and perspective
- Ensure proper lighting that matches the original room's light sources
- Create a cohesive color scheme and style
- Budget level: {budget_level} (affects furniture quality and quantity)

SPECIFIC TRANSFORMATIONS:
- Update wall colors and textures
- Replace or add furniture pieces that fit the style
- Add appropriate decor and accessories
- Improve lighting fixtures if needed
- Add plants, artwork, or other styling elements
- Ensure the space feels lived-in and functional

OUTPUT: Generate a photorealistic "after" image that shows the transformed room while maintaining the same camera angle and perspective as the original."""
        
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[redesign_prompt, room_image],
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )
        
        if response:
            print("✅ Room redesign complete!")
            saved_files = extract_images_from_response(response, "redesigned_room")
            return saved_files
        else:
            print("❌ No response received")
            return []
            
    except Exception as e:
        print(f"❌ Room redesign failed: {e}")
        return []

def create_design_variations(room_image_path, base_style, num_variations=3):
    """Create multiple design variations of the same room"""
    print(f"🎨 Creating {num_variations} design variations...")
    
    style_variations = {
        1: f"{base_style} with warm, cozy elements",
        2: f"{base_style} with bold, statement pieces", 
        3: f"{base_style} with minimalist, clean approach"
    }
    
    all_designs = []
    
    for i in range(1, num_variations + 1):
        print(f"\n🎯 Creating variation {i}: {style_variations[i]}")
        designs = redesign_room(room_image_path, style_variations[i])
        all_designs.extend(designs)
        time.sleep(2)  # Rate limiting
    
    print(f"✅ Created {len(all_designs)} design variations!")
    return all_designs

def fusion_design_inspiration(room_image_path, inspiration_images, design_goal):
    """Fuse multiple inspiration images with the room for unique designs"""
    print(f"🔥 Creating fusion design with {len(inspiration_images)} inspiration images")
    
    try:
        room_image = Image.open(room_image_path)
        inspiration_imgs = [Image.open(img_path) for img_path in inspiration_images]
        
        fusion_prompt = f"""Create a stunning interior design by fusing elements from these inspiration images into this room.

DESIGN GOAL: {design_goal}

FUSION INSTRUCTIONS:
- Extract the best design elements from each inspiration image
- Seamlessly blend colors, textures, and styles from the inspirations
- Maintain the room's architecture and layout
- Create a harmonious design that incorporates multiple inspiration sources
- Ensure realistic lighting and proportions
- The result should feel cohesive despite multiple influences

Generate a photorealistic transformation that shows how these inspirations would look in this actual space."""
        
        # Combine all images in the prompt
        content_parts = [fusion_prompt, room_image] + inspiration_imgs
        
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=content_parts,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )
        
        if response:
            print("✅ Fusion design complete!")
            saved_files = extract_images_from_response(response, "fusion_design")
            return saved_files
        
        return []
        
    except Exception as e:
        print(f"❌ Fusion design failed: {e}")
        return []

def generate_shopping_list(room_image_path, redesigned_image_path):
    """Generate a shopping list based on the room transformation"""
    print("🛒 Generating shopping list...")
    
    try:
        original_room = Image.open(room_image_path)
        redesigned_room = Image.open(redesigned_image_path)
        
        shopping_prompt = """Compare these two room images (before and after) and create a detailed shopping list.

ANALYZE:
- What furniture pieces were added or changed?
- What decor items are new?
- What lighting fixtures are different?
- What colors/materials are used?

GENERATE:
- Detailed shopping list with specific items
- Estimated price ranges for each category
- Priority levels (must-have vs. nice-to-have)
- Alternative budget options
- Where to shop for each type of item

Format as a practical shopping guide that someone could actually use."""
        
        response = client.models.generate_content(
            model=MODEL_TEXT,
            contents=[shopping_prompt, original_room, redesigned_room]
        )
        
        if response:
            shopping_list = response.text
            print("✅ Shopping list generated!")
            print("\n" + "="*60)
            print("🛒 YOUR INTERIOR DESIGN SHOPPING LIST")
            print("="*60)
            print(shopping_list)
            return shopping_list
        
        return None
        
    except Exception as e:
        print(f"❌ Shopping list generation failed: {e}")
        return None

# ============================================================================
# SECTION 6: DEMO AND TESTING
# ============================================================================

print("\n" + "=" * 80)
print("🎬 DEMO: VIRTUAL INTERIOR DESIGNER")
print("=" * 80)

# Create a sample room for testing
def create_sample_room():
    """Generate a sample room image for testing"""
    print("🏠 Creating sample room for demonstration...")
    
    sample_prompt = """Create a photorealistic image of a basic, empty living room that needs interior design help:
- Plain white walls
- Hardwood floors
- Large window with natural light
- Basic furniture: old brown sofa, small coffee table
- Room feels outdated and lacks personality
- Shot from a corner showing good room perspective
- 8K quality, realistic lighting"""
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[sample_prompt],
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE']
        )
    )
    
    if response:
        saved_files = extract_images_from_response(response, "sample_room")
        return saved_files[0] if saved_files else None
    return None

# Generate sample room
sample_room_file = create_sample_room()

if sample_room_file:
    print(f"\n✅ Sample room created: {sample_room_file}")
    
    # Analyze the room
    room_analysis = analyze_room(sample_room_file)
    
    # Create redesigns
    print("\n🎨 Testing different design styles...")
    
    # Style 1: Modern Scandinavian
    modern_designs = redesign_room(
        sample_room_file, 
        "Modern Scandinavian style with light colors, natural materials, cozy textures, and plants",
        "medium"
    )
    
    # Style 2: Warm Industrial
    time.sleep(3)  # Rate limiting
    industrial_designs = redesign_room(
        sample_room_file,
        "Warm industrial style with exposed brick accent wall, leather furniture, metal fixtures, and warm lighting",
        "high"
    )
    
    # Generate shopping list if we have a redesigned room
    if modern_designs:
        shopping_list = generate_shopping_list(sample_room_file, modern_designs[0])

print("\n" + "=" * 80)
print("🏆 HACKATHON SUBMISSION READY!")
print("=" * 80)

hackathon_summary = """
## 🏠 Virtual Interior Designer - Project Summary

### Core Features:
1. **Room Analysis**: AI analyzes existing rooms to understand layout, style, and needs
2. **Style Transformation**: Redesigns rooms with specific style prompts while maintaining architecture
3. **Multiple Variations**: Creates different design approaches for the same space
4. **Inspiration Fusion**: Combines multiple inspiration images with real rooms
5. **Shopping Lists**: Generates actionable shopping guides based on transformations

### Gemini 2.5 Flash Image Features Used:
- **Multi-image Fusion**: Combines room photos with inspiration images
- **Image Editing**: Transforms existing room photos while maintaining perspective
- **Visual Consistency**: Maintains architectural features and lighting across transformations
- **Detailed Scene Generation**: Creates photorealistic interior designs

### Innovation & Impact:
- **Real World Problem**: Helps people visualize interior design changes before spending money
- **E-commerce Integration**: Ready for furniture/decor shopping platform integration
- **Cost Savings**: Reduces need for expensive interior design consultations
- **Accessibility**: Makes professional-quality design accessible to everyone

### Technical Excellence:
- Maintains realistic proportions and lighting
- Preserves room architecture while transforming aesthetics
- Handles multiple design styles and budget levels
- Generates actionable, practical outputs

### Potential Extensions:
- Mobile app for real-time room scanning
- AR visualization of proposed changes
- Integration with furniture retailers
- Cost estimation and budgeting tools
- Social sharing of designs
"""

display(Markdown(hackathon_summary))

# Final file count
all_files = [f for f in os.listdir('.') if f.endswith(('.png', '.jpg', '.jpeg'))]
print(f"\n✅ Total images generated: {len(all_files)}")
print(f"📁 Project files ready for submission!")

print("\n" + "=" * 80)
print("🎉 VIRTUAL INTERIOR DESIGNER - READY TO WIN! 🏠")
print("=" * 80)